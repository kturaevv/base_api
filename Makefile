up:
	docker compose --env-file=.env.compose up -d --build
down:
	docker compose down

local:
	docker compose -f docker-compose.local.yml --env-file=.env.local up -d --build
local-down:
	docker compose -f docker-compose.local.yml down

lint:
	pylint --disable=R,C *.py app

format:
	#format code
	black *.py app/*.py

migrate:
	alembic revision --autogenerate -m "$(name)"

migrations:
	alembic upgrade heads

fakedata:
	python -c "from app.crud import CRUD; \
				CRUD()._fake_populate_products_categories();\
				CRUD()._fake_populate_junction_table();\
				"