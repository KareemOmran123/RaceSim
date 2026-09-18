# RaceSim Architecture

## Milestone 1 implementation

The three applications run as local host processes in `frontend/`, `core-api/`, and `simulation-api/`. Root Docker Compose runs only PostgreSQL 17 and MongoDB 8.0, with named persistent volumes, health checks, and localhost-only published ports. The root `.env.example` documents local configuration; application startup commands are in the README.

The frontend is a static foundation page. Each API exposes `GET /health` for process liveness only. There are no application database schemas, API database connections, or inter-service calls yet. Prisma and the business workflow below remain planned for later milestones.

## Planned system context

RaceSim uses three application layers and two data stores. The locked V1 request path is:

```text
Browser
  ->
Next.js
  ->
Core API (Node.js + Express + TypeScript + Prisma)
  |-> PostgreSQL
  ->
Simulation API (Python + FastAPI)
  |-> MongoDB
```

The browser interacts with the Next.js application. Next.js calls the Core REST API. The Core API coordinates the race workflow and calls the Simulation REST API. There is no direct browser-to-database or frontend-to-Simulation-API access.

## Ownership boundaries

### Next.js frontend

- Renders race setup, results, history, race detail, and safe architecture views.
- Retrieves vehicles and tracks from the Core API rather than hardcoding catalog data.
- Does not connect to PostgreSQL or MongoDB.
- Does not call the Simulation API directly.

### Core API

- Exposes the application's public REST interface.
- Validates and coordinates the three-player race workflow.
- Resolves track voting according to the specified majority and tie rules.
- Owns all PostgreSQL access through Prisma.
- Creates the race before requesting a simulation.
- Calls the Simulation API over REST and stores the returned official results.
- Uses transactions where multiple relational writes must succeed or fail together.

### Simulation API

- Accepts a complete simulation request from the Core API.
- Calculates weighted scores with a small seeded random modifier.
- Produces reproducible results for identical input and seed.
- Owns all MongoDB access.
- Stores a complete nested calculation document before returning the result.

## Data boundaries

PostgreSQL is the authoritative relational store for players, the vehicle and track catalogs, races, participation, votes, and official results. It supports relational constraints, joins, indexes, and transactional consistency.

MongoDB is the detailed simulation record. It stores snapshots of the inputs and all intermediate and final scoring data so a simulation can be inspected without reconstructing historical vehicle or track state.

Services exchange explicit API payloads rather than sharing database access. Database identifiers may correlate records across stores, but neither service reads or writes the other service's database.

## Race sequence

```text
Browser/Next.js       Core API/PostgreSQL       Simulation API/MongoDB
       |                       |                          |
       |-- submit race ------->|                          |
       |                       |-- store race ----------->| PostgreSQL
       |                       |-- simulate ------------->|
       |                       |                          |-- store document -> MongoDB
       |                       |<-- simulation result ----|
       |                       |-- store official result >| PostgreSQL
       |<-- display result ----|                          |
```

The concrete failure and retry policy will be decided during the relevant implementation milestone. V1 should favor clear, observable behavior over distributed-systems complexity.

## Cross-cutting concerns planned for V1

- Environment variables provide configuration; secrets are never committed.
- Swagger/OpenAPI describes REST contracts.
- Automated tests cover meaningful business logic and service boundaries.
- Docker Compose currently provides the two local databases; application containerization remains for a later milestone.
- GitHub Actions runs the agreed verification checks in a later milestone.
- A developer-facing architecture view is safe for display and excludes secrets and sensitive configuration.
