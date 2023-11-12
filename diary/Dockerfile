# Dockerfile

# pull the official docker image
FROM python:3.11

WORKDIR home

# copy project
COPY ./src .

# copy dependencies
COPY requirements.txt .

# install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# cmd command
CMD ["uvicorn", "asgi:app", "--host", "0.0.0.0", "--port", "8000"]
