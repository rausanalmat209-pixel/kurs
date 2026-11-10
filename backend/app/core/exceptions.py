from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse


class DomainError(Exception):
    """Service қабаты шығаратын базалық бизнес-логика қатесі."""

    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


class UserNotFoundError(DomainError):
    """Қолданушы табылмаған кезде шығатын қате."""
    pass


class InvalidTaskScoreError(DomainError):
    """Ойын ұпайы немесе тапсырма дерегі қате болғанда шығатын қате."""
    pass


def register_exception_handlers(app: FastAPI) -> None:
    """Қате-HTTP қабаты: қате сұранысты анықтайды және қате туралы хабарлама береді."""

    @app.exception_handler(UserNotFoundError)
    async def user_not_found_handler(_request: Request, exc: UserNotFoundError) -> JSONResponse:
        return JSONResponse(
            status_code=404,
            content={"detail": exc.message},
        )

    @app.exception_handler(InvalidTaskScoreError)
    async def invalid_score_handler(_request: Request, exc: InvalidTaskScoreError) -> JSONResponse:
        return JSONResponse(
            status_code=400,
            content={"detail": exc.message},
        )

