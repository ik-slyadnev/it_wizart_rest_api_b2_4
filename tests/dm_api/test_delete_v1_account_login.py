import pytest


class TestDeleteV1AccountLogin:
    def test_delete_v1_account_login(self, auth_user, login_helper):
        """
        Тест проверяет выход пользователя из системы (удаление текущей сессии)
        """
        response = login_helper.logout()
        assert response.status_code == 204, "Неверный код ответа при выходе из системы"

        check_auth = auth_user.helper.get_current_user()
        assert check_auth.status_code == 401, "Пользователь все еще авторизован после выхода"
