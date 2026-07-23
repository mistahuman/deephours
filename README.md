# deephours

Working-hours tracker: log what you worked on and keep the week in order.

## Stack

FastAPI · MongoDB · Svelte · Skeleton · Docker Compose

## Run

```bash
cp env.sample .env
make install         # virtualenv + dependencies
make dev             # backend
make ui              # frontend, in a second shell
```

Or the whole stack at once:

```bash
make run             # -> http://localhost:8080
make stop
```

## Configuration

| Var | What |
|---|---|
| `MONGO_URI` | MongoDB connection string (local or Atlas) |
| `MONGO_DB` | Database name |
