# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"Hello": "World"} 

from pydantic import BaseModel, Field
from typing import List
import instructor

import os
from groq import Groq

MODEL = "openai/gpt-oss-120b"

def main():
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        print("Missing GROQ_API_KEY. Set it in Codespaces Secrets.")
        return

    client = Groq(api_key=api_key)

    print('Groq Chat ready. Type a question, or type "quit" to exit.\n')

    while True:
        try:
            q = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nBye!")
            break

        if q.lower() == "quit":
            print("Bye!")
            break

        if not q:
            continue

        try:
            resp = client.chat.completions.create(
                model=MODEL,
                messages=[
                    {"role": "user", "content": q},
                    {"role": "system", "content": "Answer briefly in 1-2 sentences only."}
                    ],
                max_tokens=250,
                temperature=0.7,
            )
            answer = resp.choices[0].message.content
            print(f"AI: {answer}\n")
        except Exception as e:
            print(f"Error calling Groq API: {e}\n")

if __name__ == "__main__":
    main()


