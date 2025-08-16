# Gemini Project Guidelines

This document provides guidelines for the AI assistant to follow when working on this project.

## Project Overview

This is a simple Python web application that uses the Flask framework. The main application file is `app.py`.

## Dependencies

This project uses `pyproject.toml` to manage abstract dependencies and `requirements.lock` to store pinned versions.

### First-time Setup

1.  **Create a virtual environment:**
    ```bash
    uv venv
    ```

2.  **Activate the virtual environment:**
    ```bash
    source .venv/bin/activate
    ```

3.  **Install dependencies from the lock file:**
    ```bash
    uv pip sync requirements.lock
    ```

### Managing Dependencies

-   To add or update dependencies, modify the `dependencies` list in `pyproject.toml`.
-   After modifying `pyproject.toml`, update the lock file with:
    ```bash
    uv pip compile pyproject.toml -o requirements.lock
    ```

## Running the Application

To run the web server, execute the following command:

```bash
python app.py
```

The application will be available at http://localhost:5000.
