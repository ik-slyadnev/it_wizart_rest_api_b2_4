class TestPutV1AccountToken:
    def test_put_v1_account_token(self, dm_api_facade, mailhog_facade, prepare_user, account_helper):
        """
        Тест проверяет активацию аккаунта по токену
        """
        payload = {
            "login": prepare_user.login,
            "email": prepare_user.email,
            "password": prepare_user.password
        }
        response = dm_api_facade.account_api.post_v1_account(json=payload)
        assert response.status_code == 201, "Регистрация пользователя не прошла"

        token = account_helper.get_registration_token(prepare_user.login)
        assert token is not None, f"Токен для пользователя {prepare_user.login} не был получен"

        response = dm_api_facade.account_api.put_v1_account_token(token=token)
        assert response.status_code == 200, "Не удалось активировать аккаунт"
