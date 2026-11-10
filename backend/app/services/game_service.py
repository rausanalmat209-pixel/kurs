from app.core.exceptions import InvalidTaskScoreError, UserNotFoundError
from app.repositories.game_repo import GameRepository, game_repository
from app.schemas.dto import GameResultResponse, GameSubmitRequest, UserProfileResponse


class GameService:
    """Service қабаты (ереже бойынша мұнда HTTPException қолданылмайды):
    1-әрекет: Ойын логикасын басқарады.
    2-әрекет: Тапсырмаларды өңдейді.
    """

    def __init__(self, repo: GameRepository) -> None:
        self.repo = repo

    def get_user_profile(self, user_id: int) -> UserProfileResponse:
        user = self.repo.get_user_by_id(user_id)
        if not user:
            raise UserNotFoundError(f"ID={user_id} қолданушысы табылмады.")

        games_played = self.repo.get_user_games_count(user_id)
        return UserProfileResponse(
            id=user["id"],
            username=user["username"],
            role=user["role"],
            total_points=user["total_points"],
            games_played=games_played,
        )

    def process_game_submission(self, payload: GameSubmitRequest) -> GameResultResponse:
        """1-әрекет: Ойын логикасын басқарады және 2-әрекет: Тапсырмаларды өңдейді."""
        user = self.repo.get_user_by_id(payload.user_id)
        if not user:
            raise UserNotFoundError(f"ID={payload.user_id} қолданушысы табылмады.")

        if payload.correct_answers > payload.total_questions:
            raise InvalidTaskScoreError(
                "Дұрыс жауаптар саны жалпы сұрақтар санынан көп болуы мүмкін емес."
            )

        score = int((payload.correct_answers / payload.total_questions) * 100)
        if score >= 90:
            rank_label = "Үздік (Алтын қадам)"
        elif score >= 70:
            rank_label = "Жақсы (Күміс қадам)"
        else:
            rank_label = "Талпыныс (Қола қадам)"

        saved = self.repo.save_game_result(
            user_id=payload.user_id,
            task_name=payload.task_name,
            score=score,
        )

        return GameResultResponse(
            result_id=saved["result_id"],
            user_id=payload.user_id,
            task_name=payload.task_name,
            score=score,
            rank_label=rank_label,
            total_points=user["total_points"],
        )


game_service = GameService(repo=game_repository)

