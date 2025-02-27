from django.contrib.auth.tokens import PasswordResetTokenGenerator
from six import text_type


class AccountsVerifyTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return text_type(user.id) + text_type(timestamp)


accounts_verify_token = AccountsVerifyTokenGenerator()
