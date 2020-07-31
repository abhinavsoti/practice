print ("Condition Program Starts now")
print ("lets print the length of the string first")
a0 = "I am happy today"
a = len(a0)
print ("the length of the string (" + a0 + ") is: " + str(a))

# Dictionary example to store stock price for a given stock over a perriod of time

dict_stock_price_YesBank = {'YES':{'NSE': {'07302020': 11.90,'07292020': 12.35, '07282020': 12.20}, 'BSE': {'07302020': 11.80,'07292020': 12.15, '07282020': 12.00}}}

print (dict_stock_price_YesBank ['YES'] ['NSE'])

print (dict_stock_price_YesBank ['YES'] ['BSE'])
