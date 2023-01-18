import numpy as np
import random

class Sorter:
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

    def mainMenu(self):
        numbers_to_sort = int(input("How many numbers would you like to generate to be sorted?"))
        largest_number = int(input("What is max value you would like a random number to have?"))
        array = self.generateRandom(self, numbers_to_sort, largest_number)
        print(array)
        print('-----------')
        print('sorted')
        answer = self.bucketSort(self, array)


S = Sorter
S.mainMenu(S)

