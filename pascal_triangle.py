prices = [7,6,4,3,1]
mi=min(prices)
max=0
while prices.index(mi)==len(prices)-1 and len(prices)>1:
    prices.pop()
    mi =min(prices)
if len(prices)>0:
    for i in range(prices.index(mi),len(prices)):
        if prices[i]>max:
            max=prices[i]
    print(max-mi)
else:
    print(0)



