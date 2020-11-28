import pandas as pd
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/test")
async def test():
    dictlist = [{"col1": 1, "col2": 2}, {"col1": 2, "col2": 3}]

    df = pd.DataFrame(dictlist)
    return {"message": df.to_dict(orient="list")}
