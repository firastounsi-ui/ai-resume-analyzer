# AI Resume Analyzer

AI Resume Analyzer is a web application that analyzes resume text using an AI model and provides feedback such as strengths, weaknesses, suggestions, and a job match score.

## Features

* Analyze resume strengths and weaknesses
* Provide improvement suggestions
* Match resume to a job description
* Show a match score
* Simple and clean user interface

## Tech Stack

* Python
* FastAPI
* HTML, JavaScript, Bootstrap
* OpenAI API

## How It Works

1. The user pastes a resume and optionally a job description
2. The frontend sends the data to the backend
3. The backend sends the data to an AI model
4. The model analyzes the resume
5. The result is returned and displayed in the browser

## Setup

1. Clone the repository

```
git clone <your-repo-url>
cd ai-resume-analyzer
```

2. Create a virtual environment

```
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies

```
pip install -r requirements.txt
```

4. Create a `.env` file

```
OPENAI_API_KEY=your_api_key_here
```

5. Run the app

```
uvicorn app.main:app --reload
```

Open in browser:
http://127.0.0.1:8000

## What I Learned

* How to build a backend with FastAPI
* How to call an AI API
* How to structure input and output
* How to connect frontend and backend

## Disclaimer

This tool gives AI-generated feedback and should not be considered perfect or final.
