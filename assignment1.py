import math
targetx=[]
# Name-->CHANDER SHEKHAR
 #  Roll-->1/17/FET/BCS/056 (8CSA)


targety=[]
fighterx=[0]*12
fightery=[0]*12

print("Enter Target path, xb[t] & yb[t]:")
targetx=list(map(int, input().split()))
targety=list(map(int, input().split()))
print(targetx)
print("Enter Fighter's Initial position,")
fighterx[0]=int(input())
fightery[0]=int(input())
print("Enter Fighter velocity, vf:")
fighterv=int(input())
for t in range(12) :
  d=math.sqrt(pow((targety[t]-fightery[t]),2)+pow((targetx[t]-fighterx[t]),2));
  if d<10:
    print("\nCaught at"+str(t)+" mts and "+str(d)+" kms");
    break
     
  else:
    
    fighterx[t+1]=fighterx[t]+(fighterv*(targetx[t]-fighterx[t])/d)
    fightery[t+1]=fightery[t]+(fighterv*(targety[t]-fightery[t])/d)
     

if t>11:
    print("Target Escaped\n")
