# main.py

from fastapi import FastAPI
from typing import Union
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
  
@app.get("/login-sns")
async def loginSns(code: Union[str, None] = None):
  if code and code.strip():
    return {"url": "smartedu://mylogin?code=" + code, "type": "SUCCESS"}
  return {"url": "smartedu://mylogin", "type": "ERROR", "code": "CODE_IS_EMPTY"}
