from fastapi import FastAPI
from database_connection import conn 

app = FastAPI()

@app.get("/")
def read_roots():
    return {"message":"hello users"}


@app.post("/signup")
def signup_user(name:str,password:str):
    name = name 
    password = password
    cursor = conn.cursor()
    cursor.execute(
    "INSERT INTO user_pass (name, password) VALUES (%s, %s)", (name, password)
)
    #new_id = cursor.fetchone()[2]
    conn.commit()
    cursor.close()
   
    
    return {"message": "user added"}
    

@app.post("/login")
def user_login(name:str,password:str):
    name = name
    password = password
    cursor = conn.cursor()
    cursor.execute("select * from user_pass where name = %s and password =%s",(name,password))
    result = cursor.fetchone()
    cursor.close()
   
    
    if result :
        return {"message": "login success"}
    else:
        return {"message": "invalid credentials"}