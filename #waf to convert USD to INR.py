#waf to convert USD to INR
usd= int(input("enter dollar:"))
inr=int(input("enter current rupee value"))


def converter(usd,inr):
    fees= usd*inr
    print("total amount=",fees)
    return fees
converter(usd,inr)