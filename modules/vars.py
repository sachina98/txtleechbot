import os

API_ID    = os.environ.get("28174664", "")
API_HASH  = os.environ.get("f504bf34ad7dbc597c8802db2f46453c", "")
BOT_TOKEN = os.environ.get("7619482400:AAFGp5-uBHKUAi8Q3XE6JDl40w9HtLdAKL4", "") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
