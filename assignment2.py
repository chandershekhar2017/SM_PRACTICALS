# Tyre Shop Modelling and Simulation
# Name---->CHANDER SHEKHAR
# Roll -->1/17/FET/BCS/056 (8CSA)



import random
p = list(map(int,input("\nEnter the reorder value according to policy : ").strip().split()))
q = list(map(int,input("\nEnter the reorder quantity according to policy : ").strip().split()))

cost=[0]*5

for i in range(5):
    day=0
    duedate=0
    unitsdue=45
    start=0
    stock=115
   
    while(day<=180):
        if(day==duedate):
            stock=stock+q[i]
            unitsdue=0
        demand=random.randint(0,99)
        if(demand<=stock):
            stock=stock-demand
            cost[i]=cost[i]+0.75
        else:
            shortage=demand-stock
            cost[i]=cost[i]+shortage
            stock=0
        if(stock+unitsdue<=p[i]):
            unitsdue=q[i]
            cost[i]=cost[i]+18
            duedate=day+3
        day=day+1
        
    print("cost of "+str(i)+" Policy is "+str(cost[i]))
            
    
    
