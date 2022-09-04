import strawberry


@strawberry.type
class Book:
    id: int
    title: str
    author: str
