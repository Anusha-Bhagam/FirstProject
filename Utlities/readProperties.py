import configparser

config = configparser.RawConfigParser()
config.read('.\\Configurations\\config.ini')


class ReadConfig:
    @staticmethod
    def get_application_url():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def get_username():
        uname = config.get('common info', 'username')
        return uname

    @staticmethod
    def get_password():
        pwd = config.get('common info', 'password')
        return pwd
