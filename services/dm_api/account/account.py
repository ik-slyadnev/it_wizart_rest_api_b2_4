from common.rest_client import RestClient


class AccountApi(RestClient):
    def post_v1_account(self, login: str, email: str, password: str):
        """
        Регистрация нового аккаунта.

        :param login: Логин пользователя
        :param email: Email пользователя
        :param password: Пароль пользователя
        :return: Response
        """
        payload = {
            "login": login,
            "email": email,
            "password": password
        }
        response = self.post(
            path="/v1/account",
            json=payload
        )
        return response

    def put_v1_account_token(self, token: str):
        """
        Активация аккаунта по токену.

        :param token: Токен активации
        :return: Response
        """
        response = self.put(
            path=f"/v1/account/{token}"
        )
        return response

    def put_v1_account_email(self, login: str, new_email: str, password: str):
        """
        Смена email пользователя.

        :param login: Логин пользователя
        :param password: Пароль пользователя
        :param new_email: Новый email пользователя
        :return: Response
        """
        payload = {
            "login": login,
            "email": new_email,
            "password": password
        }
        response = self.put(
            path="/v1/account/email",
            json=payload
        )
        return response

    def get_v1_account(self):
        """
        Получение информации о текущем пользователе
        """
        response = self.get(
            path="/v1/account"
        )
        return response

    def post_v1_account_password(self, login: str, email: str):
        """
        Запрос на сброс пароля

        :param login: Логин пользователя
        :param email: Email пользователя
        :return: Response
        """
        payload = {
            "login": login,
            "email": email
        }
        response = self.post(
            path="/v1/account/password",
            json=payload
        )
        return response

    def put_v1_account_password(self, old_password: str, new_password: str, reset_token: str = None):
        """
        Смена пароля пользователя

        :param old_password: Текущий пароль
        :param new_password: Новый пароль
        :param reset_token: Токен сброса пароля (опционально)
        :return: Response
        """
        payload = {
            "oldPassword": old_password,
            "newPassword": new_password
        }
        if reset_token:
            payload["resetToken"] = reset_token

        response = self.put(
            path="/v1/account/password",
            json=payload
        )
        return response