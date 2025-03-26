import string

import pandas as pd
from faker import Faker
import random

# Generate fake data
fake = Faker()
users = []

interests = [
    "Luxury Shopping",
    "Travel",
    "Dining",
    "Budget Shopping",
    "Mortgage Payments",
    "Flights",
    "Hotels",
    "Adventure Activities",
    "Cameras",
    "Family Vacations",
    "Kids",
    "Education",
    "Home Essentials",
    "Professional Development",
    "Healthcare",
    "Fixed Deposits",
    "Insurance",
    "Finance Investments",
    "Real Estate",
    "Business Networking",
    "Family Activities",
    "Wellness",
    "Gaming",
    "Tech Gadgets",
    "Streaming Subscriptions",
    "Fine Dining",
    "Luxury Travel",
    "High-End Gadgets",
    "Online Shopping",
    "Food Delivery"
]

preferences = [
    "Discounts",
    "New Arrivals",
    "Home Loan",
    "Retirement Saving",
    "ETFs",
    "Travel Credit Cards",
    "Digital Banking",
    "International Insurance",
    "Family Insurance",
    "Mortgage",
    "Savings Accounts",
    "Health Insuance",
    "Travel credit Crads",
    "Gym Subscription",
    "Tax Savings",
    "Insurance",
    "Digital Banking",
    "Certificates of Deposits",
    "Medicare Plans",
    "Pension Management",
    "Wealth Management",
    "Home Loans",
    "Small Business Financing",
    "Retirement plans",
    "Health & Life Insurance",
    "Tax Savings",
    "BNPL",
    "Crypto",
    "Subscription Services",
    "Private Banking",
    "Investment Portfolios",
    "Tax Advisory",
    "Digital Banks"
]

sentiments = [
    "Navigating fluctuations raw material prices!! Cash Flow planning is KEY!",
    "Loving the new fashion trends this season!",
    "Just finished a 5K run! Need new running shoes. Any suggestions?",
    "Exciting collaborations coming soon!! Guess which celeb is joining our campaign?",
    "Need to start saving more. Thinking of opening a deposit account",
    "Whats the best way to integrate blockchain for textile supply chain transparency?",
    "Struggling to stick to my budget this month.",
    "Trying out the new Tesla self-driving update. Feels like future!!",
    "Why do banks charge so many hidden feed? I need a no-fee checking account",
    "Sponsoring atheletes is costly. Any creative financing options to support brand ambassadors?",
    "Meal prepping for the family! Need new lunchbox ideas",
    "Why is my gym membership so expensive? Thinking of switching.",
    "Looking for efflicent supply chain financing to handle seasonal demand spikes",
    "Capturing beautiful moments with newly bought iphone! Love BNPL!!",
    "Excited to get promoted! Time to plan for wealth creation",
    "Our latest organic products are now available in Whole Foods! Expanding distrbution channels!",
    "Old movies were a delight to eyes. These days, its just action!!!",
    "The rising costs of premium fabrics is impacting pricing strategy. Exploring Financial options!",
    "Just landed in Balil Best WiFi cafes for digital nomads?",
    "Trying out new beauty products!",
    "Marketing volatility ahea-looking at safer hedge fund strategies",
    "Excited about the new digital banking solutions we'are rolling out!!",
    "Looking for sustainable finance options to increase eco-friendly fabric sourcing!!",
    "Can't wait for the new game release!",
    "Concerned about the recent market volatility.",
    "Struggling with delayed invoice payments - need better financial management tools",
    "Any suggestions for travel credit cards in Bali",
    "Love how Whole Foods always stocks fresh organic produce!!!",
    "Managing cash flow during seasonal demand shifts is always a challenge - need better financing options",
    "Happy with the new premium credit card benefits!",
    "Behind the scenes at Paris Fashion Week! Our latest couture line is making waves Medical costs are rising. I need better Medicare coverage.",
    "Proud to be certified organic! Every thread tells a story of sustainability!",
    "Exploring financial partnership to our Direct-To-Customer ecommerce platforml",
    "Excited for an upcoming conference on financial literacy",
    "Whats the best way to manage fluctuating inventory costs in the sports industry?",
    "Why does my bank take 3 days to process my payment? So outdated.",
    "Excited about the new wealth management strategies.",
    "Switching to a new payroll system any recommendation for banking integration?",
    "Just bought a new guitar! #music #hobby",
    "Considering a mortgage for my first home.",
    "Thinking of upgrading my car! Any loan suggestions?",
    "Stock market is volatile again. Should I move to safer investment?",
    "Crypto is the future. Just bought my first Ethereum!!",
    "Retirement planning should start early. Wish I had done more.",
    "Whats the best smart watch for productivity? Apple or Garmin?",
    "Anyone know a good real estate broker? Looking for my first home!!",
    "Scaling up operations to support global cliens! Lokking for banking partners with seamless cross-border transactions",
    "Exploring sustainable finance options to expand our organice farm operations!",
    "Advising UHNW clients on diversifying portfolios into aternative assets like art and crypto ",
    "Expanding our brand to international markets any recommendations for cross border payments solutions?",
    "Partnering with Financial institutions to offer exclusive payment plans for luxury buyers ",
    "Looking for sustainable financing solutions to scale ethical production",
]

def generate_alphanumeric():
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for i in range(6))
#
for _ in range(100):
    users.append({
        "userName": generate_alphanumeric(),
        "customerId": fake.uuid4(),
        "name": fake.name(),
        "age": fake.random_int(18, 80),
        "gender": fake.random_element(["M", "F"]),
        "location": fake.city(),
        "interests": random.sample(interests,3),
        "preferences": random.sample(preferences,3),
        "annualIncome": fake.random_int(0,10000000),
        "education": fake.random_element(["High School", "Bachelor", "Master", "PhD"]),
        "occupation": fake.job(),
        "postId": fake.random_int(101,10000001),
        "socialMediaPlatform": fake.random_element(["Twitter", "Facebook", "Instagram", "linkedIn", "Reddit"]),
        "socialMediaContent": fake.random_element(sentiments),  # Mock posts
        #"socialMediaSentimentScore": fake.random_digit(-1.0, 1.0),
        #"socialMediaIntent": fake.,
        "socialMediaTimeStamp": fake.time(),
        "productId": fake.random_int(21, 200001),
        "purchaseHistory": [fake.word() for _ in range(5)],  # Mock products
    })

df = pd.DataFrame(users)
df.to_csv("customer_data.csv", index=False)


