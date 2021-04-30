def longestSubstrDistinctChars(s):   
    seenCharacters = {}
    length = 0
    start = 0
      
    for i,c in enumerate(s):
        if c in seenCharacters:
            start = max(start, seenCharacters[c] + 1)
  
        seenCharacters[c] = i
        length = max(length, i-start + 1)
        
    return length
  

s = "geeksforgeeks"
length = longestSubstrDistinctChars(s)
print(length)
