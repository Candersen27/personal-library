import numpy as np
import random

class Solution:
    def bucketSort(self, A):
        min = A[0]
        max = A[0]
        finalSorted = []
        for i in A:
            if i > max:
                max = i
            if i < min:
                min = i
        #print(min)
        #print(max)
        numBuckets = max - min
        myBuckets = np.zeros(numBuckets+1)

        for i in A:
            #print(i-min)
            myBuckets[i-min] += 1
        #print(myBuckets)

        for i in range(0, len(myBuckets)):
            j = int(myBuckets[i])
            for k in range(0, j):

                finalSorted.append(i + min)
        print(finalSorted)
        return finalSorted

    def generateRandom(self, n, max):
        randomList = []
        for i in range(0, n):
            temp = random.randint(0, max)
            randomList.append(temp)
        return randomList





test = Solution()
myArray = test.generateRandom(1000000, 1000)
print(myArray)
ans = test.bucketSort(myArray)
