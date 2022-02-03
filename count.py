import datetime
x = datetime.datetime.now()
print('########## Receipt ##########')
j = int(input('NumProduct= '))
print('########## price ##########')
sum=0
t=0
for i in range(j):
    h= float(input('price= '))
    t+=h
print('########## discount ##########')
n= int(input('disPer= '))
p = t*(n/100) #ผมรวม%
sum = t-p #ผลรวมหลังลบ%
# sum = t-(t*(n/100))
print('')
print('Date:',x.strftime("%A"),x.date(),'Time:',x.strftime("%H"),':',x.strftime("%M"))
print('Summary=',t,'discount--',n,'--%=',p,'bath')
print('TotalSummary=[',sum,']/Bath')
print('')
##