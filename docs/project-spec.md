# RaceSim Project Specification

## Purpose

RaceSim is a small distributed full-stack portfolio project with a racing theme. It is a technical architecture demonstration, not a real racing or driving game.

The project is intended to demonstrate:

- full-stack application architecture;
- relational and document databases;
- REST APIs and service-to-service communication;
- SQL and data modeling;
- Git workflows;
- Docker and Docker Compose;
- automated testing and GitHub Actions; and
- transparent, AI-assisted software development.

The primary audiences are technical interviewers, recruiters, and the developer while learning. The project should support applications for Junior Software Engineer, Technical Support Engineer, and Implementation Engineer roles, while providing foundations for eventual AI Engineer work.

## Locked V1 technology choices

| Area | Technology | Responsibility |
| --- | --- | --- |
| Frontend | Next.js, React, TypeScript | User interface; communicates only with the Core API |
| Core API | Node.js, Express, TypeScript, Prisma | Business workflow; owns PostgreSQL |
| Relational database | PostgreSQL | Catalog, race, participant, vote, and official result data |
| Simulation API | Python, FastAPI | Deterministic scoring simulation; owns MongoDB |
| Document database | MongoDB | Complete simulation input, calculation, and output documents |

All communication uses REST. The browser does not access PostgreSQL or MongoDB directly. The Core API is the only service that accesses PostgreSQL, and the Simulation API is the only service that accesses MongoDB.

## V1 user flow

1. The user enters exactly three player names.
2. Each player selects one of three vehicles. Multiple players may select the same vehicle.
3. Each player votes for one of three tracks.
4. A majority vote selects the track; a 1-1-1 tie is resolved randomly.
5. The Core API creates and stores the race.
6. The Core API sends the race data to the Simulation API over REST.
7. The Simulation API calculates the results from vehicle attributes and a small, controlled random modifier.
8. The Simulation API stores the complete simulation document in MongoDB.
9. The Simulation API returns the result to the Core API.
10. The Core API stores the official race result in PostgreSQL.
11. The frontend displays the result and adds the race to persistent history.
12. A user can open a previous race in a race detail view.

## Vehicles and tracks

V1 contains exactly three vehicles. Each vehicle has:

- speed;
- acceleration;
- handling;
- braking;
- traction; and
- weight.

V1 also contains exactly three tracks. Vehicles and tracks come from PostgreSQL through the Core API and must not be hardcoded in the frontend.

## Simulation behavior

The race is a scoring simulation, not a physics simulation. Conceptually, weighted vehicle attributes plus a small seeded random modifier produce a final performance score.

The same input and seed must reproduce the same result. A simulation response includes:

- the full finishing order;
- performance scores;
- optionally generated finish times;
- the winner;
- a simple winner explanation; and
- the random seed.

## Data responsibilities

### PostgreSQL

Expected relational entities are:

- `players`;
- `vehicles`;
- `tracks`;
- `races`;
- `race_participants`;
- `track_votes`; and
- `race_results`.

The model should demonstrate primary and foreign keys, one-to-many relationships, appropriate many-to-many relationships, constraints, joins, justified indexes, and useful transactions. Prisma is the Core API's data-access tool, but the schema must remain understandable and queryable with manual SQL.

### MongoDB

Each complete simulation document includes:

- race ID and random seed;
- generated timestamp;
- track snapshot;
- participant and vehicle-stat snapshots;
- scoring inputs and base scores;
- random modifiers and final scores;
- finishing positions; and
- winner explanation.

MongoDB is used intentionally to demonstrate nested, document-oriented data and to retain the complete simulation calculation record.

## V1 deliverables

- race setup for exactly three players;
- deterministic scoring simulation;
- persistent race history;
- race detail page;
- a safe developer/architecture view that does not expose secrets;
- Swagger/OpenAPI documentation;
- Docker and Docker Compose support;
- automated tests;
- GitHub Actions CI; and
- architecture documentation.

## Out of scope for V1

- authentication or user accounts;
- real-time multiplayer or WebSockets;
- leaderboards;
- actual driving, physics, 3D graphics, or advanced animation;
- Redis, Kafka, RabbitMQ, or other message brokers;
- Kubernetes;
- track, vehicle, or admin editors; and
- production cloud infrastructure.

V1 must remain intentionally small and finishable.

## Git workflow

Long-lived branches are `main` and `staging`; implementation work uses `feature/*` branches. The intended promotion path is:

```text
feature/* -> pull request -> staging -> testing -> pull request -> main
```

