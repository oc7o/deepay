import strawberry
from gqlauth.user import arg_mutations
import strawberry_django_jwt.mutations as jwt_mutations


@strawberry.type
class UserMutations:
    register = arg_mutations.Register.field
    verify_account = arg_mutations.VerifyAccount.field
    update_account = arg_mutations.UpdateAccount.field
    resend_activation_email = arg_mutations.ResendActivationEmail.field
    archive_account = arg_mutations.ArchiveAccount.field
    delete_account = arg_mutations.DeleteAccount.field
    password_change = arg_mutations.PasswordChange.field
    send_password_reset_email = arg_mutations.SendPasswordResetEmail.field
    password_reset = arg_mutations.PasswordReset.field
    password_set = arg_mutations.PasswordSet.field
    verify_secondary_email = arg_mutations.VerifySecondaryEmail.field
    swap_emails = arg_mutations.SwapEmails.field
    remove_secondary_email = arg_mutations.RemoveSecondaryEmail.field
    send_secondary_email_activation = arg_mutations.SendSecondaryEmailActivation.field

    token_auth = arg_mutations.ObtainJSONWebToken.field # login mutation
    verify_token = arg_mutations.VerifyToken.field
    refresh_token = arg_mutations.RefreshToken.field
    revoke_token = arg_mutations.RevokeToken.field

# @strawberry.type
# class UserMutations:
#     token_auth = jwt_mutations.ObtainJSONWebToken.obtain
#     verify_token = jwt_mutations.Verify.verify
#     refresh_token = jwt_mutations.Refresh.refresh
#     delete_token_cookie = jwt_mutations.DeleteJSONWebTokenCookie.delete_cookie

