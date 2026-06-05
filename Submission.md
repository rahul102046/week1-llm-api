I built a terminal chatbot using OpenRouter and the OpenAI SDK. The chatbot can hold multi-turn conversations, remember previous messages, reset conversation history, and show token usage.
Setup
Created an OpenRouter account and API key.
Stored the key in a .env file.
Added .env to .gitignore so the key never gets pushed to GitHub.
Used python-dotenv to load environment variables.
Features
Multi-turn chatbot
ChatAgent class
Model selection
/reset command
/tokens command
Rolling memory buffer
Exit command
PROBLEM I FACED:

Initially, python-dotenv was not installed, which caused import errors.
Some OpenRouter models returned 404 errors because the model name was unavailable or outdated.
Several free models returned 429 rate-limit errors, so I had to test different models before finding one that worked reliably.
I accidentally ran the project with a different Python installation, which caused package-related errors.
I faced indentation errors while modifying the chatbot loop and adding new commands.
Git was not installed/configured initially, which prevented me from creating a repository and pushing my code to GitHub.