class TestDeleteV1AccountLoginAll:
    def test_delete_v1_account_login_all(self, auth_user, login_helper):
        """
        Тест проверяет выход пользователя из системы на всех устройствах
        """
        response = login_helper.logout_all()
        assert response.status_code == 204, "Неверный код ответа при выходе из системы на всех устройствах"

        check_auth = auth_user.helper.get_current_user()
        assert check_auth.status_code == 401, "Пользователь все еще авторизован после выхода"
