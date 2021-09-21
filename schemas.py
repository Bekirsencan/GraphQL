from models import Post
from pydantic import BaseModel
from graphene_sqlalchemy import SQLAlchemyObjectType

class PostSchema(BaseModel):
    title: str
    content: str


class PostModel(SQLAlchemyObjectType):
    class Meta:
        model = Post