from fastapi import FastAPI
from uvicorn import Server, Config

# Initializing fastapi
app = FastAPI(__name__ = "Rivora")

# Routes
@app.get('/health')
def health_check():
    return { "Status": "Ok" }

# Remove this for production -- Only useful for dev
# Only start the server from main.py   
if __name__ == "__main__":
    config: Config = Config( # Just mentioning type -- not needed 
                "app.main:app",
                port=5000, 
                host="127.0.0.1", 
                log_level="info",
                # workers=4,
                reload=True
            )
    server: Server = Server(config)
    server.run()
