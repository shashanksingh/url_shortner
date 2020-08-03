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
        
5. Everything is now up and running


To Run Tests
`pyenv activate url-shortner-3.8`
`make test`

would output something like:

`benchmark: 3.2.3 (defaults: timer=time.perf_counter disable_gc=False min_rounds=5 min_time=0.000005 max_time=1.0 calibration_precision=10 warmup=False warmup_iterations=100000)
plugins: mock-3.2.0, benchmark-3.2.3
collected 4 items                                                                                                                                                                                                                          

tests/test_performance_bechmark.py::test_performance_of_saving_all_graphs_into_storage 
Pulling image mysql:8.0.21
⠼
Container started:  ed2b0488ef
plugins: mock-3.2.0, benchmark-3.2.3
collected 1 item                                                                                                                                                                                                                           

tests/test_url_shortner_service_controller.py::test_e2e_from_controller_to_database_for_all_functionality 
Pulling image mysql:5.7.28
⠼
Container started:  f396bbb74b
Waiting to be ready...
PASSED

