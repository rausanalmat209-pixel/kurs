# Қадам (Проект-тест) — FastAPI + Next.js

Бұл жоба — оқу процесін, ойын/тестілеуді және жергілікті LLM (Ollama) мүмкіндіктерін біріктіретін заманауи веб-қосымша.

## Іске қосу

### 1. Қоршаған орта айнымалыларын баптау
Жоба түбіріндегі `.env` файлында айнымалылар орнатылғанын тексеріңіз (`.env.example` үлгісі бойынша).

### 2. Дерекқор мен инфрақұрылымды қосу (Docker Compose)
```bash
docker compose up -d
```

### 3. Backend (FastAPI) іске қосу
```bash
cd backend
python -m venv .venv
# Windows PowerShell:
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
```
Сервер қосылған соң интерактивті құжаттама (Swagger UI): http://localhost:8000/docs

### 4. Тесттерді тексеру (pytest)
```bash
cd backend
pytest
```
