# Groq Q&A CLI Application

This project is based on the provided `pystart` repository template.

The assignment requirement is to create a Python application (`main.py`) that talks to the Groq API. The user should be able to enter questions, the application must call the Groq API to generate responses, and the program must continue running in a loop until the user types `quit`.

This implementation satisfies all assignment requirements.

---

## Description

This application runs as a command-line interface (CLI).  
It performs the following steps:

1. Prompts the user to enter a question.
2. Sends the question to the Groq API.
3. Prints the AI-generated response.
4. Repeats the process in a loop.
5. Stops only when the user types `quit`.

The model used in this project is:
openai/gpt-oss-120b

--- 

## Requirements

Python 3.9 or higher is required.

Install dependencies using:

```bash
pip install -r requirements.txt
```
The requirements.txt file contains:
groq

---

## Environment Variable Setup

Before running the program, you must set your Groq API key.

### macOS / Linux
```bash
export GROQ_API_KEY="your_api_key_here"
```

### Windows PowerShell
```bash
$env:GROQ_API_KEY="your_api_key_here"
```

## GitHub Codespaces

Add a repository secret:

Name: GROQ_API_KEY

Value: your Groq API key

Then restart the Codespace.

## How to Run
```bash
python main.py
```
Example session:
```vbnet
Groq Chat ready. Type a question, or type "quit" to exit.

You: what is tesla
AI: Tesla is an American electric vehicle and clean energy company founded in 2003.

You: who founded apple
AI: Apple was founded by Steve Jobs, Steve Wozniak, and Ronald Wayne in 1976.

You: quit
Bye!
```

## Exit Condition
The program will continue running until the user types:
```nginx
quit
```
At that point, the application terminates.

