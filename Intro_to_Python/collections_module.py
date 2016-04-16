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
dict(lc)                    # convert to a dictionary
lc.items()                  # converts to a list of (element, count) pairs

list_of_pairs = [(1,2),(3,4),(5,6)]
Counter(dict(list_of_pairs)) # convert from a list of (elem, cnt) pairs

lc.most_common()[:-3-1:-1]   # n least common elements
lc += Counter()                 # remove zero and negative counts




# defaultdict
from collections import defaultdict

d = {}
d['one']   # key error:  key 'one' doesn't exist

d = defaultdict(object)
d['one']

for item in d:
    print item
    
# can initialize with default values
d = defaultdict(lambda: 0)
d['one']
    




# orderedDict
from collections import OrderedDict    

print 'Normal dictionary: '
d = {}

d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['d'] = 'D'
d['e'] = 'E'

for (k,v) in d.items():
    print k,v


print 'OrderedDict: '
d = OrderedDict()

d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['d'] = 'D'
d['e'] = 'E'

for k,v in d.items():
    print k,v
    
# equality with an OrderedDict()
print 'Dictionaries are equal? '

d1 = {}
d1['a'] = 'A'
d1['b'] = 'B'

d2 = {}
d2['b'] = 'B'
d2['a'] = 'A'

print d1 == d2

print 'Ordered Dictionaries are equal? '
d1 = OrderedDict()
d1['a'] = 'A'
d1['b'] = 'B'

d2 = OrderedDict()
d2['b'] = 'B'
d2['a'] = 'A'    

print d1 == d2



# namedtuple
t = (12,13,14)
t[0]

from collections import namedtuple
Dog = namedtuple('Dog', 'age breed name')

sam = Dog(age = 2, breed = 'Lab', name = 'Sammy')
little_max = Dog(age = 8, breed = 'Dude', name = 'Max')

print little_max.age
print little_max.breed
print little_max.name


new = (7, 'Husky', 'Bob')
bob = Dog._make(new)

