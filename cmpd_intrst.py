def cmpd_intrst(p,r,n,t):
    a=p*(1+(r/n))**(n*t)
    return round(a,2) 
P,R,N,T=map(int, input('Enter Principle,rate,numbers of time interest compound, time (year) : ').split(','))
print(cmpd_intrst(P,R,N,T))