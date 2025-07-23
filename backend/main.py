import uvicorn
from fastapi import FastAPI, Request, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import os
from fastapi.templating import Jinja2Templates

from database import engine
from routers import users, products, carts, orders # Import your routers

# Import your models to create tables if they don't exist
# from models import Base # Example
# Base.metadata.create_all(bind=engine)

app = FastAPI(title="Project Build A Modern", version="0.1.0", description="A modern e-commerce platform")

# CORS Configuration
origins = ["*"]  # Change to your allowed origins in production
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

# Router Registration
app.include_router(users.router)
app.include_router(products.router)
app.include_router(carts.router)
app.include_router(orders.router)

# Health Check
@app.get('/health')
def health_check():
    return {"status": "ok"}

# Templates for frontend rendering
templates = Jinja2Templates(directory="templates")

# Serve static files from 'static' directory
if os.path.exists("static"):
    app.mount("/static", StaticFiles(directory="static"), name="static")

    @app.get("/{path:path}")
    async def serve_frontend(request: Request, path: str):
        if path.startswith("api"):
            return None
        html_file = os.path.join("static", path)
        if os.path.isfile(html_file):
            return FileResponse(html_file)
        return templates.TemplateResponse("index.html", {"request": request})

# Example Exception Handling
@app.exception_handler(HTTPException)
def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.detail})

# Start the application (for development)
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
