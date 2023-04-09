FROM python:3.10-bullseye
COPY requirements.txt requirements.txt
ADD app.py /
RUN pip3 install -r requirements.txt
ENV DATA_PATH="data/log.txt"
EXPOSE 5000:5000
VOLUME ["/data"]
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]