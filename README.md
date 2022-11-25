## FastAPI Postgres SQLA template
---

 Project can be started with docker compose:
```sh
# Copy env variables for compose
cat .env.compose > .env
docker compose up -d --build
```

 Project can be started locally with postgres in separate container:
```sh
# Copy env variables for local deployment
cat .env.local > .env

# Start DB container
docker compose -f docker-compose.local.yml up -d 

# Init project env
# With conda
conda env create --name api --file=environment.yml
conda activate api

# With pip
python -m venv env
source env/scripts/activate
pip install -r requirements.txt

# Start app
uvicorn main:app --reload

# Test with 
pytest
