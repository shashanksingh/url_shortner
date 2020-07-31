import yaml

"""
This class is loads the YML file config
in real world production system it would rather load from
a Config server
"""


class ConstantYML:
    def __init__(self):
        config_file = "config-dev.yml"
        with open(config_file, "r") as stream:
            try:
                self.yml = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)


"""
This class is usefull during internalization efforts
As all strings used are collected in one place. 
"""


class Constants:
    ConstantYMLOBJECT = ConstantYML()
    ALL_SYSTEMS_GO = "All systems go :rocket:"
    PORT_EXPOSED = 9090
    RUNNING_ON_PORT = f"Running on port {PORT_EXPOSED} :thumbs_up:"
    OPEN_THE_POD_BAY_DOOR = "Open the POD BAY Door ! HAL"
    MAX_WORKERS_FOR_SERVER = 10
    # print(ConstantYMLOBJECT.yml)
    # MYSQL_USER_NAME = ConstantYMLOBJECT.yml.MYSQL_USER_NAME
    # MYSQL_PASSWORD = ConstantYMLOBJECT.yml.MYSQL_PASSWORD
    # MYSQL_HOST = ConstantYMLOBJECT.yml.MYSQL_HOST
    BASE_DOMAIN_FOR_REDIRECTION_SERVICE = "http://localhost:9091/"
