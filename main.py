from fastapi import FastAPI
from routes.auth import router as auth_router
from routes.uploads import router as uploads_router

app = FastAPI()

# Includes the auth_router under the /auth prefix
app.include_router(auth_router, prefix="/auth")

# Includes the uploads_router under the /uploads prefix
app.include_router(uploads_router, prefix="/uploads")