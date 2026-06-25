# from dotenv import load_dotenv

# load_dotenv()
# from langchain_mistralai import ChatMistralAI

# messages = []

# print("__________________welcome! type 0 to exit this app______________")

# # a while loop is beacuse we can continue talking until user press 0 to exit this app
# # two issues are here 1st Short term memory 2nd Large context window and no roles are defined here
# while True:
#     prompt = input("YOU: ")
#     messages.append(prompt)
#     if prompt == "0":
#         break
#     model = ChatMistralAI(model="mistral-small-2603")
#     res = model.invoke(messages)
#     messages.append(res.content)
#     print("BOT:", res.content)
#     print(messages)


################################################################################

# from dotenv import load_dotenv

# load_dotenv()
# from langchain_mistralai import ChatMistralAI
# from langchain.messages import HumanMessage, AIMessage, SystemMessage

# messages = [
#     SystemMessage(content="You are a funny and witty AI assistant!"),
# ]

# print("__________________welcome! type 0 to exit this app______________")

# # a while loop is beacuse we can continue talking until user press 0 to exit this app
# # We are defining the roles here --> AI model
# while True:
#     prompt = input("YOU: ")
#     messages.append(HumanMessage(content=prompt))
#     if prompt == "0":
#         break
#     model = ChatMistralAI(model="mistral-small-2603")
#     res = model.invoke(messages)
#     messages.append(AIMessage(content=res.content))
#     print("BOT:", res.content)
#     print(messages)


################################################################################

from dotenv import load_dotenv

load_dotenv()
from langchain_mistralai import ChatMistralAI
from langchain.messages import HumanMessage, AIMessage, SystemMessage


print("__________________welcome! type 0 to exit this app______________")
print("1. Funny")
print("2. Angry")
print("3. Sarcastic")
print("4. Sad")
print("5. Romantic")

personalities = {
    "1": "You are a funny and witty AI assistant!",
    "2": "You are an angry and aggressive AI assistant!",
    "3": "You are a sarcastic and witty AI assistant!",
    "4": "You are a sad and depressed AI assistant!",
    "5": "You are a romantic and loving AI assistant!",
}

choice = input("\n Choose personality(1-5):")
if choice not in personalities:
    print("Invalid Choice")
    exit()

messages = [
    SystemMessage(content=personalities[choice]),
]

# a while loop is beacuse we can continue talking until user press 0 to exit this app
# We are defining the roles here --> AI model as well as we are giving the choice of mood the ai will have(behaviour)
while True:
    prompt = input("YOU: ")
    messages.append(HumanMessage(content=prompt))
    if prompt == "0":
        break
    model = ChatMistralAI(model="mistral-small-2603")
    res = model.invoke(messages)
    messages.append(AIMessage(content=res.content))
    print("BOT:", res.content)
    print(messages)
