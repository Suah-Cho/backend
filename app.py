from fastapi import FastAPI
from fastapi.responses import JSONResponse
import requests
import logging
import os

app = FastAPI()
API_MODE = os.getenv('API_MODE')
MODE = os.getenv('MODE')

@app.get('/')
def get_test():
    logging.info("API_MOCDE is " + API_MODE)
    logging.info("MODE is " + MODE)
    if API_MODE:
        logging.info(f"API_MODE: {API_MODE}")
        return JSONResponse(status_code=200, content={"message": "Hello, World! from " + API_MODE})
    else:
        return JSONResponse(status_code=200, content={"message": "Hello, World!"})


@app.post('/')
def event_grid(data: dict):
    print(data)
    response = requests.post('https://hooks.slack.com/services/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', json={"text": str(data)})
    print("response", response)
    return JSONResponse(status_code=200, content={"message": "response"})
