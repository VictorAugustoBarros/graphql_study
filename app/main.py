import strawberry
import uvicorn
from fastapi import FastAPI
from strawberry.asgi import GraphQL
from app.graphql_query.query import Query
from app.routes.book_routes import book_router


class Api:
    def __init__(self):
        self.port = 6010
        self.app = FastAPI()
        self.schema = strawberry.Schema(query=Query)
        self.graphql_app = GraphQL(self.schema)
        self.create_routes()

    def create_routes(self):
        self.app.add_route("/graphql", self.graphql_app)
        self.app.add_websocket_route("/graphql", self.graphql_app)  # Pesquisar sobre

        self.app.include_router(book_router)

    def run(self):
        uvicorn.run(app=self.app, port=self.port)


api = Api()
