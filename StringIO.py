# StringIO

import StringIO

# arbitrary string
message = 'This is just a normal string.'

# StringIO method to set as file object
f = StringIO.StringIO(message)


f.read()

f.write(" Second line written to file like object")

# reset cursor like a file
f.seek(0)

# read again
f.read()
