# AI Resume Analyzer

## 🚀 Live Demo
👉 [Click here to try the app](https://ai-resume-analyzer-ckb1.onrender.com)

## Screenshots

### Home Page
![Home](screenshots/home.png)

### Result Example
![Result](screenshots/result.png)

---

## Overview

AI Resume Analyzer is a full-stack web application that analyzes resume text using an AI model and provides structured feedback such as strengths, weaknesses, suggestions, and a job match score.

---

## Features

* Analyze resume strengths and weaknesses
* Provide actionable improvement suggestions
* Match resume to a job description
* Return a match summary and score
* Clean and simple Bootstrap-based UI

---

## Tech Stack

* Python
* FastAPI
* HTML, JavaScript, Bootstrap
* OpenAI API

---

## How It Works

1. The user pastes a resume and optionally a job description
2. The frontend sends the data to the FastAPI backend using a POST request
3. The backend builds a structured prompt
4. The backend sends the prompt to the OpenAI API
5. The model analyzes the resume and returns structured JSON
6. The backend parses the response
7. The frontend displays the result dynamically

---

## Project Structure

```bash
ai-resume-analyzer/
├── app/
│   ├── main.py
│   ├── prompts.py
│   ├── schemas.py
│   ├── services/
│   │   └── ai_service.py
│   └── templates/
│       └── index.html
├── screenshots/
│   ├── home.png
│   └── result.png
├── static/
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt
```

---

## Setup

### 1. Clone the repository

```
git clone <your-repo-url>
cd ai-resume-analyzer
```

### 2. Create a virtual environment

Linux/macOS:

```
python3 -m venv venv
source venv/bin/activate
```

Windows:

```
python -m venv venv
venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Create a `.env` file

```
OPENAI_API_KEY=your_api_key_here
```

### 5. Run the application

```
uvicorn app.main:app --reload
```

Open in browser:

http://127.0.0.1:8000

---

## Example Input

**Resume:**
Computer science student with Java and PostgreSQL experience. Built a backend REST API project.

**Job Description:**
Looking for a working student backend developer with API and database skills.

---

## What I Learned

* Building APIs with FastAPI
* Structuring requests and responses using Pydantic
* Integrating an AI API into a real application
* Designing prompts for structured output
* Connecting frontend and backend using JavaScript

---

## Future Improvements

* PDF resume upload
* Improved UI/UX
* Better error handling
* Rate limiting for public deployment

---

## Disclaimer

This tool provides AI-generated feedback and should be used as guidance, not as a definitive evaluation.
