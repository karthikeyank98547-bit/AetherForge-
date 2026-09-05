# AETHERFORGE AI

Autonomous Manufacturing Intelligence Platform — a product-level smart-factory control and intelligence workspace built around a correlated simulator, PostgreSQL, Spring Boot, React/shadcn/ui, optional ML inference, RAG, and an interactive digital twin.

## Stack
- Java 21 + Spring Boot 4.1.1
- PostgreSQL 18
- React 19.2 + TypeScript + Vite
- Tailwind CSS 4 + shadcn/ui source components
- TanStack Query 5
- Three.js / React Three Fiber
- Python FastAPI + scikit-learn ML service
- Docker Compose

## Run with Docker
```bash
docker compose up --build
```
Frontend: http://localhost:3000
Backend: http://localhost:8080
Swagger/OpenAPI: http://localhost:8080/swagger-ui/index.html
ML health: http://localhost:8000/health

## Demo users
- admin@aetherforge.ai / Admin@12345
- engineer@aetherforge.ai / Engineer@12345
- operator@aetherforge.ai / Operator@12345
- viewer@aetherforge.ai / Viewer@12345

These are demo-only credentials for the seeded simulation environment. Change credentials before any real deployment.

## Document support
Knowledge uploads accept text-oriented `.txt`, `.md`, and `.csv` files in the demo. Quality Vision accepts image uploads under 5 MB and labels its deterministic inference as DEMO INFERENCE.

## Golden demo scenario
CNC-07 is seeded with bearing-degradation behavior. Sensor signals correlate across vibration → temperature → health → risk → alert → predictive maintenance → copilot context → autonomous action approval → simulated execution → recovery → audit.

The simulator is clearly labeled DEMO / SIMULATION and never controls physical equipment.
