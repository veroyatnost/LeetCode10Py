

'''
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). 
You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.
'''

def canCompleteCircuit(I,C):
  R=[I[i]-C[i] for i in range(len(I))]
  RC=[sum(R[:i+1]) for i in range(len(I))]
  if sum(R)<0:
    return -1
  else:
    result=0 if RC.index(min(RC))+1==len(I) else RC.index(min(RC))+1
  return result
