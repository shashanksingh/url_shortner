FROM python:3
LABEL version="0.0.1"


WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "make", "run_redirection_service" ]
EXPOSE 5000