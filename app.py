import sys
import os
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from src.train_model import generate_reply 

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

app = FastAPI()

class TweetRequest(BaseModel):
    text: str

@app.post("/generate_reply/")
def get_reply(request: TweetRequest):
    """ Generate Twitter-style replies through HTTP POST requests """
    reply = generate_reply(request.text)
    return {"reply": reply}

def cli_mode():
    """ Interact with CLI """
    print("\n💬 Enter a tweet to get a reply (type 'exit' to quit):")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        reply = generate_reply(user_input)
        print(f"TwiUser: {reply}")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "cli":
        cli_mode()
    else:
        uvicorn.run(app, host="0.0.0.0", port=8000)
