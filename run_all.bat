@echo off
echo ============================================================
echo   NEXUS AI-BASED SCREENING SUPPORT PLATFORM
echo   Launching Frontend, Backend, and AI/ML Service
echo ============================================================

REM 1. Start AI/ML Service (Flask on Port 5000)
echo [1/3] Starting Nexus AI/ML Service (Port 5000)...
start "Nexus ML Service (Flask :5000)" cmd /k "cd /d %~dp0ml-service && .\venv\Scripts\python.exe app.py"

REM 2. Start Spring Boot Backend (Port 8081)
echo [2/3] Starting Nexus Backend (Spring Boot :8081)...
start "Nexus Backend (Spring Boot :8081)" cmd /k "cd /d %~dp0backend && .\mvnw.cmd spring-boot:run"

REM 3. Start React Frontend (Vite :5173)
echo [3/3] Starting Nexus Frontend (React + Vite :5173)...
start "Nexus Frontend (Vite :5173)" cmd /k "cd /d %~dp0frontend && npm run dev"

echo ============================================================
echo   All 3 services have been launched in separate windows!
echo   - AI/ML Service:   http://localhost:5000
echo   - Backend Service: http://localhost:8081
echo   - Frontend UI:     http://localhost:5173
echo ============================================================
pause
