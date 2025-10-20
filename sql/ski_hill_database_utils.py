import sqlite3
import random
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

DB_PATH = "ski_hill.db"
RNG = random.Random(58)

def create_mountain_huts_table(
        cur: sqlite3.Cursor,
        n_huts: int = 5
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

    names = [
        "Abby", "Base", "Chalet", "Deepti", "Eileen", "Frederic", "Goodall", "Henrik", 
        "Ishi", "Jackolantern", "Koala", "Llama", "Marino J", "Nuance", "Oval", "Pecunia", 
        "Quartile", "Responder", "Septuagint", "Tibult", "Union", "Vail", "Watanabe", 
        "Xerxes", "YKnot", "Zephyr"
    ]
    suffixes = [
        "2", "II", "Not", "?"
    ]

    mountain_huts = []
    for hut in range(n_huts):
        name = f"{RNG.choice(names)} {RNG.choice(names)}"
        if RNG.random() > 0.9:
            name += f" {RNG.choice(suffixes)}"
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
        n_huts: int = 5
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
        # if RNG.random() > 0.8:
        #     # increase the chance of orphaned huts
        #     continue
        if RNG.random() > 0.6:
            hut1 = hut
            hut2 = RNG.randint(1, n_huts)
        else:
            hut1 = RNG.randint(1, n_huts)
            hut2 = hut
        trails.append((hut1, hut2))
        # surrounded in try-catch to avoid errors from duplicates
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
    db_name: str = DB_PATH,
    n_huts: int = 5
) -> None:
    """
    Create an SQLite DB with 'mountain_huts' and 'trails' tables
    All analytics must be derived from these table (no views).
    """
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()

    # Reset
    # TODO: consider adding base camp or lodge
    create_mountain_huts_table(cur, n_huts)
    create_trails_table(cur, n_huts)

    conn.commit()
    conn.close()

    print(f"SQLite database '{db_name}' created with a 'mountain_huts' table and 'trails' table.")


def get_schema(db_path: str = DB_PATH) -> str:
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


def execute_sql(query: str, db_path: str = DB_PATH) -> pd.DataFrame:
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

def graph_ski_routes(db_path: str = DB_PATH) -> nx.DiGraph:
    """
    Visualize the Routes defined in the specified database path
    :param db_path: path to database containing mountain_huts and trails tables
    """
    mountain_huts = execute_sql("select * from mountain_huts", db_path)
    trails = execute_sql("select * from trails", db_path)
    
    graph = nx.DiGraph()

    for idx, hut in mountain_huts.iterrows():
        graph.add_node(hut["name"])

    mountain_huts.set_index(keys="id", inplace=True)
    for hut1_idx, hut2_idx in trails.itertuples(index=False):
        hut1_series = mountain_huts.loc[hut1_idx]
        hut2_series = mountain_huts.loc[hut2_idx]
        if hut1_series["altitude"] > hut2_series["altitude"]:
            graph.add_edge(u_of_edge=hut1_series["name"],
                           v_of_edge=hut2_series["name"],
                           length=hut1_series["altitude"]-hut2_series["altitude"])
        else:
            graph.add_edge(u_of_edge=hut2_series["name"],
                           v_of_edge=hut1_series["name"],
                           length=hut2_series["altitude"]-hut1_series["altitude"])
    
    # TODO: adjust node x-positions based on connections
    pos = nx.planar_layout(graph)

    plt.figure(figsize=(12,10))
    nx.draw(graph,
            pos=pos,
            with_labels=True,
            font_size=12)
    plt.title("Ski Routes")
    plt.show()

    return graph