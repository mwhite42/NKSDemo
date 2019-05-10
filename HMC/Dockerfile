FROM python:3.6

COPY requirements.txt /
RUN pip install -r requirements.txt

COPY css/ /css
COPY index.jinja2 /
COPY hmc.mp4 /
COPY hmc.py /


CMD [ "python", "hmc.py" ]

