AI-Powered Twitter Response System

A lightweight AI-powered chatbot that generates Twitter-style responses using FastAPI and GPT4All. The chatbot leverages a custom knowledge graph to improve contextual awareness and reduce reliance on external APIs.

Features
- FastAPI-based REST API** for tweet response generation.
- Locally running GPT4All** for AI inference, minimizing API dependencies.
- Custom AI knowledge graph** to enhance response relevance.
- Automated testing with pytest** for API validation.
- Planned migration to Spring Boot (Java)** for scalability.

---

 Tech Stack
- Python 3.12
- FastAPI  for backend API
- GPT4All for local LLM inference
- NetworkX for knowledge graph representation
- Uvicorn for ASGI server
- pytest for testing

---

Installation

1 Clone the repository

$ git clone https://github.com/layered-devin/twitter-style-ai-chatbot.git
$ cd twitter-style-ai-chatbot


2Create a virtual environment and install dependencies

$ python -m venv venv
$ source venv/bin/activate  # On Windows: venv\Scripts\activate
$ pip install -r requirements.txt


3 Run the FastAPI server

$ python app.py

This will start the API server at http://127.0.0.1:8000

4Test the API

$ python tests/test_api.py

If the setup is correct, you should see:



---

API Endpoints

`POST /generate_reply/`** - Get AI-generated Twitter-style reply
Request Body:

{
  "text": "What do you think about AI?"
}

Response:

{
  "reply": "AI is like a genie that grants wishes, but instead of granting your wish, it just makes your life worse."
}


Open the interactive API docs at [`http://127.0.0.1:8000/docs`](http://127.0.0.1:8000/docs) 


All local tests pass. The CI/CD may fail due to environmental problems and needs to be repaired later
