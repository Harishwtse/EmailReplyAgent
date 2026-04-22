# ReplyGeniAI Email Agent

ReplyGeniAI Email Agent is an AI-powered email response generator that automatically detects customer intent and creates professional replies using Generative AI.

This project helps customer support teams respond faster with consistent, empathetic, and professional communication.

---

## Features

- Detects customer intent automatically  
  - Complaint  
  - Refund Request  
  - Payment Issue  
  - Technical Issue  
  - Product Support  
  - General Inquiry  

- Generates smart email replies

- Tone customization:
  - Empathetic  
  - Professional  
  - Friendly  
  - Formal  
  - Apologetic  

- Uses Generative AI for contextual responses

- FastAPI backend support

- Clean UI with Streamlit

---

## Example Input

### Customer Email

Hi, I purchased a laptop, currently it is not working.

Hello I am Harish, My amount was not credited to my account.

---

## Detected Intent

Complaint

---

## Selected Tone

Empathetic and Professional

---

## Generated Reply

**Subject:** Re: Amount Not Credited to Your Account

Dear Harish,

Thank you for reaching out to us regarding the issue with your account. We apologize for the inconvenience this has caused and are here to assist you.

To resolve this issue, could you please provide us with your account number and the date of the transaction that was supposed to be credited to your account? This information will enable us to look into the matter further and process the payment as soon as possible.

We appreciate your patience and cooperation in this matter. We will respond to you as soon as we have an update.

Thank you for choosing our services.

Best regards,  
Customer Support Team

---

## Tech Stack

- Python  
- Streamlit  
- FastAPI  
- Open Source LLM / Groq / Llama Models  
- Prompt Engineering  
- NLP Intent Detection  

---

## Project Structure

```bash
ReplyGeniAI/
│── app.py
│── backend.py
│── utils.py
│── requirements.txt
│── .env
│── README.md
