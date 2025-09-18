# Django ChatterBot Terminal Chat Client

**MSCS-633 Assignment 3**  
A conversational AI chatbot built with Django and ChatterBot for terminal-based interactions.

## Project Overview

This project implements a machine learning-powered chatbot that can engage in natural conversations through a terminal interface. The bot uses Django for database management and ChatterBot for AI conversation capabilities.

## Files

- `chat_terminal.py` - Main application with Django ChatterBot integration
- `requirements.txt` - Python dependencies
- `chatbot.db` - SQLite database for conversation storage
- `README.md` - This documentation

## Requirements

- Python 3.8+
- Django 5.2.6
- ChatterBot 1.2.3
- spaCy NLP library

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the chatbot:
```bash
python3 chat_terminal.py
```

## Usage

The bot will train itself on startup and then present an interactive chat interface:

```
Django ChatterBot Terminal Chat Client
Let's have a natural conversation!
Type 'quit' to exit
--------------------------------------------------
user: Good morning! How are you doing?
bot: I am doing very well, thank you for asking.
user: quit
bot: Thanks for the great conversation! Goodbye!
```

## Features

- **Natural Conversations**: Trained with conversational pairs for flowing dialogue
- **Django Integration**: Uses Django ORM for database management
- **Machine Learning**: ChatterBot AI for intelligent responses
- **Assignment Compliance**: Meets MSCS-633 requirements
- **Clean Terminal Interface**: Simple, user-friendly chat experience

## Assignment Requirements Met

Django framework integration  
ChatterBot conversation engine  
Terminal-based chat interface  
Proper conversation flow  
Required example conversation supported

## Technical Details

- **Database**: SQLite with Django ORM
- **AI Engine**: ChatterBot with BestMatch logic adapter
- **Training**: Custom conversational pairs + contextual responses
- **Interface**: Command-line terminal chat loop
