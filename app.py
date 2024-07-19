from fastapi import FastAPI
from fastapi.responses import JSONResponse
import requests
app = FastAPI()

@app.get('/')
def get_test():
    return JSONResponse(status_code=200, content={"message": "Hello, World!"})


@app.post('/')
def event_grid(data: dict):
    print(data)
    response = requests.post('https://hooks.slack.com/services/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', json={"text": str(data)})
    print("response", response)
    return JSONResponse(status_code=200, content={"message": "response"})
