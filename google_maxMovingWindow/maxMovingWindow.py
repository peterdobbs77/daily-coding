

def maxInMovingWindow(array, k):
    for i in range(len(array)-k+1):
        array[i] = max(array[i:i+k])
        print(array[i])


array = [10, 5, 2, 7, 8, 7]
k = 3
maxInMovingWindow(array, k) # shouldBe = [10, 7, 8, 8]
