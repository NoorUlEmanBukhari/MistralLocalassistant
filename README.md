# Mistral Local Assistant

A fully offline AI chatbot interface built using the **Mistral 7B Instruct** model and **Gradio**. This project demonstrates how to run and interact with a local LLM in a user-friendly web interface — no internet or APIs required.

## Features

- Runs **entirely on your local machine**
- Integrates **Mistral 7B Instruct** (.gguf model) using `llama-cpp-python`
- Clean and customizable **Gradio interface**
- No external dependencies or API keys needed
- Supports contextual conversations using a memory-style chat format

## Setup Instructions

1. **Clone the repository**:
 git clone https://github.com/NoorUlEmanBukhari/mistral-local-assistant.git
 cd mistral-local-assistant

 ## Create and activate Virtual environment 
 python -m venv venv
 venv\Scripts\activate   # On Windows


## Run the App
python gradio_app.py

