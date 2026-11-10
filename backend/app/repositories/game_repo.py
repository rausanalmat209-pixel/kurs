from typing import Any


class GameRepository:
    """Repository қабаты:
    1-әрекет: Қолданушы деректерін алады.
    2-әрекет: Ойын нәтижелерін сақтайды.
    """

    def __init__(self) -> None:
        self._users: dict[int, dict[str, Any]] = {
            1: {"id": 1, "username": "student_qadam", "role": "student", "total_points": 120},
            2: {"id": 2, "username": "teacher_qadam", "role": "teacher", "total_points": 350},
        }
        self._results: list[dict[str, Any]] = [
            {"result_id": 1, "user_id": 1, "task_name": "Python негіздері", "score": 120}
        ]

    def get_user_by_id(self, user_id: int) -> dict[str, Any] | None:
        """1-әрекет: Қолданушы деректерін алады."""
        return self._users.get(user_id)

    def get_user_games_count(self, user_id: int) -> int:
        return sum(1 for item in self._results if item["user_id"] == user_id)

    def save_game_result(self, user_id: int, task_name: str, score: int) -> dict[str, Any]:
        """2-әрекет: Ойын нәтижелерін сақтайды."""
        result_id = len(self._results) + 1
        record = {
            "result_id": result_id,
            "user_id": user_id,
            "task_name": task_name,
            "score": score,
        }
        self._results.append(record)
        self._users[user_id]["total_points"] += score
        return record


game_repository = GameRepository()

