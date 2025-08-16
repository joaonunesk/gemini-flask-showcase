# Gemini Flask Showcase

A simple Python web application using Flask, demonstrating login/logout functionality and HTMX integration.

## Features

- User authentication (login/logout)
- Session management
- HTMX-powered frontend for dynamic content swapping
- Simple template structure

## Project Structure

```
app.py                # Main Flask application
templates/            # HTML templates
tests/                # Pytest-based test suite
pyproject.toml        # Project dependencies
requirements.lock     # Locked dependency versions
```

## Setup

1. **Create a virtual environment:**
    ```bash
    uv venv
    ```

2. **Activate the virtual environment:**
    ```bash
    source .venv/bin/activate
    ```

3. **Install dependencies:**
    ```bash
    uv pip sync requirements.lock
    ```

## Running the Application

Start the Flask server:

```bash
python app.py
```

Visit [http://localhost:5000](http://localhost:5000) in your browser.

## Running Tests

```bash
pytest
```