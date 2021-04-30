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


def activitySelection(start, end, n): 
    temp = 0

    if n < 1:
        return 0
    
    end, start = mergeSort(end, start)
        
    # for i in range(1,n):
    #     for j in range(0,n-1):
    #         if(end[j] > end[j+1]):
    #             temp = start[j]
    #             start[j] = start[j+1]
    #             start[j+1] = temp
        
    #             temp = end[j]
    #             end[j] = end[j+1]
    #             end[j+1] = temp
    
    print(start)
    print(end)
                
    print("\nMaximum Selected Activities")
    temp = 0
    print(start[temp], end[temp]), 
    count = 1
    
    for j in range(n): 
        if start[j] > end[temp]: 
            print(start[j], end[j]), 
            temp = j
            count += 1
    
    return count
  

start = [1, 3, 2, 5]
end = [2, 4, 3, 6]
n = len(end)

print(activitySelection(start, end, n))