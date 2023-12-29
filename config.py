# config.py

# Importing required libraries
import os

# Function to load OpenAI API key
def load_openai_key():
    try:
        with open('openai_key.txt', 'r') as file:
            openai_key = file.read().strip()
        return openai_key
    except FileNotFoundError:
        print("openai_key.txt file not found. Please ensure the file exists and try again.")
        return None

# Setting OpenAI API key
OPENAI_API_KEY = load_openai_key()
