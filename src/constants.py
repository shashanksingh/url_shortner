import yaml


class ConstantYML:
    def __init__(self):
        with open("../config-dev.yml", "r") as stream:
            try:
                self.yml = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)


class Constants:
    ConstantYMLOBJECT = ConstantYML()
    ALL_SYSTEMS_GO = "All systems go :rocket:"
    PORT_EXPOSED = 9090
    RUNNING_ON_PORT = f"Running on port {PORT_EXPOSED} :thumbs_up:"
    MAX_WORKERS_FOR_SERVER = 10
    MYSQL_USER_NAME = ConstantYMLOBJECT.yml.MYSQL_USER_NAME
    MYSQL_PASSWORD = ConstantYMLOBJECT.yml.MYSQL_PASSWORD
    MYSQL_HOST = ConstantYMLOBJECT.yml.MYSQL_HOST
