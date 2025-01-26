from common.rest_client import RestClient

class LoginApi(RestClient):
    def post_v1_account_login(self, login: str, password: str, remember_me: bool = True):
        """
        Авторизация пользователя

        :param login: Логин пользователя
        :param password: Пароль пользователя
        :param remember_me: Флаг запоминания сессии
        :return: Response
        """
        payload = {
            "login": login,
            "password": password,
            "rememberMe": remember_me
        }
        response = self.post(
            path="/v1/account/login",
            json=payload
        )
        return response

    def delete_v1_account_login(self, headers=None):
        """
        Выход из системы (логаут)

        :param headers: Заголовки запроса, должен содержать X-Dm-Auth-Token
        :return: Response
        """
        response = self.delete(
            path="/v1/account/login",
            headers=headers
        )
        return response

    def delete_v1_account_login_all(self, headers=None):
        """
        Выход из системы на всех устройствах

        :param headers: Заголовки запроса, должен содержать X-Dm-Auth-Token
        :return: Response
        """
        response = self.delete(
            path="/v1/account/login/all",
            headers=headers
        )
        return response
