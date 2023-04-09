FROM python:3.10-bullseye
COPY requirements.txt requirements.txt
ADD reader.py /
RUN pip3 install -r requirements.txt
ENV DATA_PATH="data/log.txt"
ENV WAIT_TIME=5
ENV CHECKUP_FREQ=6
# ENV WRITER_ENDPOINT="" ; commented out because this is likely unknowable until runtime
VOLUME ["/data"]
CMD ["python", "./reader.py"]