import os
from dotenv import load_dotenv
import json


load_dotenv()

ILO_IP = os.getenv("ILO_IP")
ILO_SSH_PORT = os.getenv("ILO_SSH_PORT")
ILO_WEB_PANEL = f"https://{ILO_IP}"

ILO_LOGIN = os.getenv("ILO_LOGIN")
ILO_PASSWORD = os.getenv("ILO_PASSWORD")

with open("config.conf") as file:
    JSON_DATA = json.load(file)
