FROM tiangolo/uwsgi-nginx-flask:python3.9
COPY ./dplot_server.py ./
COPY ./data ./data
COPY ./logs ./logs
COPY ./requirements.txt ./
COPY ./uwsgi_docker_config.ini ./uwsgi.ini
RUN pip install -r requirements.txt