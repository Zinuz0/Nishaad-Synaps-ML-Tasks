request_spending = {
    "Mahek": {
        "balance": 3000.00,
        "transactions": [
            {"amount": -9000.00, "category": "Creatives"},
            {"amount": 7000.00, "category": "Sponsor"},
            {"amount": -2000.00, "category": "Prize-Money"}
        ]
    },
    "Arham": {
        "balance": 5000.00,
        "transactions": [
            {"amount": 8000.00, "category": "Stalls"},
            {"amount": 7500.00, "category": "Seminars"}
        ]
    },
    "Unnati": {
        "balance": 3500.00,
        "transactions": [
            {"amount": -5000.00, "category": "Attraction"},
            {"amount": 2500.00, "category": "Promo"},
            {"amount": -900.00, "category": "Lighting"},
            {"amount": -3000.00, "category": "Games"}
        ]
    },
    "Gaurang": {
        "balance": 2000.00,
        "transactions": [
            {"amount": -1500.00, "category": "Website"},
            {"amount": -1000.00, "category": "C2C"},
            {"amount": -500.00, "category": "Posters"}
        ]
    }
}

    
def total_spending(request_spending, account_id, category):
    if account_id in request_spending:
        name = request_spending[account_id]
        
        for transaction in name['transactions']:
            if transaction["category"] == category:
                amount_spent= transaction["amount"]
        return amount_spent 
    else:
        return "Account not found" 

print(total_spending(request_spending, "Mahek", "Creatives"))
    
     

