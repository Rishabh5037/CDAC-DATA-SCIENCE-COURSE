Amount = int(input('Enter the investment amount:'))
Years = int(input('Enter the number of years:'))
Rate = int(input('Enter the rate as a%:'))

SUM=0

yr="Year"
sb="Starting balance"
intr="interest"
ebal="Ending balance"



print(yr.ljust(5),sb.rjust(20),ebal.rjust(20))
for each in range(1,6):
    INTREST =(Rate/100)*Amount
    ebal = Amount+INTREST
    print('%d %15.2f %25.2f %19.2f'%(each,Amount,INTREST,ebal))
    Amount = ebal
    SUM+=INTREST
    print("Ending balance:",ebal)
    print("Total intrest earned:",SUM)




