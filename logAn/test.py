import re

line = '10.1.1.1 - - [22/Aug/2014:16:48:19 +0800] "POST /ajax/MbpRequest.do HTTP/1.1" 200 616 "-" "Dalvik/1.6.0 (Linux; U; Android 4.0.4; GT-I9103 Build/IMM76D)" "36.250.89.22" 127.0.0.1:8090 0.036 0.036 '

p = r'(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'

o = re.compile(p)

m = o.search(line)

print(m.groupdict())


