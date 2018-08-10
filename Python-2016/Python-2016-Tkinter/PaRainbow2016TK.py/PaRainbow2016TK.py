#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python 2.7

from Tkinter import *

conf__nCount = 280

def hsv2rgb(h, s, v):
	hi = int(h / 60.0) % 6
	f1 = h / 60.0 - hi
	p = int( v * (1.0 - s) )
	q = int( v * (1.0 - f1 * s) )
	t = int( v * (1.0 - (1.0 - f1) * s) )
	#print hi
	if hi==0:
		return v, t, p
	elif hi==1:
		return q, v, p
	elif hi==2:
		return p, v, t
	elif hi==3:
		return p, q, v
	elif hi==4:
		return t, p, v
	else: #hi==5
		return v, p, q

if __name__ == '__main__':
	m_nClientWidth, m_nClientHeight = 600, 450

	objFrame = Tk('PaRainbow2016TK.py')
	objFrame.title('PaRainbow2016TK.py')
	#objFrame.geometry('%sx%s' % (m_nClientWidth, m_nClientHeight) )

	objCanvas = Canvas(objFrame, width=m_nClientWidth, height=m_nClientHeight, bg='#000000')
	objCanvas.pack(expand=YES, fill=BOTH)

	A_lines = [None for i in xrange(conf__nCount)]
	for i in xrange(conf__nCount):
		m_strColor1 = '#%02x%02x%02x' % hsv2rgb(i, 1.0, 255)
		A_lines = objCanvas.create_line(0, i, m_nClientWidth, i, width=1, fill=m_strColor1)

	mainloop()
