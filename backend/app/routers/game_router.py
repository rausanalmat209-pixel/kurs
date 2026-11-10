from fastapi import APIRouter
from app.schemas.dto import GameResultResponse, GameSubmitRequest, UserProfileResponse
from app.services.game_service import game_service

router = APIRouter(prefix="/api/v1", tags=["Қадам ойыны және профиль"])


@router.post("/game/submit", response_model=GameResultResponse)
async def submit_game(payload: GameSubmitRequest) -> GameResultResponse:
    """Router қабаты (1-әрекет): Ойын туралы сұранысты қабылдайды (SQL жазылмайды)."""
    return game_service.process_game_submission(payload)


@router.get("/users/{user_id}/profile", response_model=UserProfileResponse)
async def open_user_profile(user_id: int) -> UserProfileResponse:
    """Router қабаты (2-әрекет): Қолданушы профилін ашады (SQL жазылмайды)."""
    return game_service.get_user_profile(user_id)

