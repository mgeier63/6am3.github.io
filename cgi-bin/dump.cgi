#!/usr/bin/env python
import sys
import os
import time

dumped = open('/home/foobar/pbdbg_'+os.environ['QUERY_STRING']+'_'+str(int(time.time())), 'wb')

for line in sys.stdin:
 dumped.write(line)

print "Content-type: text/html" 
print 
print "<html><body>" 
print "OK"
print str(int(time.time()))
print os.environ['QUERY_STRING']
print "</body></html>" 
