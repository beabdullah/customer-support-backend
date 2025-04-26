from fastapi import FastAPI
from app.routers import auth, ticket

app = FastAPI(title="Customer Support Backend")

# Include routers
app.include_router(auth.router)
app.include_router(ticket.router)

@app.get("/")
def read_root():
    return {"message": "Customer Support Backend"}