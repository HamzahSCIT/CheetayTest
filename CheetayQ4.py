def mergeSort(end, start):
    if len(end) > 1:
        mid = len(end) // 2
        left = end[:mid]
        right = end[mid:]
        
        mid = len(start) // 2
        sleft = start[:mid]
        sright = start[mid:]

        mergeSort(left, sleft)
        mergeSort(right, sright)

        i = 0
        j = 0        
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
              end[k] = left[i]
              start[k] = sleft[i]
              i += 1
            else:
                end[k] = right[j]
                start[k] = sright[j]
                j += 1
            k += 1

        while i < len(left):
            end[k] = left[i]
            start[k] = sleft[i]
            i += 1
            k += 1

        while j < len(right):
            end[k]=right[j]
            start[k] = sright[j]
            j += 1
            k += 1
        
        return end, start


def maxMeetings(S, E, N): 
    temp = 0
    E, S = mergeSort(E, S)                
    print(S[temp], E[temp]), 
    count = 1
    
    for j in range(n): 
        if S[j] > E[temp]: 
            print(S[j], E[j]), 
            temp = j
            count += 1
    
    return count
  

start = [75250, 50074, 43659, 8931, 11273, 27545, 50879, 77924]
end = [112960, 114515, 81825, 93424, 54316, 35533, 73383, 160252]
n = len(end)

print(maxMeetings(start, end, n))