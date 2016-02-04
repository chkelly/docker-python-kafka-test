FROM orchardup/python:2.7
ADD . /code
WORKDIR /code
RUN apt-get update && apt-get install -y git
RUN pip install -r requirements.txt
CMD python app.py
