# Dockerized GraphQL

Simple Post API for using GraphQL with Docker.

## Setup

* Create venv
```
py -m venv venv
```
* Activate venv
```
venv\Scripts\activate
```
* Install requirements.txt
```
pip install -r requirements.txt
```

## Migration Commands

* Alembic init
```
alembic init alembic
```
* MakeMigrations (alembic)
```
docker-compose run app alembic revision --autogenerate -m "New Migration" 
```
* Migrate (alembic)
```
docker-compose run app alembic upgrade head
```
## GraphQL Commands

* Create New Post From GraphQl Page
```
mutation CreateNewPost{                                 
    createNewPost(title:"title", content="content")     
    {                                                   
        ok                                              
    }                                                   
}      
```
* Get All Queries
```
query{                                                  
    allPosts{                                           
        content                                         
    }                                                  
}        
```

## Libraries and tools 🛠
* [GraphQL](https://graphql.org)
* [Graphene](https://graphene-python.org)
* [FastAPI](https://fastapi.tiangolo.com)
* [PostgreSQL](https://www.postgresql.org)
* [Psycopg2](https://pypi.org/project/psycopg2/)
* [Uvicorn](https://www.uvicorn.org)
* [Python Dotenv](https://pypi.org/project/python-dotenv/)
* [Docker](https://www.docker.com)



