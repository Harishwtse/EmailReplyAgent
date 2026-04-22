import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Load Env
load_dotenv()

# Load LLM
llm = ChatGroq(
    groq_api_key = os.getenv("GROQ_API_KEY"),
    model_name = "llama-3.1-8b-instant"
)

# ----------------------------------
# Intent Agent
#-----------------------------------

def intent_agent(email):
    prompt = f"""
    Read the email and classify into one category:
    Complaint / refund / meeting / inquiry/ support

    Email:
    {email}

    Give only category name.
    """
    return llm.invoke(prompt).content.strip()


# ---------------------------------------------------
# Tone Agent
# ---------------------------------------------------

def tone_agent(Intent):
    if Intent == "Complaint":
        return "Empathetic and professional"
    elif Intent == "Refund":
        return "Polite and Helpful"
    elif Intent == "Meeting":
        return "Formal and Clear"
    else:
        return "Professional"
    
# --------------------------------------------
# Reply Agent
# --------------------------------------------

def reply_agent(email, Intent, tone):
    prompt = f""" 
    You are a smart customer support assistant

    Email:
    {email}

    Intent: {Intent}
    Tone: {tone}

    Write a professional short email reply.
    """

    return llm.invoke(prompt).content.strip()

#--------------------------------------------------
# Main Workflow
#--------------------------------------------------

def run_agents(email):
    intent = intent_agent(email)
    tone = tone_agent(intent)
    reply = reply_agent(email, intent, tone)

    return{
        "intent" : intent,
        "tone": tone,
        "reply" : reply
    }
