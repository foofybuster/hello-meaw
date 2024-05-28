FROM python:3.12.3

COPY . /app

WORKDIR /app
RUN apt update && apt install ffmpeg libsm6 libxext6  -y 
RUN python -m pip install --upgrade setuptools
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt 
CMD ["python", "-m", "greeter_server"]
EXPOSE 50051
