import json
import pandas as pd

#Read the csv file
df = pd.read_csv('customer_data.csv')

#Fetch Data
def fetch_user_details_by_userName(userName):
    if userName in df['userName'].values:
        user_row = df[df['userName'] == userName].iloc[0]
        user_data = {
            "user": {
                "userName": user_row['userName'],
                "name": user_row['name'],
                "age": int(user_row['age']),
                "gender": user_row['gender'],
                "location": user_row['location'],
                "interests": user_row['interests'],
                "preferences": user_row['preferences'],
                "annualIncome": int(user_row['annualIncome']),
                "education": user_row['education'],
                "occupation": user_row['occupation']
            },
            "socialMediaProfile": {
                "postId": int(user_row['postId']),
                "socialMediaPlatform": user_row['socialMediaPlatform'],
                "socialMediaContent": user_row['socialMediaContent'],
                "socialMediaTimeStamp": user_row['socialMediaTimeStamp']
            },
            "transactionProfile": {
                "productId": int(user_row['productId']),
                "purchaseHistory": user_row['purchaseHistory']
            }
        }
        return json.dumps(user_data, indent=4)
    else:
        return json.dumps({"error":"User not found"})

#Example
userName_to_search = 'dvEjuE'
user = fetch_user_details_by_userName(userName_to_search)
print(user)
