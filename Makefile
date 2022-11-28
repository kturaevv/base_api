up:
	docker compose --env-file=.env.compose up -d --build
down:
	docekr compose down

local:
	docker compose -f docker-compose.local.yml --env-file=.env.local up -d --build
local-down:
	docker compose -f docker-compose.local.yml down 
