# Dockerfile

# pull the official docker image
FROM python:3.11

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY requirements.txt .

RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# copy project
COPY . .

#path app
ENV PYTHONPATH "${PYTHONPATH}:/src/"

#set port
EXPOSE 8000

# cmd command
CMD ["uvicorn", "src.main:application", "--host", "0.0.0.0", "--port", "8000"]
