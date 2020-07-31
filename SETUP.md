1. Install Python 3.8+
2. Install virtualenv
3. Install 2to3 :
    `pip install 2to3`
3. Install GRPC io : 
    `python -m pip install grpcio`
    more details here https://grpc.io/docs/languages/python/quickstart/
4. Run :
    `make build`
    It should output something like

`
Starting url_shortner_database_1 ... done
Creating url_shortner_api-service_1 ... done
Creating url_shortner_redirection-service_1 ... done
Attaching to url_shortner_database_1, url_shortner_api-service_1, url_shortner_redirection-service_1
api-service_1          | python -m main
database_1             | 2020-07-31 17:14:00+00:00 [Note] [Entrypoint]: Entrypoint script for MySQL Server 8.0.21-1debian10 started.
database_1             | 2020-07-31 17:14:00+00:00 [Note] [Entrypoint]: Switching to dedicated user 'mysql'
redirection-service_1  | python -m main
database_1             | 2020-07-31 17:14:00+00:00 [Note] [Entrypoint]: Entrypoint script for MySQL Server 8.0.21-1debian10 started.
database_1             | 2020-07-31T17:14:00.581950Z 0 [System] [MY-010116] [Server] /usr/sbin/mysqld (mysqld 8.0.21) starting as process 1
database_1             | 2020-07-31T17:14:00.590076Z 1 [System] [MY-013576] [InnoDB] InnoDB initialization has started.
database_1             | 2020-07-31T17:14:00.815597Z 1 [System] [MY-013577] [InnoDB] InnoDB initialization has ended.
database_1             | 2020-07-31T17:14:00.930444Z 0 [System] [MY-011323] [Server] X Plugin ready for connections. Bind-address: '::' port: 33060, socket: /var/run/mysqld/mysqlx.sock
database_1             | 2020-07-31T17:14:01.036421Z 0 [Warning] [MY-010068] [Server] CA certificate ca.pem is self signed.
database_1             | 2020-07-31T17:14:01.036621Z 0 [System] [MY-013602] [Server] Channel mysql_main configured to support TLS. Encrypted connections are now supported for this channel.
database_1             | 2020-07-31T17:14:01.039466Z 0 [Warning] [MY-011810] [Server] Insecure configuration for --pid-file: Location '/var/run/mysqld' in the path is accessible to all OS users. Consider choosing a different directory.
database_1             | 2020-07-31T17:14:01.062844Z 0 [System] [MY-010931] [Server] /usr/sbin/mysqld: ready for connections. Version: '8.0.21'  socket: '/var/run/mysqld/mysqld.sock'  port: 3306  MySQL Community Server - GPL.
`

5. Everything is now up and running