from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Congrats! The lambda deployed!"}


@app.get("/working/{user_input}")
def print_if_working(user_input: int):
    return {"message": f"But did this endpoint work? Look! Your input {user_input}!"}
