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

## Current status

The repository is in its initial documentation and planning stage. No application frameworks, dependencies, databases, containers, or functional features have been initialized yet.

## Documentation

- [Project specification](docs/project-spec.md)
- [Architecture](docs/architecture.md)
- [AI-assisted development](docs/ai-development.md)
- [Architecture Decision Records](docs/decisions/README.md)

Implementation will proceed in small milestones using `feature/*` branches, with changes promoted through `staging` before `main`.
