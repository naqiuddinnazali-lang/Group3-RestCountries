# This script is responsible for managing the SQLite database that will store the country population data.

# It includes functions to initialize the database, save country population data to the database, and retrieve records.



import sqlite3

import json



# Define the name of the SQLite database file.

DB_NAME = "country_population.db"



# This function establishes a connection to the SQLite database and sets the row factory to # sqlite3.Row,

# which allows accessing columns by name. It returns the connection object.

def get_connection():

    conn = sqlite3.connect(DB_NAME)

    conn.row_factory = sqlite3.Row

    return conn



# This function initializes the database by creating a table named 'records' if it does not already exist.

# The table has columns for created_at, id, and data (which will store the top 10 population countries data as a

# JSON string).

def int_db():

    conn = get_connection()

    cursor = conn.cursor()



    # Create a table named 'records' if it does not already exist. The table has columns for created_at,

    # id and data.

    cursor.execute("""

        CREATE TABLE IF NOT EXISTS records (

            created_at datetime default current_timestamp,

            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,

            country TEXT NOT NULL,

            capital TEXT NOT NULL,

            region TEXT NOT NULL,

            subregion TEXT NOT NULL,

            population INTEGER NOT NULL

        )

    """

)



    # Commit the transaction to save the changes to the database and close the connection.

    conn.commit()

    conn.close()



# This function normalizes a country dictionary to a tuple suitable for database insertion.

# It extracts the country name, capital, region, subregion, and population from the input

# dictionary, providing default values if any of the expected keys are missing.

def _normalize_country(item: dict) -> tuple:

    return (

        item.get("country") or item.get("name") or "N/A",

        item.get("capital") or "N/A",

        item.get("region") or "N/A",

        item.get("subregion") or "N/A",

        int(item.get("population") or 0),

    )



# This function saves the country data to the database. It accepts either a single country dictionary or a list of country dictionaries.

# dictionary or a list of country dictionaries.

def save_db(data):

    # Accept a single country dict or a list of country dicts.

    items = data if isinstance(data, list) else [data]



    conn = get_connection()

    cursor = conn.cursor()



    # Insert each country into the database and keep track of the inserted IDs for retrieval.

    inserted_ids = []

    for item in items:

        country, capital, region, subregion, population = _normalize_country(item)

        cursor.execute(

            """

            INSERT INTO records (country, capital, region, subregion, population)

            VALUES (?, ?, ?, ?, ?)

            """,

            (country, capital, region, subregion, population),

        )

        inserted_ids.append(cursor.lastrowid)



    conn.commit()



    # Retrieve the inserted records using the inserted IDs to return the complete record

    # with the created_at timestamp.

    placeholders = ",".join("?" for _ in inserted_ids)

    cursor.execute(

        f"SELECT * FROM records WHERE id IN ({placeholders}) ORDER BY id",

        inserted_ids,

    )

    records = cursor.fetchall()

    conn.close()



    # Convert the retrieved records to a list of dictionaries for easier consumption.

    result = [

        {

            "created_at": row["created_at"],

            "id": row["id"],

            "country": row["country"],

            "capital": row["capital"],

            "region": row["region"],

            "subregion": row["subregion"],

            "population": row["population"],

        }

        for row in records

    ]



    return result if isinstance(data, list) else result[0]



# The following code block is executed only when the script is run directly (not imported as a module).

if __name__ == "__main__":

    from g3_condition import get_top_10_highest_population_countries

   

    int_db()



    data = get_top_10_highest_population_countries()

    record = save_db(data)

    print(json.dumps(record, indent=2))