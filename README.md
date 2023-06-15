# Mail Service

The Mail Service is a webservice that provides an API for managing packages and post offices. It allows users to track packages, view post office information, and perform various package-related operations.

## Features

- Package management: Create, update, and delete packages.
- Post office management: Add and edit post office details.
- Package tracking: Track the status and location of packages.
- User authentication: Register, login, and manage user accounts.
- API endpoints: Provides a RESTful API for integrating with other systems.

## Installation

### Prerequisites

- Docker: Ensure that Docker and docker-compose are installed on your machine.

### Setup

1. Clone the repository:

   ```shell
   git clone https://github.com/your-username/mail-service.git

2.Navigate to the project directory:
cd mail-service

3.Build and run the Docker containers:
docker-compose up --build

4.Access the application:
Web application: Open a web browser and visit http://localhost:8080.
API documentation: The API documentation can be accessed at http://localhost:8080/api/docs.

### Configuration
The application can be configured through environment variables. Create a .env file in the project root directory and provide the following variables:
- Database configuration:
POSTGRES_USER=postgres
POSTGRES_PASSWORD=password
POSTGRES_DB=mailing-service-db

- Application configuration:
DATABASE_URL=postgresql://postgres:password@mailing-service-db:5432/mailing-service-db

### Development
To contribute to the Mail Service project, follow these steps:

- Fork the repository on GitHub.
- Clone your forked repository.
- Create a new branch for your feature or bug fix.
- Make the necessary changes and commit them.
- Push the changes to your forked repository.
- Submit a pull request to the main repository.

## Dev API Testing Examples
- curl -X POST -H "Content-Type: application/json" -d '{"address": "123 Main St", "zip_code": "12345", "name": "Post Office 1"}' http://localhost/api/postoffice
- curl -X GET http://localhost/api/postoffice/{id}
- curl -X POST -H "Content-Type: application/json" -d '{"destination_address": "456 Elm St", "destination_zip_code": "67890", "recipient_name": "John Doe", "id": "abc123", "type": "letter"}' http://localhost/api/package
- curl -X GET http://localhost/api/package/{id}
- curl -X POST -H "Content-Type: application/json" -d '{"package_id": "abc123"}' http://localhost/api/postoffice/{id}/arrival
- curl -X POST -H "Content-Type: application/json" -d '{"package_id": "abc123"}' http://localhost/api/postoffice/{id}/departure

## Supported OS
- Linux based OS
- WSL in NOT supported!

### License
This project is licensed under the MIT License. See the LICENSE file for more details.