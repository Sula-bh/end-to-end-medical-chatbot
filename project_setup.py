import logging
import os
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="[%(asctime)s]: %(message)s:")


list_of_files = [
    "src/med_chatbot/__init__.py",
    "src/med_chatbot/helper.py",
    "src/med_chatbot/prompt.py",
    "src/med_chatbot/logger.py",
    ".env",
    "setup.py",
    "notebooks/experiment.ipynb",
    "app.py",
    "store_index.py",
    "data/.gitkeep",
    "static/.gitkeep",
    "templates/chat.html",
    "requirements.txt",
    "README.md",
    ".gitignore",
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "" and not os.path.exists(filedir):
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file {filename}")

    if not os.path.exists(filepath):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} is already created")
