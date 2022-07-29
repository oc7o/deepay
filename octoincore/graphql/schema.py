import strawberry
from strawberry_django_jwt.middleware import JSONWebTokenMiddleware
from strawberry.tools import merge_types

from octoincore.dashboard.schema import DashboardQuery
from octoincore.users.schema import UserQueries, UserMutations


Query = merge_types("RootQuery", (UserQueries, DashboardQuery,))
Mutation = merge_types("RootMutation", (UserMutations,))


schema = strawberry.Schema(query=Query, mutation=Mutation, extensions=[JSONWebTokenMiddleware])