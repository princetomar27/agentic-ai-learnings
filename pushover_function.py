from dotenv import load_dotenv
from openai import OpenAI
import json
import os
import requests
from pypdf import PdfReader
import gradio as gr

load_dotenv(override=True)
openAI = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

pushover_user = os.getenv("PUSHOVER_USER")
pushover_token = os.getenv("PUSHOVER_TOKEN")

def pushNotificationToUser(message):
    print(f"Sending notification to user ${message}")
    payload = {
        "user": pushover_user,
        "token": pushover_token,
        "message": message
    }

    requests.post(os.getenv("PUSHOVER_URL"), data=payload)

pushNotificationToUser("Hey Prince !")
