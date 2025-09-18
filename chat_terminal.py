#!/usr/bin/env python3
"""
Django ChatterBot Terminal Chat Client
Simple terminal chat using Django and ChatterBot
"""

import os
import sys
import django
from django.conf import settings

# Configure Django
if not settings.configured:
    settings.configure(
        DEBUG=True,
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(os.path.dirname(__file__), 'chatbot.db'),
            }
        },
        INSTALLED_APPS=[
            'django.contrib.contenttypes',
            'django.contrib.auth',
        ],
        USE_TZ=True,
        SECRET_KEY='django-secret-key-for-chatbot',
    )

django.setup()

# Import ChatterBot
try:
    from chatterbot import ChatBot
    from chatterbot.trainers import ListTrainer
except ImportError:
    print("ChatterBot not installed. Run: pip install -r requirements.txt")
    sys.exit(1)


class SimpleChatBot:
    def __init__(self):
        # Create the bot with better configuration for conversations
        self.bot = ChatBot(
            'SimpleBot',
            storage_adapter='chatterbot.storage.SQLStorageAdapter',
            database_uri='sqlite:///chatbot.db',
            logic_adapters=[
                {
                    'import_path': 'chatterbot.logic.BestMatch',
                    'default_response': 'I am still learning. Can you tell me more?',
                    'maximum_similarity_threshold': 0.90
                },
                'chatterbot.logic.MathematicalEvaluation',
            ]
        )
        
        # Train the bot with conversational pairs
        print("Training bot for natural conversations...")
        list_trainer = ListTrainer(self.bot)
        
        # Train with conversational pairs (question-answer format)
        conversations = [
            # Assignment required conversation
            ["Good morning! How are you doing?", "I am doing very well, thank you for asking."],
            ["You're welcome.", "Do you like hats?"],
            
            # Natural greeting conversations
            ["Hi", "Hello! How are you today?"],
            ["Hello", "Hi there! How can I help you?"],
            ["Hey", "Hey! What's up?"],
            ["How are you?", "I'm doing great, thanks for asking! How about you?"],
            ["I'm good", "That's wonderful to hear! What brings you here today?"],
            ["I'm fine", "Glad to hear that! Is there anything you'd like to chat about?"],
            
            # About the bot
            ["What's your name?", "I'm a ChatterBot. You can call me Bot. What's your name?"],
            ["My name is John", "Nice to meet you, John! How can I help you today?"],
            ["What can you do?", "I can chat with you about various topics. What would you like to talk about?"],
            ["Tell me about yourself", "I'm an AI chatbot built with Python and Django. I love having conversations!"],
            
            # Common responses
            ["Thank you", "You're very welcome! Happy to help!"],
            ["Thanks", "No problem at all! Anything else I can help with?"],
            ["Yes", "Great! Tell me more."],
            ["No", "Okay, no worries. Is there something else you'd like to discuss?"],
            
            # Questions about AI/Technology
            ["What is AI?", "AI stands for Artificial Intelligence. It's technology that can think and learn like humans."],
            ["How do you work?", "I use machine learning to understand your messages and find the best responses."],
            ["Are you smart?", "I'm learning every day! The more we chat, the better I get at conversations."],
            
            # Casual conversation
            ["What do you like?", "I enjoy having interesting conversations with people like you!"],
            ["Do you have hobbies?", "I love chatting and learning new things from people. What about you?"],
            ["What's the weather like?", "I can't check the weather, but I hope it's nice where you are!"],
            
            # Follow-up questions to keep conversation going
            ["That's interesting", "I'm glad you think so! What else would you like to know?"],
            ["Cool", "Right? What else is on your mind?"],
            ["Okay", "Is there anything specific you'd like to talk about?"],
            
            # Ending conversation
            ["Goodbye", "Goodbye! It was great chatting with you!"],
            ["Bye", "See you later! Have a wonderful day!"],
            ["See you later", "Take care! Come back anytime for another chat!"],
        ]
        
        # Train with each conversation pair
        for conversation in conversations:
            list_trainer.train(conversation)
        
        print("Training complete! Ready for natural conversations!")
    
    def get_contextual_response(self, user_input):
        """Get a more contextual response by checking common patterns"""
        user_lower = user_input.lower().strip()
        
        # Handle common patterns for better conversation flow
        if any(greeting in user_lower for greeting in ['hi', 'hello', 'hey']):
            if not hasattr(self, 'greeted'):
                self.greeted = True
                return "Hello! Nice to meet you! How are you doing today?"
        
        if any(word in user_lower for word in ['good', 'fine', 'well', 'great']):
            if 'how are you' in self.last_response.lower() if hasattr(self, 'last_response') else False:
                return "That's wonderful! What would you like to chat about?"
        
        # Get normal ChatterBot response
        response = self.bot.get_response(user_input)
        self.last_response = str(response)
        return str(response)
    
    def chat(self):
        print("Django ChatterBot Terminal Chat Client")
        print("Let's have a natural conversation!")
        print("Type 'quit' to exit")
        print("-" * 50)
        
        while True:
            try:
                user_input = input("user: ").strip()
                
                if user_input.lower() in ['quit', 'exit', 'bye', 'goodbye']:
                    print("bot: Thanks for the great conversation! Goodbye!")
                    break
                
                if user_input:
                    response = self.get_contextual_response(user_input)
                    print(f"bot: {response}")
                    
            except KeyboardInterrupt:
                print("\nbot: Thanks for chatting! Goodbye!")
                break
            except EOFError:
                print("\nbot: Take care!")
                break


def main():
    try:
        chatbot = SimpleChatBot()
        chatbot.chat()
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
