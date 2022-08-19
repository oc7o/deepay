import strawberry
from gqlauth.user.queries import UserQueries
from strawberry.tools import merge_types
from strawberry_django_jwt.middleware import JSONWebTokenMiddleware

from octoincore.dashboard.schema import DashboardQuery
from octoincore.inventory.schema import InventoryQuery
from octoincore.users.schema import UserMutations

Query = merge_types("RootQuery", (UserQueries, DashboardQuery, InventoryQuery,))
Mutation = merge_types("RootMutation", (UserMutations,))

schema = strawberry.Schema(
    query=Query,
    mutation=Mutation,
    extensions=[
        JSONWebTokenMiddleware,
    ],
)

