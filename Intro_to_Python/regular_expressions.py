# regular expressions

import re

# SEARCHING FOR PATTERNS IN TEXT

# list of patterns to search for
patterns = ['term1', 'term2']

# text to parse
text = 'This is a string with term1, but it does not have the other term.'

for pattern in patterns:
    print 'Searching for "%s" in: \n"%s"' % (pattern, text),

    # check for match
    if re.search(pattern, text):
        print '\n'
        print 'Match was found. \n'
    else:
        print '\n'
        print 'No match was found.\n'

match = re.search(patterns[0], text)

type(match)  # returns a match object

match.start()  # show start of match
match.end()    # show end of match




# SPLIT WITH REGULAR EXPRESSIONS

split_term = '@'
phrase = 'What is the doman name of someone with the email: hello@gmail.com'

re.split(split_term, phrase)

re.split("a", "This is a sentence with a bunch of words in it")



# FINDING ALL INSTANCES OF A PATTERN
re.findall('match', 'test phrase match here and match here')

# PATTERN re SYNTAX

# function to return results from re
def multi_re_find(patterns, phrase):
    '''
    takes in a list of regex patterns
    Print a list of all matches
    '''
    
    for pattern in patterns:
        print 'Searching the phrase using the re check: %r' % pattern
        print re.findall(pattern,phrase)
        print '\n'



# REPETITION SYNTAX
test_phrase =  'sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd'

test_patterns = ['sd*',      # s followed by zero or more d's
                 'sd+',      # s followed by one or more d's
                 'sd?',      # s follow by 0 or 1 d's
                 'sd{3}',    # s followed by 3 d's
                 'sd{2,4}',  # s followed by 2 or 3 d's
                 ]

multi_re_find(test_patterns, test_phrase)


# CHARACTER SETS
test_patterns = ['[sd]',   # either s or d
                 's[sd]+', # s followed by one or more s or d
                 'd[sd]{1}' # s followed by exactly 1 s or d
                 ]
                 

multi_re_find(test_patterns, test_phrase)

# EXCLUSION
test_phrase = 'This is a string! But it has punctuation.  How can we remove it?'

re.findall('[^!.? ]+', test_phrase)



# CHARACTER RANGES
test_phrase = 'This is an example sentence.  Lets see if we can find some letters.'

test_patterns = ['[a-z]+',      # sequences of lower case letters
                 '[A-Z]+',      # sequences of upper case letters
                 '[a-zA-Z]+',   # sequences of lower or upper case letters
                 '[A-Z][a-z]+'] # one upper case followed by lower case letteres

multi_re_find(test_patterns, test_phrase)

                 
        
# ESCAPE CODES
test_phrase = 'This is a string with some numbers 1233 and a symbol #hashtag'

test_patterns = [r'\d+', # sequence of digits
                 r'\D+', # sequence of non-digits
                 r'\s+', # sequence of whitespace
                 r'\S+', # sequence of non whitespace
                 r'\w+', # alphanumeric characters
                 r'\W+', # non alphanumeric characters
                 ]
                 
multi_re_find(test_patterns, test_phrase)

