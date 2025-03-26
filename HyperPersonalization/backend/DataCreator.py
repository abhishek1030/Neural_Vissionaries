import string
import pandas as pd
from faker import Faker
import random

# Initialize Faker
token_generator = Faker()


def generate_alphanumeric():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))


# Sample data lists
interests = [
    "Luxury Shopping", "Travel", "Dining", "Budget Shopping", "Mortgage Payments",
    "Flights", "Hotels", "Adventure Activities", "Cameras", "Family Vacations",
    "Kids", "Education", "Home Essentials", "Professional Development", "Healthcare"
]

preferences = [
    "Discounts", "New Arrivals", "Home Loan", "Retirement Saving", "ETFs",
    "Travel Credit Cards", "Digital Banking", "International Insurance", "Family Insurance",
    "Mortgage", "Savings Accounts", "Health Insurance", "Gym Subscription"
]

sentiments = [
    "Navigating fluctuations raw material prices!! Cash Flow planning is KEY!",
    "Loving the new fashion trends this season!",
    "Just finished a 5K run! Need new running shoes. Any suggestions?",
    "Need to start saving more. Thinking of opening a deposit account",
    "Struggling to stick to my budget this month.",
    "Looking for sustainable finance options to increase eco-friendly fabric sourcing!!",
    "Excited about the new wealth management strategies.",
    "Switching to a new payroll system. Any recommendation for banking integration?",
]

paymentMode = [
    "Credit Card", "Wire Transfer", "Amex Platinum", "Auto Debit", "Net Banking"
    "Debit Card", "Business Loan", "Ach Debit", "Corporate Credit Card", "Bank Wire"
]

transactionType = [
    "Credit Card", "Wire Transfer", "Amex Platinum", "Auto Debit", "Net Banking"
    "Debit Card", "Business Loan", "Ach Debit", "Corporate Credit Card", "Bank Wire"
]


# Generate data lists
customer_data = []
social_media_data = []
transaction_data = []

for _ in range(100):
    user_id = token_generator.uuid4()
    user_name = generate_alphanumeric()

    # Customer Data
    customer_data.append({
        "userName": user_name,
        "customerType": "Individual",
        "customerId": user_id,
        "name": token_generator.name(),
        "age": random.randint(18, 80),
        "gender": random.choice(["M", "F"]),
        "location": token_generator.city(),
        "interests": random.sample(interests, 3),
        "preferences": random.sample(preferences, 3),
        "annualIncome": random.randint(0, 10000000),
        "education": random.choice(["High School", "Bachelor", "Master", "PhD"]),
        "occupation": token_generator.job(),
    })

    # Social Media Data
    social_media_data.append({
        "userName": user_name,
        "postId": random.randint(101, 10000001),
        "socialMediaPlatform": random.choice(["Twitter", "Facebook", "Instagram", "LinkedIn", "Reddit"]),
        "socialMediaContent": random.choice(sentiments),
        "socialMediaTimeStamp": token_generator.time(),
    })

    # Transaction Data
    transaction_data.append({
        "userName": user_name,
        "productId": random.randint(21, 200001),
        #"transactionType": row['transactionType'],
        "amount": random.randint(30, 80000),
        #"category": row['category'],
        "purchase_date": token_generator.time(),
        "payment_mode": random.choice(paymentMode)
    })

# Convert lists to DataFrames
customer_df = pd.DataFrame(customer_data)
social_media_df = pd.DataFrame(social_media_data)
transaction_df = pd.DataFrame(transaction_data)

# Save to CSV files
customer_df.to_csv("customer_data.csv", index=False)
social_media_df.to_csv("social_media.csv", index=False)
transaction_df.to_csv("transaction.csv", index=False)

print("CSV files successfully created!")
