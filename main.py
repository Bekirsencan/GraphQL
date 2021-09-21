from schemas import PostSchema, PostModel
import graphene
import models
from fastapi import FastAPI
from starlette.graphql import GraphQLApp
from db_conf import db_session

db = db_session.session_factory()

app = FastAPI()

class Query(graphene.ObjectType):
    all_post = graphene.List(PostModel)

    def resolve_all_posts(self, info):
        query = PostModel.get_query(info)
        return query.all() 
    
class CreateNewPost(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        content = graphene.String(required=True)
        
    ok = graphene.Boolean()
    
    @staticmethod
    def mutate(root, info, title, content):
        post = PostSchema(title=title, content=content)
        db_post = models.Post(title=post.title, content=post.content)
        db.add(db_post)
        db.commit()
        db.refresh(db_post)
        ok = True
        return CreateNewPost(ok=ok)
        
class PostMutations(graphene.ObjectType):
    create_new_post = CreateNewPost.Field()

app.add_route("/graphql", GraphQLApp(schema=graphene.Schema(mutation=PostMutations, query=Query)))