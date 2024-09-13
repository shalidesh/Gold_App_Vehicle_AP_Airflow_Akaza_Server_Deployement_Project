import psycopg2
from .configs import host, database, port, user, password



def check_table(table_name):
    with psycopg2.connect(host=host, port=port, database=database, user=user, password=password) as conn:
        with conn.cursor() as cur:
            # Check if table exists
            cur.execute(f"select * from information_schema.tables where table_name='{table_name}'")
            if bool(cur.rowcount):
                # If table exists, delete all records
                cur.execute(f"delete from {table_name}")
                

# Establish db connection and create table
def create_table(table_name, columns):
    with psycopg2.connect(host=host, port=port, database=database, user=user, password=password) as conn:
        with conn.cursor() as cur:
            cur.execute(f"""
                create table if not exists {table_name}(
                {','.join(columns)})""")
            

# upload  table
def upload_table_gold(table_name):
    with psycopg2.connect(host=host, port=port, database=database, user=user, password=password) as conn:
        with conn.cursor() as cur:
            cur.execute(f"""
                        COPY {table_name} TO '/var/lib/postgresql/gold/{table_name}.csv' DELIMITER ',' CSV HEADER;
                """)

# upload  table
def upload_table_vehicle(table_name):
    with psycopg2.connect(host=host, port=port, database=database, user=user, password=password) as conn:
        with conn.cursor() as cur:
            cur.execute(f"""
                        COPY {table_name} TO '/var/lib/postgresql/vehicle/{table_name}.csv' DELIMITER ',' CSV HEADER;
                """)
                    

# Insert data into db
def populate_table(table_name, data):
    with psycopg2.connect(host=host, port=port, database=database, user=user, password=password) as conn:
        with conn.cursor() as cur:
            # Prepare the SQL query
            columns = ", ".join(data.columns)
            values_placeholder = ", ".join(["%s"] * len(data.columns))
            query = f"INSERT INTO {table_name} ({columns}) VALUES ({values_placeholder})"
            # Prepare the data
            data_tuples = [tuple(x) for x in data.to_records(index=False)]
            # Execute the query
            cur.executemany(query, data_tuples)
            # Commit the transaction
            conn.commit()


                    