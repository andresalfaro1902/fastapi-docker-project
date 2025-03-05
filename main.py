from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "¡Hola, esta es una API con FastAPI!"}

@app.get("/info")
def get_info():
    return {"info": "Este es un endpoint de información"}
