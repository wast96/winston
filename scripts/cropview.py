#!/usr/bin/env python3
"""Crop a fractional box from a page PNG for eyeball verification.
Usage: cropview.py PAGE L T R B [--out /tmp/x.png] [--scale 3]
Fractions are 0..1 of width(L,R)/height(T,B). Origin top-left.
"""
import sys, os
from PIL import Image
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
page=int(sys.argv[1]); L,T,R,B=[float(x) for x in sys.argv[2:6]]
out="/tmp/claude-0/-home-user-winston/dac10533-0580-58c9-9032-3548cb13c2f6/scratchpad/crop.png"
scale=3
i=6
while i < len(sys.argv):
    if sys.argv[i]=='--out': out=sys.argv[i+1]; i+=2
    elif sys.argv[i]=='--scale': scale=float(sys.argv[i+1]); i+=2
    else: i+=1
im=Image.open(os.path.join(ROOT,'data','png','p%04d.png'%page))
w,h=im.size
box=(int(L*w),int(T*h),int(R*w),int(B*h))
c=im.crop(box)
c=c.resize((int(c.width*scale),int(c.height*scale)))
os.makedirs(os.path.dirname(out),exist_ok=True)
c.save(out)
print('saved',out,'from',box,'pagesize',(w,h))
