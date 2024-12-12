Project Setup and Execution Guide

This document provides step-by-step instructions to set up and run the project.

1. Create a Virtual Environment

To isolate the project dependencies, create a virtual environment using Conda:

conda create -p venv python=3.10 -y

2. Set Up Groq API

Create an account on Groq.

Obtain your API key from Groq's dashboard.

Create a .env file in the project directory and add the following line:

GROQ_API_KEY=your_api_key_here

Replace your_api_key_here with your actual Groq API key.

3. Install Required Dependencies

Install the necessary Python packages by running:

pip install -r requirements.txt

4. Run the SQLite Script

To set up the SQLite database and populate it with initial data, execute:

python sqlite.py

5. Run the Streamlit Application

Launch the Streamlit application to interact with the database:

streamlit run app.py

Summary

This project leverages a SQLite database and Groq API for querying data through a Streamlit interface. Ensure that all prerequisites are fulfilled and environment variables are correctly set to avoid errors.

Enjoy exploring the application!
