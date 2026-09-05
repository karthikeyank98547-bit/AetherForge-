# AetherForge Architecture

Browser → React/Vite/shadcn → typed API client → Spring Boot REST/SSE → repositories/services → PostgreSQL.

The simulator produces correlated signals for the golden CNC-07 scenario. Autonomous actions require ENGINEER/ADMIN authorization and only execute simulated maintenance workflows. The ML service is a replaceable FastAPI/scikit-learn adapter. The Copilot has a tool-backed deterministic mode that remains usable without an LLM credential.
