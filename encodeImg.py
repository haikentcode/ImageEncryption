#!/usr/bin/env python
import sys
x=sys.argv[1]
y=sys.argv[2]
z=sys.argv[3]

hk=open(x,"rb")
tm=hk.read()
ag=open(z,'wb')
gudan=sum(ord(ch) for ch in y)%256
list1=list(tm)
k=0;
 
for x in list1:
        i=int(x.encode('hex'),16)
        t=(i+gudan)%256
        list1[k]=("%0.2X"%t).decode('hex')
        k=k+1;

strn=''.join(list1)

ag.write(strn);

