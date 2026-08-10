from fastapi import FastAPI

app=FastAPI(title="Hemalatha")

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/name")
def read_name():
    return {"name": "Hemalatha"}

@app.get("/batch")
def read_batch():
    return {"batch": "555_B"}
@app.get("/email")
def read_email():
    return {"email": "hemalatha@example.com"}
