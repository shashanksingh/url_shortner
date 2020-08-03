There are two steps
a. Docker-Compose
b. Makefile

a. Docker Compose
    `docker-compose -f docker-compose.dev.yml  up database`


b. Makefile
1. Install Python 3.8+
2. Install virtualenv
    `pip install pyenv pyenv-virtualenv`
    `pyenv virtualenv 3.8 url-shortner-3.8`
    `pyenv activate url-shortner-3.8`
3. Install 2to3 in same session:
    `pip install 2to3`
3. Install GRPC io and requirements in same session: 
    `pip install grpcio`
    `pip install -r requirements-dev.txt`
    more details here https://grpc.io/docs/languages/python/quickstart/
4. Run in separate tabs with `pyenv activate url-shortner-3.8` executed in that tab:
    `make run_server`
    `make run_redirection_service`
    `make run_clients`    
        

`

5. Everything is now up and running