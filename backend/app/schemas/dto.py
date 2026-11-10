from pydantic import BaseModel, Field


class GameSubmitRequest(BaseModel):
    """Schema қабаты (1-әрекет): Қолданушы мен ойын мәліметтерін тексереді."""

    user_id: int = Field(..., ge=1, description="Қолданушы ID-і")
    task_name: str = Field(..., min_length=2, max_length=150, description="Тапсырма атауы")
    correct_answers: int = Field(..., ge=0, le=100, description="Дұрыс жауаптар саны")
    total_questions: int = Field(..., ge=1, le=100, description="Барлық сұрақтар саны")


class UserProfileResponse(BaseModel):
    """Schema қабаты (2-әрекет): Профиль жауап форматын анықтайды."""

    id: int
    username: str
    role: str
    total_points: int
    games_played: int


class GameResultResponse(BaseModel):
    """Schema қабаты (2-әрекет): Ойын нәтижесінің жауап форматын анықтайды."""

    result_id: int
    user_id: int
    task_name: str
    score: int
    rank_label: str
    total_points: int

