# Name-->CHANDER SHEKHAR
#  Roll-->1/17/FET/BCS/056 (8CSA)

import random
customers = [1, 2, 3,4,5,6,7]
n=len(customers)
arrival_time = []
arrival_time.append(random.randint(1,6))
for i in range(1,7):
    r=random.randint(1,6)
    arrival_time.append(arrival_time[i-1]+r)


service_time = [2,3,1,1,1,1,2] 

service_begin=[]
service_end=[]
waiting_time=[]
server_idle=[]
service_begin.append(0)
waiting_time.append(0)
service_end.append(service_time[0])
server_idle.append(0)
for i in range(1,7):
    if service_end[i-1]>arrival_time[i]:
        service_begin.append(service_end[i-1])
    else:
        service_begin.append(arrival_time[i])
    service_end.append(service_begin[i]+service_time[i])
    waiting_time.append(service_begin[i]-arrival_time[i])
    server_idle.append(service_begin[i]-service_end[i-1])
    
print("customer\tArrival Time\tServiceBegin\tServiceTime\tServiceEnd\tWaitingTime\tServerIdle")
for i in range(7):
    print(" ", i + 1, "\t\t", arrival_time[i], "\t\t", service_begin[i], 
              "\t\t", service_time[i], "\t\t", service_end[i], "\t\t", waiting_time[i],"\t\t",server_idle[i])
