import json
from langchain_core.prompts import PromptTemplate

from HyperPersonalization.backend.app import get_recommendation
from llm_helper import llm
from prompt_template import template


def get_recommendations(user_data):
    """Reads user data from a JSON file and returns recommendation data."""
    print("response::::", user_data)
    print(type(user_data))
    #with open(file_path, encoding="utf-8", errors="ignore") as file:
    posts = json.loads(user_data)
    print("response::::", posts)
    # Extract user details
    customer_type = posts["user"]["customer_type"]
    details = posts["user"]

    # Extract social media insights
    sentiment = [post["sentiment"] for post in posts["socialMediaProfile"]]
    intent = [post["intent"] for post in posts["socialMediaProfile"]]
    timestamp = [post["time_stamp"] for post in posts["socialMediaProfile"]]

    # Extract transaction history
    transaction_type = [post["transaction_type"] for post in posts["transactionProfile"]]
    category = [post["category"] for post in posts["transactionProfile"]]
    amount = [post["amount"] for post in posts["transactionProfile"]]
    purchase_date = [post["purchase_date"] for post in posts["transactionProfile"]]
    payment_mode = [post["payment_mode"] for post in posts["transactionProfile"]]

    # Create prompt template and chain
    pt = PromptTemplate.from_template(template)
    chain = pt | llm

    # Invoke the chain with user data
    response = chain.invoke(
        input={
            "customer_type": customer_type,
            "details": details,
            "sentiment": sentiment,
            "intent": intent,
            "timestamp": timestamp,
            "transaction_type": transaction_type,
            "category": category,
            "amount": amount,
            "purchase_date": purchase_date,
            "payment_mode": payment_mode,
        }
    )

    # Clean and parse the recommendation response
    recommendation = response.content.replace("```json", "").replace("```", "").strip()

    try:
        recommendation_data = json.loads(recommendation)
    except json.JSONDecodeError:
        recommendation_data = {"error": "Invalid JSON response from LLM"}

    return recommendation_data


# Example usage
if __name__ == "__main__":
    result = get_recommendation()
    print(result)
