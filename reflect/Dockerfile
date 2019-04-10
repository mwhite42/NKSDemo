FROM python:3.6

COPY requirements.txt /
RUN pip install -r requirements.txt

COPY reflect.py /

CMD [ "python", "reflect.py" ]

