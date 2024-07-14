from fastapi import FastAPI
from workout_api.routers import api_router
from fastapi_pagination import paginate

app = FastAPI(title='WorkoutApi')
app.include_router(api_router)
add_pagination(app)
