from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")

def root():
    return "Hello World"

@app.get("/health")
def health_check():
    return "ok"

@app.get("/calculate")
def calculate(a: int, b: int, operation: str):
    if operation == "add":
        return {"result": a + b}
    elif operation == "subtract":
        return {"result": a - b}
    elif operation == "multiply":
        return {"result": a * b}
    elif operation == "divide":
        if b == 0:
            raise HTTPException(status_code=400, detail="Division by zero is not allowed")
        return {"result": a / b}
    else:
        raise HTTPException(status_code=400, detail="Unsupported operation")