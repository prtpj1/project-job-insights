FROM python:3.9-bullseye

ADD . /job-insights-docker
WORKDIR /job-insights-docker
COPY ./ /job-insights-docker

RUN python3 -m pip install --upgrade pip
RUN pip install -r dev-requirements.txt

CMD flask run --host=0.0.0.0
