# RaceSim

RaceSim is a small distributed full-stack portfolio project with a racing theme. It is designed to demonstrate application architecture, REST service communication, relational and document data modeling, automated testing, containerized development, CI, and transparent AI-assisted engineering.

RaceSim is not a real racing game. Its V1 race is a reproducible scoring simulation for exactly three players, three vehicles, and three tracks.

## Planned V1 architecture

- Next.js, React, and TypeScript frontend
- Node.js, Express, TypeScript, and Prisma Core API
- PostgreSQL owned by the Core API
- Python and FastAPI Simulation API
- MongoDB owned by the Simulation API
- REST communication from browser to frontend to Core API to Simulation API

## Current status: Milestone 1

The development foundation contains a minimal Next.js App Router page, an Express Core API, a FastAPI Simulation API, and Docker Compose services for PostgreSQL and MongoDB. The applications run on the host; only the databases run in containers.

The frontend displays "RaceSim" and "Foundation successfully running." Each backend exposes a `/health` endpoint. There are no application tables, simulation documents, seed data, database connections from the APIs, or service-to-service calls yet. Prisma, race setup, scoring, history, authentication, and CI are not implemented.

## Prerequisites

- Node.js 22.14 or newer with npm (Node 22 is the baseline used for this milestone).
- Python 3.12 or newer with pip and venv.
- Docker Desktop (or Docker Engine with the Compose plugin), running with Linux containers.
- Available local ports listed below.

The commands below use PowerShell. On macOS/Linux, use `cp` instead of `Copy-Item`, `python3` to create the virtual environment, and `.venv/bin/python` instead of `.venv\Scripts\python.exe`. Use `npm.cmd` in PowerShell if its execution policy blocks `npm.ps1`.

## Configure the local environment

From the repository root:

```powershell
Copy-Item .env.example .env
```

Choose local database passwords in `.env` and keep `MONGODB_URL` consistent with the MongoDB credentials and port. URI credentials containing special characters must be percent-encoded. These examples are for local development only. `.env` and its variants are ignored by Git; `.env.example` remains tracked.

Compose reads the root `.env`. Core API scripts load it using Node's environment-file support; the Simulation API launcher loads it with python-dotenv. Existing shell variables take precedence. Both APIs also start with default ports if `.env` is missing. The frontend currently needs no environment variables. `CORE_API_URL` and `MONGODB_URL` are reserved placeholders and are not consumed yet; root `.env` is not automatically loaded by Next.js.

## Install dependencies

From the repository root:

```powershell
npm --prefix frontend ci
npm --prefix core-api ci
cd simulation-api
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
cd ..
```

Node dependencies have committed npm lockfiles. Python direct dependencies are pinned in `requirements.txt`; their transitive dependencies are resolved by pip. No global Python package installation or virtual environment activation is required.

## Start the databases

From the repository root:

```powershell
docker compose config --quiet
docker compose up -d --wait
docker compose ps
```

PostgreSQL 17 and MongoDB 8.0 use official images, named persistent volumes, and health checks. Both published ports bind to `127.0.0.1`. PostgreSQL creates an empty development database and MongoDB creates a local administrative user; no application schema or collections are supplied. MongoDB authentication uses the `admin` database.

Stop the containers while retaining their data:

```powershell
docker compose stop
```

Initialization credentials apply only to new volumes. Editing `.env` does not change passwords already stored in a database. Do not delete volumes to address a configuration issue without considering the data they contain.

## Run the applications

Open three separate terminals from the repository root.

Frontend:

```powershell
cd frontend
npm run dev
```

Core API:

```powershell
cd core-api
npm run dev
```

Simulation API:

```powershell
cd simulation-api
.\.venv\Scripts\python.exe run.py
```

Each development command supports reloading. Stop it with Ctrl+C. These launchers bind to localhost for local development.

| Component | Default local address | Configuration |
| --- | --- | --- |
| Frontend | http://127.0.0.1:3000 | Next.js default; override with `npm run dev -- --port 3002` |
| Core health | http://127.0.0.1:3001/health | `CORE_API_PORT` |
| Simulation health | http://127.0.0.1:8000/health | `SIMULATION_API_PORT` |
| Simulation OpenAPI UI | http://127.0.0.1:8000/docs | FastAPI's built-in documentation |
| PostgreSQL | `127.0.0.1:5433` | `POSTGRES_PORT` (container port remains 5432) |
| MongoDB | `127.0.0.1:27017` | `MONGO_PORT` |

If a port is already occupied, change the relevant setting before starting the service. Keep any URL placeholders aligned with those changes.

## Verify the foundation

With the APIs running, use PowerShell:

```powershell
Invoke-RestMethod http://127.0.0.1:3001/health
Invoke-RestMethod http://127.0.0.1:8000/health
```

Expected JSON responses are `{"service":"core-api","status":"ok"}` and `{"service":"simulation-api","status":"ok"}`. These are liveness checks, not database readiness checks. Open the frontend address to see the foundation page.

Build and static checks, from the repository root:

```powershell
npm --prefix frontend run build
npm --prefix frontend run lint
npm --prefix frontend run typecheck
npm --prefix core-api run build
npm --prefix core-api run typecheck
.\simulation-api\.venv\Scripts\python.exe -m pip check
docker compose config --quiet
```

After building, run `npm start` inside `frontend/` or `core-api/` to run that application's compiled output. No business-logic test suite exists in Milestone 1; the relevant verification is builds, static checks, database health checks, and live HTTP smoke checks.

Tooling limitation: ESLint 9 is retained for compatibility with the React lint plugin bundled by the current Next.js configuration. npm reports its upstream deprecation; ESLint 10 currently fails when loading that plugin's rules.

## Documentation

- [Project specification](docs/project-spec.md)
- [Architecture](docs/architecture.md)
- [AI-assisted development](docs/ai-development.md)
- [Architecture Decision Records](docs/decisions/README.md)

Implementation will proceed in small milestones using `feature/*` branches, with changes promoted through `staging` before `main`.
