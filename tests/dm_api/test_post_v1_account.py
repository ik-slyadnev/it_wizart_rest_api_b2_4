class TestPostV1Account:
    def test_post_v1_account(self, account_helper, prepare_user):
        """
        Проверка регистрации нового пользователя
        """
        user = account_helper.register_new_user(prepare_user)

        assert user.login == prepare_user.login
        assert user.email == prepare_user.email
        assert user.password == prepare_user.password
