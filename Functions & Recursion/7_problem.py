#......WAF to convert usd to pkr (today 1$=279.88)
def converter(usd_val):
    pkr_val = usd_val * 279.88  # Multiply by today's conversion rate
    print(usd_val, "USD =", pkr_val, "PKR") 
converter(1)
converter(6)