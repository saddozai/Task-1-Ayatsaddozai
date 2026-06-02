#importing libraries
import random
import re 
chatdic= {
    "greeting": {
        "patterns": [
            "hello", "hi", "hey",
            "good morning",
            "good evening"
        ],
        "responses": [
            "Hello! How can I help you today?",
            "Hi there! Welcome to DecodeLabs chatbot.",
            
            "Hey! What would you like assistance with?"
        ]
    },

    "goodbye": {
        "patterns": [
            "bye", "goodbye", "see you",
            "take care"
        ],
        "responses": [
            "Goodbye! Have a great day.",
            "Take care.",
            
            "See you again soon."
        ]
    },

    "thanks": {
        "patterns": [
            "thanks", "thank you",
            "thx", "appreciate"
        ],
        "responses": [
            "You're welcome.",
            "Happy to help.",
            "My pleasure.",
            "Glad I could assist."
        ]
    },

    "help": {
        "patterns": [
            "help", "assist", "support",
            "guide", "explain"
        ],
        "responses": [
            "Sure! Tell me what you need help with.",
            "I am here to assist you.",
            "Please explain your issue."
        ]
    },

    "weather": {
        "patterns": [
            "weather", "temperature",
            "forecast", "rain"
        ],
        "responses": [
            "The weather seems pleasant today.",
            "Please check online weather services for live updates.",
            "It might be sunny today."
        ]
    },

    "time": {
        "patterns": [
            "time", "date",
            "today", "day"
        ],
        "responses": [
            "You can check your system clock for the current time.",
            "Today's date is available on your device.",
            "Current date and time are system generated."
        ]
    },

    "courses": {
        "patterns": [
            "course", "training",
            "internship", "classes"
        ],
        "responses": [
            "DecodeLabs offers technical training programs.",
            "Internship opportunities are available in AI and development.",
            "Various IT and AI courses are offered."
        ]
    },

    "complaint": {
        "patterns": [
            "problem", "issue",
            "bug", "not working"
        ],
        "responses": [
            "I am sorry for the inconvenience.",
            "Please explain the issue in detail.",
            "Our support team will look into this."
        ]
    }
}

fallbackresponses = [
    "Sorry, I didn't understand that.",
    "Can you please rephrase your question?",
    "I am still learning. Try asking differently.",
    "Sorry, I could not recognize your request."
]
#function
def get_response(user_msg):
  user_msg=user_msg.lower().strip()
  user_msg=re.sub(r"\s+"," ",user_msg)
  for intent, data in chatdic.items():
    for pattern in data ["patterns"]:
      if pattern in user_msg:
        return random.choice(data["responses"])
  return random.choice(fallbackresponses)
print("WELCOME TO DecodeLabs CHATBOT SERVICE")
print("Type Done anytime to close the chat")
while True:
    user_input= input("You:")
    user_input=user_input.lower().strip()
    if user_input in ["exit", "quit", "bye"]:

      print("\nBot: Goodbye! Thank you for using DecodeLabs Chatbot.")
      break
    chatbot_resp= get_response(user_input)
    print(f"Bot:{chatbot_resp}")