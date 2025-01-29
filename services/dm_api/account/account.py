from common.rest_client import RestClient


class AccountApi(RestClient):
    def post_v1_account(self, json: dict):
        """
        Регистрация нового аккаунта.

        :param json: {
            "login": str,
            "email": str,
            "password": str
        }
        :return: Response
        """
        response = self.post(
            path="/v1/account",
            json=json
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

    def put_v1_account_email(self, json: dict):
        """
        Смена email пользователя.

        :param json: {
            "login": str,
            "email": str,
            "password": str
        }
        :return: Response
        """
        response = self.put(
            path="/v1/account/email",
            json=json
        )
        return response

    def get_v1_account(self, **kwargs):
        """
        Получение информации о текущем пользователе

        Args:
            **kwargs: Дополнительные параметры запроса (headers, params и т.д.)
        """
        response = self.get(
            path="/v1/account",
            **kwargs
        )
        return response

    def post_v1_account_password(self, json: dict):
        """
        Запрос на сброс пароля

        :param json: {
            "login": str,
            "email": str
        }
        :return: Response
        """
        response = self.post(
            path="/v1/account/password",
            json=json
        )
        return response

    def put_v1_account_password(self, json: dict):
        """
        Смена пароля пользователя

        :param json: {
            "oldPassword": str,
            "newPassword": str,
            "resetToken": str (optional)
        }
        :return: Response
        """
        response = self.put(
            path="/v1/account/password",
            json=json
        )
        return response
