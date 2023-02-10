"""Token generator for user activation.""" ""
from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six


class TokenGenerator(PasswordResetTokenGenerator):
    """Token generator for user activation."""

    def _make_hash_value(self, user, timestamp):
        """Make hash value for user activation."""
        return (
            six.text_type(user.pk)
            + six.text_type(timestamp)
            + six.text_type(user.is_active)
        )


account_activation_token = TokenGenerator()
