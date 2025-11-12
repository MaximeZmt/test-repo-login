from auth.parser import evaluate_expression
from .storage import InMemoryStorage

HELP = """
Here are the following command available:
- quit: quits the program
- login: login
- signin: sign in
"""


def start_cli() -> None:
    """Start a simple CLI for the Auth API."""
    print("=== Simple Auth API ===")
    print("Type 'help' for help.")
    print("Type 'quit' to exit.\n")

    # Init memory for the App
    memory = InMemoryStorage()

    while True:
        expr = input(">> ").strip()

        if expr.lower() == "quit":
            print("Goodbye!")
            break

        if expr.lower() == "help":
            print(HELP)
            continue

        try:
            result = evaluate_expression(memory, expr)
            print(result)
        except Exception as e:
            print("Error:", e)