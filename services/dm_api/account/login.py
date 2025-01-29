from common.rest_client import RestClient


class LoginApi(RestClient):

    def post_v1_account_login(self, json: dict):
        """
        Авторизация пользователя

        :param json: {
            "login": str,
            "password": str,
            "rememberMe": bool
        }
        :return: Response
        """
        response = self.post(
            path="/v1/account/login",
            json=json
        )
        return response

    def delete_v1_account_login(self, **kwargs):
        """
        Выход из системы (логаут)

        :param kwargs: {
            headers: dict, optional {
                "X-Dm-Auth-Token": str
            }
        }
        :return: Response
        """
        response = self.delete(
            path="/v1/account/login",
            **kwargs
        )
        return response

    def delete_v1_account_login_all(self, **kwargs):
        """
        Выход из системы на всех устройствах

        :param kwargs: {
            headers: dict, optional {
                "X-Dm-Auth-Token": str
            }
        }
        :return: Response
        """
        response = self.delete(
            path="/v1/account/login/all",
            **kwargs
        )
        return response
