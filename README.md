# Boiler

## Features

- **FastAPI** with Python 3.8
- **Vue.js**
- Postgres
- SqlAlchemy with Alembic for migrations
- Docker compose for easier development


## Development

The only dependencies for this project should be docker and docker-compose.

### Quick Start

Starting the project with hot-reloading enabled
(the first time it will take a while):

```bash
docker-compose up -- build -d
```

To run the alembic migrations (for the users table):

```bash
docker-compose exec web alembic upgrade head
```

And navigate to http://localhost:8000



**Docs**
http://localhost:8000/docs

### Rebuilding containers:

```
docker-compose build
```

### Restarting containers:

```
docker-compose restart
```

### Bringing containers down:

```
docker-compose down
```

### Frontend Development

Alternatively to running inside docker, it can sometimes be easier
to use npm directly for quicker reloading. To run using npm:

```bash
cd frontend
npm i
npm run dev
```


## Migrations

Migrations are run using alembic. To run all migrations:


To create a new migration:

```bash
docker-compose exec web alembic revision -m "create users table"
```

```bash
docker-compose exec web alembic upgrade head
```

And fill in `upgrade` and `downgrade` methods. For more information see
[Alembic's official documentation](https://alembic.sqlalchemy.org/en/latest/tutorial.html#create-a-migration-script).


## Project Layout


## Quasar vue3
