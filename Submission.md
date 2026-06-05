# Week 1 Submission

## Overview

I built a terminal chatbot using OpenRouter and the OpenAI SDK. The chatbot can hold multi-turn conversations, remember previous messages, reset conversation history, and show token usage.

## Setup

* Created an OpenRouter account and API key.
* Stored the key in a `.env` file.
* Added `.env` to `.gitignore` so the key never gets pushed to GitHub.
* Used `python-dotenv` to load environment variables.

## Features Implemented

* Multi-turn chatbot
* ChatAgent class
* Model selection
* `/reset` command
* `/tokens` command
* Rolling memory buffer
* Exit command

## Design Decisions

### Conversation History

I stored all messages inside a `messages` list containing system, user, and assistant messages. I chose this approach because the API is stateless and previous conversation history must be sent with every request.

### ChatAgent Class

I implemented a `ChatAgent` class to manage conversation state, API calls, token tracking, and reset functionality. This keeps the code more organized compared to placing everything in a single function.

### Rolling Memory Buffer

I implemented a rolling memory buffer using `max_turns`. This prevents conversation history from growing indefinitely and helps control token usage.

### Reset Command

I implemented a `/reset` command to clear conversation history and demonstrate how stateless APIs work.

### Token Usage Command

I implemented a `/tokens` command to inspect prompt and completion token usage.

## Problems Faced

* Initially, `python-dotenv` was not installed, which caused import errors.
* Some OpenRouter models returned 404 errors because the model name was unavailable or outdated.
* Several free models returned 429 rate-limit errors, so I had to test different models before finding one that worked reliably.
* I accidentally ran the project with a different Python installation, which caused package-related errors.
* I faced indentation errors while modifying the chatbot loop and adding new commands.
* Git was not installed/configured initially, which prevented me from creating a repository and pushing my code to GitHub.

## Key Learnings

* How to make API calls using OpenRouter.
* How chat templates use system, user, and assistant roles.
* Why LLM APIs are stateless.
* How conversation history acts as memory.
* How token usage affects context length and cost.
* Why API keys should be stored securely.
* Basic Git and GitHub workflow.

## Conclusion

This project helped me understand how chat-based AI applications work, how conversation state is managed, and how LLM APIs are used in practice.
