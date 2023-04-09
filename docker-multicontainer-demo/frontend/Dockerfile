FROM python:3.10-bullseye
COPY . ./
RUN pip3 install -r requirements.txt
EXPOSE 5000:5000
VOLUME ["/data"]
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]