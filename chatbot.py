import re

# Basic text preprocessing (optional)
def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    return text

# Rule-based responses
def get_response(user_input):
    user_input = preprocess(user_input)

    # Define a dictionary of rules
    responses = {
        "hello": "Hi there! How can I help you about Tamizhan Skills courses?",
        "hi": "Hello! Ask me anything about Tamizhan Skills.",
        "courses": "Tamizhan Skills offers courses in Python, Web Development, AI, and more.",
        "timing": "Courses are usually conducted in the evening, from 6 PM to 8 PM.",
        "fees": "Fees vary depending on the course. Basic courses start at ₹999.",
        "certificate": "Yes, you will get a certificate after successful completion.",
        "location": "Tamizhan Skills is located in Tamil Nadu and also offers online classes.",
        "thank you": "You're welcome!",
        "bye": "Goodbye! Have a great day!"
    }

    # Match user input with rules
    for key in responses:
        if key in user_input:
            return responses[key]

    return "Sorry, I didn't understand that. Can you please rephrase?"

# Chat loop
def chat():
    print("Welcome to Tamizhan Skills Chatbot! (type 'exit' to quit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Bye! Take care.")
            break
        response = get_response(user_input)
        print("Chatbot:", response)

# Run the chatbot
if __name__ == "__main__":
    chat()
