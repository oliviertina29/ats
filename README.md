# Applicant Tracking System (ATS)

## Overview

The Applicant Tracking System (ATS) is a web application designed to efficiently manage job applications. The project consists of:

- **Backend**: Developed with Flask, this component provides a RESTful API to manage candidate data.
- **Frontend**: Built using Streamlit, this component provides a user-friendly interface to interact with the data.

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

- **Dashboard**: Provides an overview of key statistics, including total candidates, status distribution, and recent activities.
- **Add Candidate**: Fill out a form to add a new candidate with details such as name, email, resume, and status.
- **Update Candidate**: Modify the details of an existing candidate, including the ability to fetch current data before editing.
- **Delete Candidate**: Remove a candidate from the database.
- **View Candidates**: Display a list of all candidates with a sortable and searchable table.
- **Match Candidates with Job Description**: Submit a job description to receive a ranked list of candidates sorted by their relevance and suitability for the position based on their resumes.
- **Automated Scoring**: The ATS automatically evaluates and scores candidates based on keyword matching and skills relevant to the job description provided.
- **Data Visualization**: Includes charts and graphs to visualize candidate data, such as status distribution and candidates added per month.
- **Recent Activities Tracking**: Displays recent actions performed in the system, providing an audit trail of changes.
- **RESTful API Integration**: The backend is implemented using a RESTful API, allowing for seamless integration with various front-end applications or third-party tools.
- **User-friendly Interface**: Streamlit-based frontend provides an intuitive and responsive user interface.
- **Real-time Data Updates**: Dashboard and other views reflect real-time data from the database.
- **Search Functionality**: Ability to search and filter candidates based on various criteria.
- **Responsive Design**: The application is designed to work well on both desktop and mobile devices.

## Project Structure

```
ats/
│
├── backend/
│   ├── api.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── frontend/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── instance/
│   └── ats.db
│
├── docker-compose.yml
│
└── README.md                   # This file
```


## Contributions

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
