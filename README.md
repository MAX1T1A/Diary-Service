# Diary Service

Welcome to Diary Service, an application built using Python and FastAPI that allows users to create, read, update, and delete diary entries. But don't let its simplicity fool you; Diary Service is a powerful tool that can help you keep track of your daily activities, goals, and accomplishments.

## Getting Started
Are you ready to start using Diary Service? Great! To get started, all you need is Docker and Docker Compose installed on your system. Once you have those installed, you can simply clone this repository and run docker-compose up to start the application.

```bash
git clone https://github.com/Berupor/diary-service.git
cd diary-service
docker-compose up --build
```

That's it! Diary Service is now up and running, and you can access it by navigating to http://localhost:8000 in your web browser.

## API Documentation
Diary Service uses FastAPI's built-in API documentation to provide information on how to use the API. But don't worry; you don't need to be a FastAPI expert to use Diary Service. The API documentation is easy to read and understand, and it provides all the information you need to get started.

To access the API documentation, simply navigate to http://localhost:8000/docs in your web browser. There, you'll find a list of all the available endpoints, along with descriptions of what each endpoint does and how to use it.

## Authentication
Diary Service uses JWT for authentication. This means that when you create an account or log in, you will receive a JWT token that you will need to include in the headers of your requests to the API. Don't worry; this process is simple and straightforward, and it helps to keep your data secure.

## Database
Diary Service uses Postgres as its database. The database is automatically created when you run the application using Docker Compose, so you don't need to worry about setting up the database yourself.

Contributing
Do you want to contribute to Diary Service? That's great! We welcome contributions from anyone who is interested in improving the project. To contribute, simply fork this repository, make your changes, and submit a pull request. Please make sure to follow the existing coding style and include tests for any new functionality.

Thank you for using Diary Service! We hope it helps you stay organized and productive.
