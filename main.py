from fastapi import FastAPI
from fastapi.responses import FileResponse
from agent import run_agent

app = FastAPI()

@app.get("/")
def home():
    return {"message": "FireReach Agent Running"}


# UI PAGE
@app.get("/ui")
def ui():
    return FileResponse("index.html")


# AGENT API
@app.get("/run-agent")
def execute(icp: str, company: str, email: str):
    result = run_agent(icp, company, email)
    return result
