# OmniCalc Pro (Delivered ZIP)

This is a ready-to-run prototype of **OmniCalc Pro** (FastAPI backend + React frontend).
Run locally with Docker Compose.

## Quickstart (Docker)
```bash
# extract zip and cd into folder
docker-compose up --build
```
- Backend: http://localhost:8000
- Frontend: http://localhost:5173

## Run tests
Backend:
```bash
cd backend
pytest -q
```

Frontend:
```bash
cd frontend
npm ci
npm run dev
```

## Notes
- No secrets are included.
- This prototype includes 10 calculator modules (see backend/app/calculators).
- For production hardening, follow README in repo.
