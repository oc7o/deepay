import datetime
import profile
from typing import List, Optional

import strawberry
import strawberry_django_jwt.mutations as jwt_mutations


@strawberry.type
class MeType:
    username: str
    email: str
    isStaff: bool
    isActive: bool
    isSuperuser: bool
    lastName: str
    firstName: str
    dateJoined: datetime.datetime
    lastLogin: datetime.datetime
    profileImage: str

@strawberry.type
class UserQuery:
    @strawberry.field
    def me(self, info) -> Optional[MeType]:
        if info.context.request.user.is_authenticated:
            return MeType(
                username=info.context.request.user.username,
                email=info.context.request.user.email,
                isStaff=info.context.request.user.is_staff,
                isActive=info.context.request.user.is_active,
                isSuperuser=info.context.request.user.is_superuser,
                lastName=info.context.request.user.last_name,
                firstName=info.context.request.user.first_name,
                dateJoined=info.context.request.user.date_joined,
                lastLogin=info.context.request.user.last_login,
                profileImage=info.context.request.build_absolute_uri(info.context.request.user.profile_image.url),
            )
        return None

@strawberry.type
class UserMutations:
    token_auth = jwt_mutations.ObtainJSONWebToken.obtain
    verify_token = jwt_mutations.Verify.verify
    refresh_token = jwt_mutations.Refresh.refresh
    delete_token_cookie = jwt_mutations.DeleteJSONWebTokenCookie.delete_cookie

