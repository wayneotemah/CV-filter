# Resume Processing API

This project is a RESTful API built with FastAPI for processing resumes. The API provides endpoints to process resume data, score them, store the results in a SQLite database, and retrieve the top resumes based on their scores.

## Table of Contents
- [Overview](#overview)
- [Technologies Used](#technologies-used)
- [Endpoints](#endpoints)
  - [Process Resumes](#process-resumes)
  - [Get Top Users](#get-top-users)
- [Setup and Installation](#setup-and-installation)
- [Running the Application](#running-the-application)
- [Integration](#integration)
- [Contributing](#contributing)
- [License](#license)

## Overview
The Resume Processing API was created to automate the evaluation of resumes by processing and scoring them. The API provides endpoints to submit resumes for scoring and to retrieve the top resumes based on their scores. This project aims to simplify the resume evaluation process, making it easy to integrate with other systems and applications.

## Technologies Used
- **FastAPI**: A modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.
- **SQLAlchemy**: The Python SQL toolkit and Object-Relational Mapping (ORM) library.
- **SQLite**: A C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine.
- **Pandas**: A data analysis and manipulation library for Python.

## Endpoints

### Process Resumes
- **URL**: `/process_resumes/`
- **Method**: `POST`
- **Description**: Processes and scores a resume, storing the result in the database.
- **Request Body**: `ResumeItem` (JSON)
- **Response**: JSON containing the processed resume data and score.

### Get Top Users
- **URL**: `/top_users/`
- **Method**: `GET`
- **Description**: Retrieves the top resumes based on their scores.
- **Query Parameters**:
  - `number` (int): The number of top resumes to retrieve.
- **Response**: An Excel file containing the top resumes.

## Setup and Installation
1. **Clone the repository**:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Create a virtual environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up the database**:
    ```sh
    python -c "from database import Base, engine; Base.metadata.create_all(bind=engine)"
    ```

## Running the Application
1. **Start the FastAPI server**:
    ```sh
    uvicorn main:app --reload
    ```

2. **Access the API documentation**:
    Open your browser and navigate to `http://127.0.0.1:8000/docs` to access the interactive API documentation.

## Integration
To integrate this API with other systems:
1. **Process Resumes**: Send a `POST` request to `/process_resumes/` with the resume data in the request body.
2. **Get Top Users**: Send a `GET` request to `/top_users/` with the `number` query parameter to retrieve the top resumes.

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes. Ensure your code follows the project's coding standards and includes relevant tests.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.