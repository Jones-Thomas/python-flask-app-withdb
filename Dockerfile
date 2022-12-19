FROM python:3.8-slim-buster

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

ENV FLASK_APP="app.py"

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]

# Command to b uild the Image
# docker build -t myapp:0.1 .

# Command to spin the container
# docker run -d --name profile_app -p 5000:5000 myapp:0.1