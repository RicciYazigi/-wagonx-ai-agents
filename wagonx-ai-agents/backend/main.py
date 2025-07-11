from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="WagonX AI Agents API",
    description="AI Agent Platform for Content Creation",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {
        "message": "🚀 WagonX AI Agents API",
        "version": "1.0.0",
        "status": "running"
    }

@app.get("/health")
async def health():
    return {"status": "healthy"}

@app.get("/agents")
async def list_agents():
    return {
        "agents": [
            {"name": "CopywriterAgent", "status": "active"},
            {"name": "AssemblyAgent", "status": "active"},
            {"name": "SEOAgent", "status": "active"}
        ]
    }
