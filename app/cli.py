import uvicorn

def main():
    uvicorn.run("app.main:app", host="0.0.0.0", port=8001, reload=True)
