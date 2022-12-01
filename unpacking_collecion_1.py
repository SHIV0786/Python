#unpacking a sequence into separate variable
p = (4,5)
x, y = p
print(x," ",y)

data = ['ACME',50,91.9,(2021,12,21)]
name, shares, price, date = data
print("Name : ",name,"Shares: ",shares,"Price: ",price,"Date: ",date)

name, shares, price, (year, month, date) = data
print("Name : ",name,"Shares: ",shares,"Price: ",price,"Year: ",year,"Month: ",month,"Date: ",date)
print("\n")

#unpacking string
s = "Hello"
a,b,c,d,e, = s
print(a,b,c,d,e)

# when unpacking you may sometimes want to discard certain values then we can pick throwaway variable name for it
data = ['ACME',50,91.9,(2012,12,30)]
_, shares, price, _ = data
print(shares,price)
