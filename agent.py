def tool_hello():
    return "Hello from agent"

def tool_price():
    return "Cardamom price is 1200 (mock data)"

def tool_help():
    return "Commands: hello, price, help, exit"

def agent(task):
    task = task.lower()

    if "hello" in task:
        return tool_hello()

    if "price" in task:
        return tool_price()

    if "help" in task:
        return tool_help()

    return "I don't understand. Type help."

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Agent: bye")
        break

    result = agent(user_input)
    print("Agent:", result)