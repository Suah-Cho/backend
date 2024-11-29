from fastapi import FastAPI
from fastapi.responses import JSONResponse
import requests
import logging
import os

app = FastAPI()
API_MODE = os.getenv('API_MODE')
MODE = os.getenv('MODE')

@app.get('/api/docs')
def get_docs():
    print("It's api docs for test")

    return JSONResponse(status_code=200, content={"message" : "api docs"})

@app.get('/')
def get_test():
    print("test")
    
    return JSONResponse(status_code=200, content={"message": "Hello, World! from " + "API MODE is " + API_MODE + "MODE is " + MODE})



@app.post('/')
def event_grid(data: dict):
    print(data)
    response = requests.post('https://hooks.slack.com/services/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', json={"text": str(data)})
    print("response", response)
    return JSONResponse(status_code=200, content={"message": "response"})
