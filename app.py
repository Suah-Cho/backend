from fastapi import FastAPI
from fastapi.responses import JSONResponse
import requests
import os

app = FastAPI()

@app.get('/')
def get_test():
    return JSONResponse(status_code=200, content={"message": "Hello, World!"})

slack_url = os.environ.get('TEST_SLAK_URL')
print(slack_url)

@app.post('/')
def event_grid(data: dict):
    print(data)
    response = requests.post(url=slack_url, json={"text": str(data)})
    print("response", response)
    return JSONResponse(status_code=200, content={"message": "response"})
