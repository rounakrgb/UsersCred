import psycopg2 

conn = psycopg2.connect(
    
    database = "postgres",
    user = "postgres",
    password = "pass123",
    host = "localhost",
    port = 5432
)

print("connected successfully")





