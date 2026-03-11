from fastapi import FastAPI
from agent import run_agent

app = FastAPI()

@app.get("/")
def home():
    return {"message": "FireReach Agent Running"}


@app.get("/run-agent")
def execute(icp: str, company: str, email: str):

    result = run_agent(icp, company, email)

    return result