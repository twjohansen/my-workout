# src/main.py
from fastapi import FastAPI

app = FastAPI(title="My Workout App", description="A simple workout tracking application", version="0.1.0")

@app.get("/")
def read_root():
    return {"message": "Hello World from My Workout App!"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "message": "Application is running"}

@app.get("/api/workouts")
def get_workouts():
    # Placeholder for future workout functionality
    return {"workouts": [], "message": "Workout feature coming soon!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)