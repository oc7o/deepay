import strawberry
from strawberry_django_jwt.middleware import JSONWebTokenMiddleware

from octoincore.dashboard.schema import DashboardQuery
from octoincore.users.schema import UserMutation

@strawberry.type
class Query(DashboardQuery):
    pass

@strawberry.type
class Mutation(UserMutation):
    pass

schema = strawberry.Schema(query=Query, mutation=Mutation, extensions=[JSONWebTokenMiddleware])