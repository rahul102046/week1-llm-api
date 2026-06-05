import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ["OPENROUTER_API_KEY"],
)


class ChatAgent:

    def __init__(
        self,
        client,
        model,
        system_prompt="You are a helpful assistant.",
        max_turns=5
    ):
        self.client = client
        self.model = model
        self.max_turns = max_turns
        self.last_usage = None

        self.messages = [
            {
                "role": "system",
                "content": system_prompt
            }
        ]

    def chat(self, user_message):

        self.messages.append(
            {
                "role": "user",
                "content": user_message
            }
        )

        response = self.client.chat.completions.create(
            model=self.model,
            messages=self.messages
        )

        self.last_usage = response.usage

        reply = response.choices[0].message.content

        self.messages.append(
            {
                "role": "assistant",
                "content": reply
            }
        )

        self.trim_history()

        return reply

    def trim_history(self):

        max_messages = self.max_turns * 2

        conversation = self.messages[1:]

        if len(conversation) > max_messages:
            self.messages = [
                self.messages[0]
            ] + conversation[-max_messages:]

    def reset(self):

        system_message = self.messages[0]

        self.messages = [system_message]

    def show_tokens(self):

        if self.last_usage:
            print("\nTOKEN USAGE:")
            print(self.last_usage)
        else:
            print("No API call made yet.")


def choose_model():

    models = {
        "1": "nvidia/nemotron-3-ultra-550b-a55b:free",
        "2": "moonshotai/kimi-k2.6:free"
    }

    print("\nChoose a model:\n")

    for key, value in models.items():
        print(f"{key}. {value}")

    while True:

        choice = input("\nEnter choice: ")

        if choice in models:
            return models[choice]

        print("Invalid choice. Try again.")


def run_chatbot():

    model = choose_model()

    print(f"\nUsing model: {model}")

    agent = ChatAgent(
        client=client,
        model=model,
        system_prompt="You are a helpful assistant.",
        max_turns=5
    )

    print("\nChat started.")
    print("Commands:")
    print("/reset")
    print("/tokens")
    print("exit\n")

    while True:

        user_input = input("[YOU] ")

        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        if user_input == "/reset":
            agent.reset()
            print("History cleared.")
            continue

        if user_input == "/tokens":
            agent.show_tokens()
            continue

        try:

            reply = agent.chat(user_input)

            print(f"\n[MODEL] {reply}\n")

        except Exception as e:

            print("\nERROR:")
            print(e)


if __name__ == "__main__":
    run_chatbot()