class TestPutV1AccountPassword:
    def test_put_v1_account_password(self, account_helper, prepare_user):
        """
        Тест смены пароля пользователя

        """
        user = account_helper.register_new_user(prepare_user)

        auth_response = account_helper.auth_client(
            login=user.login,
            password=user.password
        )
        assert auth_response.status_code == 200, "Не удалось авторизоваться со старым паролем"

        new_password = "NewPassword123!"
        change_response = account_helper.change_password(
            login=user.login,
            email=user.email,
            old_password=user.password,
            new_password=new_password
        )
        assert change_response.status_code == 200, "Не удалось завершить процесс смены пароля"

        new_auth_response = account_helper.auth_client(
            login=user.login,
            password=new_password
        )
        assert new_auth_response.status_code == 200, "Не удалось авторизоваться с новым паролем"
