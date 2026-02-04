from fastapi import FastAPI

app = FastAPI(title="AI Ops Assistant")

@app.get("/")
def root():
    return {"status": "AI Ops Assistant running"}
