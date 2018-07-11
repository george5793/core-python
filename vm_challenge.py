from byotest import *

usd_coins = {100: 20, 50: 20, 25: 20, 10: 20, 5: 20, 1: 20}
eur_coins = {100: 20, 50: 20, 20: 20, 10: 20, 5: 20, 2: 20, 1: 20}

def get_change_from_vm(amount, coins = eur_coins):
    
    change = []
    
    for coin in sorted(coins.keys(), reverse = True):
        
        while coin <= amount and coins[coin] > 0:
            
            amount -= coin
            coins[coin] -= 1
            change.append(coin)
            
    if amount != 0:
        raise Exception("Insufficient coins to give change")
        
    return change
    
get_change_from_vm(3759)
print(eur_coins)