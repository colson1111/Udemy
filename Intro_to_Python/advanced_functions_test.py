# Advanced Functions Test
# Problem 1:  use map to create a function which finds the length of 
# each word in the phrase (broken by spaces), and returns the values 
# in a list

def word_lengths(phrase):
    return map(len,phrase.split())
    
word_lengths('How long are the words in this phrase')


# Problem 2:  Use reduce to take a list of digits and return the number that 
# they correspond to.  Do not convert the integers to strings!
def digits_to_num(digits):
    return reduce(lambda x,y: x*10 + y, digits)

digits_to_num([3,4,3,2,1])


# Problem 3:  Use filter to return the words from a list of words which
# start with a target letter

def filter_words(word_list, letter): 
    return filter(lambda x: x[0].lower() == letter.lower(), word_list)    

l = ['hello','are','cat','dog','ham','hi','go','to','heart']
filter_words(l,'h')


# Problem 4:  Use zip and list comprehension to return a list of the same length
# where each value is the two strings from L1 and L2 concatenated together
# with connector between them.

def concatenate(L1, L2, connector):
    return [x + connector + y for x,y in zip(L1, L2)]

concatenate(['A', 'B'], ['a', 'b'], '-')


# Problem 5:  Use enumerate and other skills to return a dictionary which has the
# values of the list as keys and the index as the value.  You may assume that a
# value will only appear once in a given list.
def d_list(L):
    return {key:value for value,key in enumerate(L)}
    
d_list(['a', 'b', 'c'])


# Problem 6:  Use enumerate and other skills to return the count of the number
# of items in the list whose value equals its index
def count_match_index(L):
    return sum([i == value for i,value in enumerate(L)])

    

count_match_index([0,2,2,1,5,5,6,10])

