# COLLECTIONS MODULE

# Counter

from collections import Counter

# Counter() with lists
l = [1,1,1,2,2,2,3,3,45,5,5,5,6,7,8,7,6,4,3,3,1]
lc = Counter(l)

# Counter() with strings
Counter('safdafdadabvfjavndiwnfandskavdfada')

# Counter() with words in a sentence
s = 'How many times does each word show up in this sentence, each word in this word'
words = s.split()
Counter(words)

Counter('How how how how words many words how'.split())

# Common patterns when using a Counter
sum(lc.values())            # total of all counts
lc.clear()                  # resets all counts
list(lc)                    # list unique elements
set(lc)                     # convert to a set


