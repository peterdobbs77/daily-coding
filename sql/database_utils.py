import sqlite3
import random
import datetime
import pandas as pd

RNG = random.Random(58)
COMPANY_START_DATE = datetime.datetime(1996, 5, 8)

IS_LIMITED_EDITION_LIKELIHOOD = 0.05 # 5% of products should be limited edition


def create_employees_table(
        cur: sqlite3.Cursor,
        n_employees: int = 5
) -> list:
    """
    Initializes table 'employees' with randomly generated staff
    Returns employee roster
    """
    cur.execute("DROP TABLE IF EXISTS employees")
    cur.execute("""
    CREATE TABLE employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        department TEXT NOT NULL,
        salary INTEGER NOT NULL,
        start_date DATE DEFAULT CURRENT_DATE
    )
    """)

    names = ["Abby", "Bruno", "Charles", "Deepti", "Eileen", "Frederic", "Goodall", "Henrik", "Ishi", "Watanabe", "Zephyr"]
    departments = ["sales", "stock", "fitting", "corporate"]

    max_date = datetime.datetime.today()
    employee_roster = []
    for empl in range(n_employees):
        # populate table with employees
        name = f"{RNG.choice(names)} {RNG.choice(names)}"
        department = RNG.choice(departments)
        salary = RNG.randint(45000, 60000)
        if department == "corporate":
            salary = RNG.randint(90000, 150000)
        start_date = COMPANY_START_DATE + (max_date - COMPANY_START_DATE) * RNG.random()
        employee_roster.append((empl+1, name, department, salary, start_date))
        cur.execute("""
            INSERT INTO employees (
                name, department, salary, start_date
            ) VALUES (?, ?, ?, ?)
        """, (name, department, salary, start_date))

    return employee_roster


def create_products_table(
        cur: sqlite3.Cursor,
        n_products: int = 10
) -> list:
    """
    Initializes table 'products' with randomly generated stuff
    Returns product inventory
    """
    cur.execute("DROP TABLE IF EXISTS products")
    # product table as reference for transactions
    cur.execute("""
    CREATE TABLE products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        brand TEXT NOT NULL,
        category TEXT NOT NULL,
        color TEXT NOT NULL,
        is_limited INTEGER DEFAULT 0,  -- boolean for tracking limited edition releases
        notes TEXT,
        release_date DATE DEFAULT CURRENT_DATE
    )
    """)
    
    brands = ["Nike", "Adidas", "Puma", "Reebok", "New Balance"]
    categories = ["shoes", "hoodie", "t-shirt", "hat", "backpack", 'cleats']
    colors = ["black", "white", "red", "blue", "green", 'cream']

    max_release_date = datetime.datetime.today()
    product_catalog = []
    for pid in range(1, n_products + 1):
        name = f"{RNG.choice(brands)} {RNG.choice(categories)}"
        brand = name.split()[0]
        category = name.split()[1]
        color = RNG.choice(colors)
        is_limited = 0 if RNG.random() > IS_LIMITED_EDITION_LIKELIHOOD else 1
        release_date = COMPANY_START_DATE + (max_release_date - COMPANY_START_DATE) * RNG.random()
        base_price = round(RNG.uniform(20.0, 150.0), 2)
        product_catalog.append((pid, name, brand, category, color, is_limited, release_date, base_price))
        cur.execute("""
            INSERT INTO products (
                name, brand, category, color, is_limited, release_date
            ) VALUES (?, ?, ?, ?, ?, ?)
        """, (name, brand, category, color, is_limited, release_date))

    return product_catalog


def create_db(
    db_name: str = "products.db",
    n_employees: int = 5,
    n_products: int = 10,
    n_txns_per_product: int = 50,
) -> None:
    """
    Create an SQLite DB with a 'transactions' table (event-sourced),
        a 'products' table (reference for 'transactions'),
        and an 'employees' table (reference for 'transactions')
    All analytics must be derived from these table (no views).
    """
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()

    # Reset
    cur.execute("DROP TABLE IF EXISTS transactions")

    # Event-sourced transactions table
    # TODO: incorporate different currencies and exchange rate
    cur.execute("""
    CREATE TABLE transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_id INTEGER NOT NULL,
        employee_id INTEGER NOT NULL,

        action TEXT NOT NULL,            -- 'insert' | 'restock' | 'sale' | 'price_update'
        qty_delta INTEGER DEFAULT 0,     -- + for restock/insert, - for sale
        unit_price REAL,                 -- price at the time of the event (NULL for non-price events)
        notes TEXT,                      -- optional
        ts DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

    employee_roster = create_employees_table(cur, n_employees)
    product_catalog = create_products_table(cur, n_products)

    # select a product release manager who is with the company and represents corporate
    release_manager_id = employee_roster[[3] == "corporate"][0]

    # Seed events per product and employee
    for (pid, name, brand, category, color, is_limited, release_date, base_price) in product_catalog:
        # Initial insert (with opening stock and price)
        initial_stock = RNG.randint(500, 5000)
        if is_limited == 1:
            initial_stock = RNG.randint(5,100)
        cur.execute("""
            INSERT INTO transactions (
                product_id, employee_id,
                action, qty_delta, unit_price, notes, ts
            ) VALUES (?, ?, 'insert', ?, ?, ?, ?)
        """, (pid, release_manager_id, initial_stock, base_price,
              f"Initial transaction:insert with stock={initial_stock}, price={base_price}",
              release_date))

        current_price = base_price

        current_date = release_date
        # Follow-up events
        for _ in range(n_txns_per_product - 1):
            # EITHER:
            current_date += (datetime.datetime.today() - current_date) * RNG.random() # leads to exponential growth in revenue
            # OR:
            current_date += (datetime.datetime.today() - current_date) / (n_txns_per_product+1) # leads to linear revenue growth (depending on product launches)
            event_type = RNG.choices(
                ["restock", "sale", "price_update"],
                weights=[0.25, 0.6, 0.15],
                k=1
            )[0]

            random_empl_id = RNG.choice(employee_roster)[0] # TODO: consider refining this per event_type
            if event_type == "restock":
                qty = RNG.randint(1, 25)
                cur.execute("""
                    INSERT INTO transactions (
                        product_id, employee_id,
                        action, qty_delta, unit_price, notes, ts
                    ) VALUES (?, ?, 'restock', ?, NULL, ?, ?)
                """, (pid, random_empl_id, qty,
                      f"Restock +{qty} units",
                      current_date))

            elif event_type == "sale":
                qty = -RNG.randint(1, 10)  # negative
                cur.execute("""
                    INSERT INTO transactions (
                        product_id, employee_id,
                        action, qty_delta, unit_price, notes, ts
                    ) VALUES (?, ?, 'sale', ?, ?, ?, ?)
                """, (pid, random_empl_id, qty, current_price,
                      f"Sale {-qty} units at {current_price}",
                      current_date))

            else:  # price_update
                delta = round(RNG.uniform(-5.0, 5.0), 2)
                current_price = max(1.0, round(current_price + delta, 2))
                cur.execute("""
                    INSERT INTO transactions (
                        product_id, employee_id,
                        action, qty_delta, unit_price, notes, ts
                    ) VALUES (?, ?, 'price_update', 0, ?, ?, ?)
                """, (pid, random_empl_id, current_price,
                      f"Price update to {current_price}",
                      current_date))

    conn.commit()
    conn.close()

    print(f"SQLite database '{db_name}' created with a 'transactions' table (event-sourced), 'products' table, and 'employees' table.")


def get_schema(db_path: str) -> str:
    """
    Return the schemas for all tables.
    """
    schema = f"database at: {db_path}"
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    for table_name in ["employees", "products", "transactions"]:
        cur.execute(f"PRAGMA table_info({table_name})")
        rows = cur.fetchall()
        schema += f"\n\ntable name: {table_name}\n" + "\n".join([f"{r[1]} ({r[2]})" for r in rows])
    conn.close()
    return schema


def execute_sql(query: str, db_path: str) -> pd.DataFrame:
    """
    Execute any SELECT over the tables.
    """
    q = query.strip().removeprefix("```sql").removesuffix("```").strip()
    conn = sqlite3.connect(db_path)
    try:
        return pd.read_sql_query(q, conn)
    except Exception as e:
        print(str(e))
        return pd.DataFrame({"error": [str(e)]})
    finally:
        conn.close()