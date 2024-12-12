# Project Setup and Execution Guide

This document provides step-by-step instructions to set up and run the project.

## Installation

**1. Create a Virtual Environment**

To isolate the project dependencies, create a virtual environment using Conda:

```bash
conda create -p venv python=3.10 -y
```

**2. Set Up Groq API**

**A.** Create an account on Groq. Obtain your API key from Groq's dashboard.

**B.** Create a .env file in the project directory and add the following line:

```bash
GROQ_API_KEY=your_api_key_here
```

**C.** Replace your_api_key_here with your actual Groq API key.

**3. Install Required Dependencies**

Install the necessary Python packages by running:

```bash
pip install -r requirements.txt
```

**4. Run the SQLite Script**

To set up the SQLite database and populate it with initial data, execute:

```bash
python sqlite.py
```
**5. Run the Streamlit Application**

Launch the Streamlit application to interact with the database:

```bash
streamlit run app.py
```
