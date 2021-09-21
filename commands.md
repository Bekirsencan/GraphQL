#### Migration Commands ####

alembic init alembic 

docker-compose run app alembic revision --autogenerate -m "New Migration" # Makemigrations
dcoker-compose run app alembic upgrade head # migrate

### GraphQL Commands ###

mutation CreateNewPost{                                 # Create New Post From GraphQL Page
    createNewPost(title:"title", content="content")     #
    {                                                   #
        ok                                              #
    }                                                   #
}                                                       #


query{                                                  # Get All Query
    allPosts{                                           #
        content                                         #
    }                                                   #
}                                                       #