import json
import pandas as pd

# Load CSV files
df_customers = pd.read_csv('customer_data.csv')
df_social = pd.read_csv('social_media.csv')
df_transactions = pd.read_csv('transaction.csv')

# Function to safely convert values
def safe_int(value, default=0):
    try:
        return int(float(value))  # Handle both float and int values
    except (ValueError, TypeError):
        return default  # Return default if conversion fails

def safe_str(value, default=""):
    return str(value) if pd.notna(value) else default

def safe_list(value, default=[]):
    try:
        return eval(value) if pd.notna(value) else default
    except:
        return default

# Fetch User Details
def fetch_user_details_by_userName(userName):
    if userName in df_customers['userName'].values:
        # Fetch user details
        user_row = df_customers[df_customers['userName'] == userName].iloc[0]

        user_data = {
            "user": {
                "userName": safe_str(user_row['userName']),
                "name": safe_str(user_row['name']),
                "customer_type": safe_str(user_row['customerType']),
                "age": safe_int(user_row['age']),
                "gender": safe_str(user_row['gender']),
                "location": safe_str(user_row['location']),
                "interests": safe_list(user_row['interests']),
                "preferences": safe_list(user_row['preferences']),
                "annualIncome": safe_int(user_row['annualIncome']),
                "education": safe_str(user_row['education']),
                "occupation": safe_str(user_row['occupation']),
                "industry": safe_str(user_row.get('industry', "")),
                "revenue": safe_int(user_row.get('revenue', 0)),
                "financial_needs": safe_str(user_row.get('financialNeeds', "")),
                "employee_count": safe_int(user_row.get('employeeCount', 0))
            },
            "socialMediaProfile": [],
            "transactionProfile": []
        }

        # Fetch social media posts
        social_media_rows = df_social[df_social['userName'] == userName]
        for _, row in social_media_rows.iterrows():
            user_data["socialMediaProfile"].append({
                "postId": safe_int(row['postId']),
                "platform": safe_str(row['socialMediaPlatform']),
                "intent": safe_str(row['intent']),
                "sentiment": safe_str(row.get('sentimentScore', "")),
                "content": safe_str(row['socialMediaContent']),
                "time_stamp": safe_str(row['timeStamp'])
            })

        # Fetch transactions
        transaction_rows = df_transactions[df_transactions['userName'] == userName]
        for _, row in transaction_rows.iterrows():
            user_data["transactionProfile"].append({
                "productId": safe_int(row['productId']),
                "transaction_type": safe_str(row['transactionType']),
                "amount": safe_int(row['amount']),
                "category": safe_str(row.get('category', "")),
                "purchase_date": safe_str(row.get('purchaseDate', "")),
                "payment_mode": safe_str(row.get('paymentMode', ""))
            })

        return json.dumps(user_data, indent=4)

    else:
        return json.dumps({"error": "User not found"})

# Example Usage
userName_to_search = 'ORG_US_007'
user = fetch_user_details_by_userName(userName_to_search)
print(user)
