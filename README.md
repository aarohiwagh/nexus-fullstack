# 🌟 Nexus Screening Platform — Full Stack System (Unified)

**Project:** AI-Based Autism and Learning Disability Screening Support Platform  
**ADYPSOE, Savitribai Phule Pune University (SPPU), AY 2026-27**

---

## 👥 Engineering Team & Service Breakdown

| Service | Technology | Lead Developer | Port | Description |
|---|---|---|---|---|
| **`frontend/`** | React + Vite + Tailwind CSS | Supriya Unde | `:5173` | Interactive screening UI, canvas drawing/writing, child profiles, reports. |
| **`backend/`** | Java 17 + Spring Boot + JPA | Shivam Ubarhande | `:8081` | REST APIs, authentication, user & child profile management, audit log. |
| **`ml-service/`** | Python 3.13 + Flask + Scikit-Learn | Aarohi Wagh | `:5000` | Stroke kinematics extraction, Random Forest models, late fusion & SHAP. |

---

## 🚀 How to Run the Entire Combined System

### Quick Start (Windows)
Double-click:
```bat
run_all.bat
```
This automatically starts all 3 services in separate terminal windows.

### Manual Start:

1. **Start the AI/ML Service:**
   ```bash
   cd ml-service
   .\venv\Scripts\Activate.ps1
   python app.py
   ```
   *Runs at `http://localhost:5000`*

2. **Start the Spring Boot Backend:**
   ```bash
   cd backend
   .\mvnw.cmd spring-boot:run
   ```
   *Runs at `http://localhost:8081`*

3. **Start the React Frontend:**
   ```bash
   cd frontend
   npm install
   npm run dev
   ```
   *Runs at `http://localhost:5173`*

---

## 📡 End-to-End Request Flow

```
1. Child draws / solves tasks on HTML5 Canvas (React Frontend :5173)
        ⬇ (POST /results)
2. Spring Boot Backend stores session data (:8081)
        ⬇ (POST /api/analysis)
3. Flask AI/ML Service extracts kinematics and predicts risk (:5000)
        ⬇ (Returns evidence level, SHAP values, uncertainty)
4. Clinician views full developmental profile & signs off in Frontend!
```
