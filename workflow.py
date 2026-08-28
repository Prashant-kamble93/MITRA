from agents import (
    intent_agent,
    planner_agent,
    response_agent,
    review_agent,
)


def run_mitra(user_input: str) -> dict:
    try:
        if not user_input or not user_input.strip():
            return {
                "success": False,
                "answer": "Please enter a question.",
                "error": None,
            }

        intent = intent_agent(user_input)
        plan = planner_agent(intent)
        answer = response_agent(user_input, intent, plan)
        review = review_agent(answer)

        return {
            "success": True,
            "intent": intent,
            "plan": plan,
            "answer": answer,
            "review": review,
            "error": None,
        }

    except Exception as exc:
        return {
            "success": False,
            "answer": "Sorry, MITRA could not process your request. Please try again.",
            "error": str(exc),
        }