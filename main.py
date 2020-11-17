import random
import sys

sys.stdout = open("multiHashResults.txt","w")

hashTableSize, flowIdSize, hashSize = 1000,1000, 3

hashTable = [-1 for _ in range(hashTableSize)]
hashValues = random.sample(range(0, 1000000), hashSize)
flowIds = random.sample(range(0, 1000000), flowIdSize)
unHashableFlows=[]

for flow in flowIds:
  
  flag, hashVal = 1, 0

  for hash in hashValues: 
    hashVal = ( flow ^ hash ) % hashTableSize
    if hashTable[hashVal] == -1:
      flag = 0
      break
      
  if flag == 1:
    unHashableFlows.append(flow)
  else:
    hashTable[hashVal] = flow

print('---------------------------------------')
print('---------------------------------------')

print("Successful entries in hash table -->")
print(len(hashTable) - len(unHashableFlows))

print('---------------------------------------')
print('---------------------------------------')

print("Hash table -->")
print([0 if entry == -1 else entry for entry in hashTable])

print('---------------------------------------')
print('---------------------------------------')


sys.stdout.close()