from fastapi import FastAPI
from dotenv import load_dotenv

from agents.planner import PlannerAgent
from agents.executor import ExecutorAgent
from agents.verifier import VerifierAgent

load_dotenv()

app = FastAPI(title="AI Ops Assistant")

planner = PlannerAgent()
executor = ExecutorAgent()
verifier = VerifierAgent()


@app.post("/run")
def run_task(task: dict):
    plan = planner.create_plan(task.get("task"))
    execution = executor.execute(plan)
    verified = verifier.verify(execution)

    return {
        "plan": plan,
        "execution": execution,
        "verification": verified
    }
