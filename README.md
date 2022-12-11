## FastAPI Postgres SQLA template
---

 Project can be started with docker compose:
```sh
make up
```

 Project can be started locally with postgres in separate container:
```sh
# Copy env variables for local deployment
cat .env.local > .env

# Start DB container
make local

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

# Populate with
make fakedata