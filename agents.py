from google import genai
from config import GOOGLE_API_KEY

client = genai.Client(api_key=GOOGLE_API_KEY)

MODEL = "gemini-3.6-flash"


def intent_agent(user_input: str) -> str:
    prompt = f"""
You are MITRA's Intent Agent.

Identify what the user is trying to accomplish.

Return only:
Intent: <short intent>
Goal: <short goal>

User request:
{user_input}
"""

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt
    )

    return response.text.strip()

def planner_agent(intent: str) -> str:
    prompt = f"""
You are MITRA's Planner Agent.

Create a simple plan to address the user's request.

Return only a numbered list of 3 to 5 steps.

User intent:
{intent}
"""

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt
    )

    return response.text.strip()


def response_agent(user_input: str, intent: str, plan: str) -> str:
    prompt = f"""
You are MITRA's Response Agent.

Give the user a clear, practical and helpful answer.

User request:
{user_input}

Intent:
{intent}

Plan:
{plan}

Write the final answer in a simple and natural way.
"""

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt
    )

    return response.text.strip()


def review_agent(answer: str) -> str:
    prompt = f"""
You are MITRA's Review Agent.

Review the following answer for:
1. Relevance
2. Clarity
3. Safety
4. Obvious factual problems

Return only:
PASS
or
REVISE: <brief reason>

Answer:
{answer}
"""

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt
    )

    return response.text.strip()