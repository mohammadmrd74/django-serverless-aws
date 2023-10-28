# Python Django and serverless with AWS

A RESTful Django application connected to AWS services using the Serverless Framework.

## Local Development

To run the project locally, follow these steps:

1. Install the Serverless Framework globally: ```npm i -g serverless```
2. Install two plugins for serverless: ```serverless plugin install -n serverless-wsgi``` ```serverless plugin install -n serverless-python-requirements```
2. Activate your virtual environment: ```source /venv/bin/activate```
3. Install Python dependencies using pip: ```python -m pip install -r requirements.txt```
4. ```aws configure``` (Enter your AWS Access Key and Secret Key when prompted).
5. ```python manage.py runserver``` 
6. app will be running on ```http://localhost:8000```


## Deployment to AWS Lambda

After completing the configuration and testing locally, you can deploy the project as an AWS Lambda function:

```serverless deploy```

This command will package and deploy your application to AWS Lambda and configure the necessary AWS resources.

## Available Endpoints

The application exposes two endpoints that can be tested using Postman or other API testing tools:

1. **Create a Device (POST Request):**
   - Endpoint: `<aws-gateway>/api/devices`
   - Description: This endpoint allows you to create a new device by sending a POST request.

2. **Get a Device (GET Request):**
   - Endpoint: `<aws-gateway>/{device_id}`
   - Description: This endpoint retrieves information about a device by providing its ID in a GET request.

## Postman Collection

A Postman collection for testing the API endpoints is provided in the `/postman` directory. You can import this collection into Postman to simplify the testing process.

## Running Unit Tests

You can run unit tests for the project using the following command:
```python manage.py test```

