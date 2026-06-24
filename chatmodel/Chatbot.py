from dotenv import load_dotenv

load_dotenv()
from langchain_mistralai import ChatMistralAI

messages = []

print("__________________welcome! type 0 to exit this app______________")

# a while loop is beacuse we can continue talking until user press 0 to exit this app
while True:
    prompt = input("YOU: ")
    messages.append(prompt)
    if prompt == "0":
        break
    model = ChatMistralAI(model="mistral-small-2603")
    res = model.invoke(messages)
    messages.append(res.content)
    print("BOT:", res.content)
    print(messages)
