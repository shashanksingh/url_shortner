import yaml

"""
This class is usefull during internalization efforts
As all strings used are collected in one place. 
"""


class Constants:
    ALL_SYSTEMS_GO = "All systems go :rocket:"
    OOPS_SOMETHING_WENT_WRONG = "Oops ! Something went wrong"
    API_PORT_EXPOSED = 9090
    REDIRECT_PORT_EXPOSED = 5000
    HTTP_RESPONSE_CODE_FOR_PERMANENTLY_MOVED = 302
    RUNNING_ON_PORT = f"Running on port {API_PORT_EXPOSED} :thumbs_up:"
    OPEN_THE_POD_BAY_DOOR = "Open the POD BAY Door ! HAL"
    MAX_WORKERS_FOR_SERVER = 10
    MYSQL_USER_NAME = "user"
    MYSQL_PASSWORD = "password"
    MYSQL_HOST = "127.0.0.1"
    MYSQL_DB = "db"
    MYSQL_PROTOCOL = "mysql+mysqldb"
    BASE_DOMAIN_FOR_REDIRECTION_SERVICE = "http://localhost:5000/"