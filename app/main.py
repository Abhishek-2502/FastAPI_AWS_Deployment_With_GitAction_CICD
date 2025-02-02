from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello3 W3ofgrld from Abhi44shes1s"}

@app.get("/test")
async def test_route():
    return {"message": "this is test"}
