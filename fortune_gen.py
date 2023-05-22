import random

fortunes = [
    "A smile is your passport into the hearts of others.",
    "A dream you have will come true.",
    "You will become great if you believe in yourself.",
    "Adventure can be real happiness.",
    "All will go well with your new project.",
    "You are very talented in many ways.",
    "Your hard work will pay off soon.",
    "You are kind-hearted and always help others.",
    "The best way to predict the future is to create it.",
    "You will find joy in unexpected places."
]

def generate_fortune():
    return random.choice(fortunes)

print("Welcome to the Fortune Generator!")
print("Here's your fortune for today:")
print(generate_fortune())
