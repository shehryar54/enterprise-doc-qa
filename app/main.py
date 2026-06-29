from fastapi import FastAPI

app = FastAPI(title="Enterprise Doc QA", version="1.0.0")

@app.get("/")
def root():
    return {"status": "running", "message": "Enterprise Doc QA API is live"}

@app.get("/health")
def health():
    return {"status": "ok"}