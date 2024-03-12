# How to use Environment Variables

Storing sensitive information, such as API keys, in environment variables is a security best practice. It prevents sensitive data from being hardcoded into your scripts, which can accidentally be exposed or shared, especially when your code is stored in version control systems.

## 1. Install python-dotenv

First, you need to install the `python-dotenv` package. Activate your virtual environment and install the package using pip:

```bash
pip install python-dotenv
```

## 2. Create a .env file

In the root directory of your project, create a file named `.env`. This file will contain your environment variables, such as:

```python
API_KEY = "your_api_key_here"
SECRET_KEY = "your_secret_key_here"
```

Replace `your_api_key_here` and `your_secret_key_here` with your actual sensitive data.

**Important:** Add .env to your .gitignore file to prevent it from being checked into version control.

## 3. Load and use Environment Variables in your Python script

In your Python script, use the `python-dotenv` package to load the environment variables from the `.env` file and then access them using the `os` module:

```python
import os
from dotenv import load_dotenv

# Load the environment variables from .env file
load_dotenv()

# Access the environment variables
api_key = os.getenv('API_KEY')
secret_key = os.getenv('SECRET_KEY')

# Use the environment variables, for example, in an API request
print(api_key, secret_key)
```

The `load_dotenv()` function loads the environment variables from the `.env` file into your script's environment, where they can be accessed using `os.getenv()`.

## Best Practices and Notes:

### Security

Never commit your `.env` file to your version control system. Always add the `.env` file to your `.gitignore `to ensure it remains private.

### Default Values

You can provide a default value when using `os.getenv()` if the environment variable is not set. For example, `os.getenv('API_KEY', 'default_value')`.

### Environment Specific Files

For different environments (development, testing, production), you can create different `.env` files, like `.env.dev, .env.test, .env.prod`, and load the relevant file based on your environment.