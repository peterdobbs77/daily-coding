import sqlite3
import random
import datetime
import pandas as pd

RNG = random.Random(58)

def create_mountain_huts_table(
        cur: sqlite3.Cursor,
        n_huts: int = 10
) -> list:
    """
    Initializes table 'mountain_huts' with randomly generated staff
    Returns list of mountain huts
    """
    cur.execute("DROP TABLE IF EXISTS mountain_huts")
    cur.execute("""
    create table mountain_huts (
        id integer primary key autoincrement,
        name varchar(40) not null,
        altitude integer not null,
        unique(name),
        unique(id)
    );
    """)

    names = ["Abby", "Bruno", "Charles", "Deepti", "Eileen", "Frederic", "Goodall", "Henrik", "Ishi", "Watanabe", "Zephyr"]

    mountain_huts = []
    for hut in range(n_huts):
        # populate table with employees
        name = names[hut]
        altitude = RNG.randint(3000, 15000)
        mountain_huts.append((hut+1, name, altitude))
        cur.execute("""
            INSERT INTO mountain_huts (
                name, altitude
            ) VALUES (?, ?)
        """, (name, altitude))

    return mountain_huts


def create_trails_table(
        cur: sqlite3.Cursor,
        n_huts: list
) -> list:
    """
    Initializes table 'trails' with randomly generated links between huts
    Returns list of trail links between huts
    """
    cur.execute("DROP TABLE IF EXISTS trails")
    # existing trail list between huts
    cur.execute("""
    CREATE TABLE trails (
        hut1 integer not null,
        hut2 integer not null
    )
    """)
    
    trails = []
    for hut in range(1, n_huts+1):
        if RNG.random() > 0.6:
            hut1 = hut
            hut2 = RNG.randint(1, n_huts)
        else:
            hut1 = RNG.randint(1, n_huts)
            hut2 = hut
        trails.append((hut1, hut2))
        try:
            cur.execute("""
                INSERT INTO trails (
                    hut1, hut2
                ) VALUES (?, ?)
            """, (hut1, hut2))
        except Exception as e:
            print(f"Caught exception {e} but proceeding")

    return trails


def create_ski_hill_db(
    db_name: str = "ski_hill.db",
    n_huts: int = 5
) -> None:
    """
    Create an SQLite DB with 'mountain_huts' and 'trails' tables
    All analytics must be derived from these table (no views).
    """
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()

    # Reset
    create_mountain_huts_table(cur, n_huts)
    create_trails_table(cur, n_huts)

    conn.commit()
    conn.close()

    print(f"SQLite database '{db_name}' created with a 'mountain_huts' table and 'trails' table.")

def propose_ski_routes(db_name: str = "ski_hill.db"):
    """
    """
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()

    response = cur.execute(
        """
        WITH bd_trails AS (
            SELECT hut1, hut2 FROM trails
            UNION
            SELECT hut2 AS hut1, hut1 AS hut2 FROM trails
        )
        SELECT 
            start.name AS startpt,
            mid.name AS middlept,
            end.name AS endpt
        FROM bd_trails AS first
        JOIN mountain_huts AS start ON start.id = first.hut1
        JOIN mountain_huts AS mid ON mid.id = first.hut2
        JOIN LATERAL (
            SELECT hut2
            FROM bd_trails
            WHERE hut1 = first.hut2
        ) AS second ON true
        JOIN mountain_huts AS end ON end.id = second.hut2
        WHERE start.altitude > mid.altitude AND mid.altitude > end.altitude;
        """
    )
    
    conn.commit()
    conn.close()

    return response

def get_schema(db_path: str) -> str:
    """
    Return the schemas for all tables.
    """
    schema = f"database at: {db_path}"
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    for table_name in ["mountain_huts", "trails"]:
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