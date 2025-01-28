class TestPutV1AccountEmail:
    def test_put_v1_account_email(self, account_helper, dm_api_facade, login_helper, prepare_user):
        """
        Проверка смены email пользователя
        """
        user = account_helper.register_new_user(prepare_user)

        response = login_helper.login(user.login, user.password)
        assert response.status_code == 200

        new_email = f"new_{user.login}@example.com"
        response = dm_api_facade.account_api.put_v1_account_email(
            json={
                "login": user.login,
                "email": new_email,
                "password": user.password
            }
        )
        assert response.status_code == 200

        response = login_helper.login(user.login, user.password)
        assert response.status_code == 403

        email_change_token = account_helper.get_registration_token(user.login)
        account_helper.activate_account(email_change_token)

        response = login_helper.login(user.login, user.password)
        assert response.status_code == 200
