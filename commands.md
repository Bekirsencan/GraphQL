#### Migration Commands ####

alembic init alembic 

docker-compose run app alembic revision --autogenerate -m "New Migration" # Makemigrations
dcoker-compose run app alembic upgrade head # migrate