from tp1_gl5_devops.services.users import createUser, findAll, findOneByEmail


class TestUserService:
    def test_create_user(self) -> None:
        user = createUser('user@qa.team', 'password', 'dev', 'ops')
        all_users = findAll()
        assert len(all_users) > 0
        assert all_users[0].email == user.email

    def test_findOneByEmail(self) -> None:
        user = findOneByEmail('user@qa.team')
        assert user is not None
        assert user.email == 'user@qa.team'
