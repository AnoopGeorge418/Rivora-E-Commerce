from fastapi import FastAPI

# Initilizing FastApi
app = FastAPI()

# routes
@app.get("/")
def health():
    return { "Status": "Success" }

# Starts backend only if app is initialized
if __name__ == "__main__":
    ...
