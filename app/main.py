from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World from Abhishek1s"}

@app.get("/test")
async def test_route():
    return {"message": "this is test"}
