FROM python:3
LABEL version="0.0.1"


WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN FLASK_ENV=development
RUN FLASK_APP=clients/redirection_service.py
COPY . .

CMD [ "make", "run_server" ]
EXPOSE 9090