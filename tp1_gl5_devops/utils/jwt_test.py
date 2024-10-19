from tp1_gl5_devops.models.user import User
from tp1_gl5_devops.utils.jwt import createToken


class JwtTest:
    def test_createToken(self) -> None:
        token = createToken(
            User(
                id=1,
                email='user@qa.team',
                password='test_password',  # noqa: S106
                firstName='dev',
                lastName='ops',
            ),
        )
        assert token != ''
        assert len(token) > 3
