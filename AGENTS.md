# RaceSim Agent Instructions

RaceSim is a small, finishable portfolio project and architecture demonstration. Before making architectural changes, read `README.md` and the documents in `docs/`, including relevant Architecture Decision Records.

- Preserve the locked V1 architecture: Next.js/React/TypeScript frontend, Node.js/Express/TypeScript/Prisma Core API owning PostgreSQL, and Python/FastAPI Simulation API owning MongoDB.
- Preserve the communication path: Browser -> Next.js -> Core API -> Simulation API. The frontend must never access either database directly, and each API must access only the database it owns.
- Implement only the requested milestone. Do not build future milestones early.
- Prefer direct, simple solutions and avoid unnecessary abstractions or technologies.
- Keep V1 exclusions out of scope, including authentication, WebSockets, leaderboards, message brokers, Kubernetes, editors, and production cloud infrastructure.
- Never commit secrets. Use environment variables for configuration and provide safe example values separately when needed.
- Add tests for meaningful business logic, especially deterministic simulation behavior, voting rules, persistence boundaries, and transactions.
- Record material architecture choices as ADRs in `docs/decisions/` when requested or warranted.
- After each task, summarize files changed, commands run, tests run, architectural decisions, and remaining issues.

