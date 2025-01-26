import pytest


class TestGetV1Account:

    def test_get_v1_account_auth(self, auth_user):
        """
        Тест на получение информации об авторизованном пользователе

        Шаги:
        1. Получаем информацию об авторизованном пользователе
        2. Проверяем ответ
        """
        response = auth_user.helper.get_current_user()

        assert response.status_code == 200, "Ошибка получения информации о пользователе"
        assert response.json()['resource']['login'] == auth_user.user.login, "Логин пользователя не совпадает"


    def test_get_v1_account_no_auth(self, dm_api_facade):
        """
        Тест на получение информации без авторизации

        Шаги:
        1. Пытаемся получить информацию о пользователе без авторизации
        2. Проверяем что получаем ошибку авторизации (401)
        """
        response = dm_api_facade.account_api.get_v1_account()

        assert response.status_code == 401, "Ожидался код ответа 401 (Unauthorized)"