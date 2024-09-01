# Applicant Tracking System (ATS)

## Overview

The Applicant Tracking System (ATS) is a web application designed to efficiently manage job applications. The project consists of:

- **Backend**: Developed with Flask, this component provides a RESTful API to manage candidate data.
- **Frontend**: Built using Streamlit, this component provides a user-friendly interface to interact with the data.

## Project Architecture

The project is divided into two main components:

- **Backend**: Flask application that provides an API for CRUD operations.
- **Frontend**: Streamlit application that allows users to add, update, delete, and view candidates.

## Prerequisites

- Python 3.6+
- Flask
- Flask-SQLAlchemy
- Streamlit
- Requests

## Installation

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/oliviertina29/ats.git
    cd ats
    ```

2. **Create and Activate a Virtual Environment:**

    ```bash
    python -m venv ats
    source ats/bin/activate  # Use `ats\Scripts\activate` for Windows
    ```

3. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

Make sure the backend and frontend use the same API URL. The default backend URL is `http://127.0.0.1:5000`.

## Usage

1. **Run the Backend:**

    ```bash
    cd backend
    python app.py
    ```

    The backend will be available at `http://127.0.0.1:5000`.

2. **Run the Frontend:**

    ```bash
    cd frontend
    streamlit run app.py
    ```

    The frontend will be available at `http://localhost:8501`.

## Features

- **Add Candidate**: Fill out a form to add a new candidate.
- **Update Candidate**: Modify the details of an existing candidate.
- **Delete Candidate**: Remove a candidate from the database.
- **View Candidates**: Display a list of all candidates.
- **Match Candidates with Job Description**: Submit a job description to receive a ranked list of candidates sorted by their relevance and suitability for the position based on their resumes.
- **Automated Scoring**: The ATS automatically evaluates and scores candidates based on keyword matching and skills relevant to the job description provided.
- **RESTful API Integration**: The backend is implemented using a RESTful API, allowing for seamless integration with various front-end applications or third-party tools.


## Project Structure

```
ats/
│
├── backend/
│   └──  app.py                  # Flask backend code        
│
├── frontend/
│   └── app.py                  # Streamlit frontend code
│    
├── instance/
│   └── ats.db                  # SQLite database file
│
├── requirements.txt 
│
└── README.md                   # This file
```


## Contributions

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
