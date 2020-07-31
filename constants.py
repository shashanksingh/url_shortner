import yaml

"""
This class is usefull during internalization efforts
As all strings used are collected in one place. 
"""


class Constants:
    ALL_SYSTEMS_GO = "All systems go :rocket:"
    PORT_EXPOSED = 9090
    RUNNING_ON_PORT = f"Running on port {PORT_EXPOSED} :thumbs_up:"
    OPEN_THE_POD_BAY_DOOR = "Open the POD BAY Door ! HAL"
    MAX_WORKERS_FOR_SERVER = 10
    MYSQL_USER_NAME = "user"
    MYSQL_PASSWORD = "password"
    MYSQL_HOST = "password"
    BASE_DOMAIN_FOR_REDIRECTION_SERVICE = "http://localhost:5000/"