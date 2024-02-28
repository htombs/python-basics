import time

t = time.localtime(time.time())
local = time.asctime(t)
today = "Today is " + local

print(t)
print(local)
print(today)

# you can import pre written code from the python server.
# in this case we've imported "time" and built a function using that already written code