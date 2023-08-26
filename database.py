import psycopg2

conn = psycopg2.connect(
    dbname="spacetrader_db",
    user = "postgres",
    password = "X#9sP4*7qYvT",
    host = "localhost"  # Assuming PostgreSQL is running locally
)
