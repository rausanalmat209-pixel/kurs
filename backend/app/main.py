from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.core.exceptions import register_exception_handlers
from app.routers.game_router import router as game_router

app = FastAPI(
    title="Қадам (Проект-тест) API",
    version="0.1.0",
    description="Оқу процесін, тестілеуді және жергілікті LLM мүмкіндіктерін біріктіретін платформа",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

register_exception_handlers(app)
app.include_router(game_router)


@app.get("/health", tags=["Жүйе"])
async def health_check() -> dict[str, str]:
    return {"status": "ok", "environment": settings.ENVIRONMENT}

