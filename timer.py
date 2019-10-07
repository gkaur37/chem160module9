import time
t=time.process_time()
n=100000000
value=10**1000+1
for i in range(n):
    value2=value*value
elapsed_time=time.process_time()-t
print("N=",n,"value bits=",value.bit_length(),"time=",elapsed_time)