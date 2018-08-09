#!/usr/bin/python
# -*- coding:utf-8 -*-

# Python 2.7
# PaEllipse2016TK.pyw

from Tkinter import *
from threading import *
import random, time, math


conf__nCount = 40
conf__strColor = '#FFFF00'

m_nClientWidth = 600
m_nClientHeight = 450
m_isRunning = True
m_nTimerInterval = 0.1
PI2 = math.pi * 2
m_fStartAngle = 0

class PaEllipseDef:
	x, y, a, b, angle, rotate = (0, 0, 0, 0, 0, 0)
	def __init__(self):
		pass
	def __init__(self, x, y, a, b, angle, rotate):
		self.x = x
		self.y = y
		self.a = a
		self.b = b
		self.angle = angle
		self.rotate = rotate

def PA_DoEllipseRotate():
	global m_fStartAngle
	m_fStartAngle += PI2 / 160
	if(m_fStartAngle>=PI2):
		m_fStartAngle=0


def PaEllipse2016TK_OnTimer():
	while m_isRunning:
		time.sleep(0.05)
		PA_DoEllipseRotate()
		PaEllipse2016TK_DoDisplay()

def PaEllipse2016TK_OnDestroy():
	global m_isRunning
	m_isRunning = False
	objThread.join()
	objFrame.destroy()
	print 'Destroy.'

def _rotate(x, y, angle):
	sin1 = math.sin(angle)
	cos1 = math.cos(angle)
	x1, y1 = (x, y)
	x = cos1 * x1 + sin1 * y1
	y = cos1 * y1 - sin1 * x1
	return (x, y)

def PaEllipse2016TK_DoDisplay():
	#print 'PaEllipse2016TK_DoDisplay()'

	x0 = m_nClientWidth / 2
	y0 = m_nClientHeight / 2
	step = PI2 / conf__nCount
	r = d = 0
	try:
		for i in xrange(conf__nCount):
			angle1 = i * step
			sin1 = math.sin(angle1 + m_fStartAngle)
			cos1 = math.cos(angle1 + m_fStartAngle)
			r = r==3 and 6 or 3 # r = r==3 ? 6 : 3
			d = r + r
			x1 = pes1.a * sin1
			y1 = pes1.b * cos1
			x1, y1 = _rotate(x1, y1, m_fStartAngle)
			x1 += x0
			y1 += y0
			objCanvas.coords(A_ovals1[i], (x1 - r, y1- r, x1 + r, y1 + r))
			x1 = pes2.a * sin1
			y1 = pes2.b * cos1
			x1, y1 = _rotate(x1, y1, m_fStartAngle)
			x1 += x0
			y1 += y0
			objCanvas.coords(A_ovals2[i], (x1 - r, y1- r, x1 + r, y1 + r))
	except Exception, e:
		pass

def PaEllipse2016TK_OnResize(event):
	global m_nClientWidth, m_nClientHeight
	if (event.width!=m_nClientWidth) or (event.height!=m_nClientHeight):
		m_nClientWidth = event.width
		m_nClientHeight = event.height

if __name__ == '__main__':
	objFrame = Tk('PaEllipse2016TK.py')
	objFrame.title('PaEllipse2016TK.py')

	objCanvas = Canvas(objFrame, width=m_nClientWidth, height=m_nClientHeight, bg='#000000' , bd=0)
	objCanvas.pack(expand=YES, fill=BOTH)

	objFrame.protocol('WM_DELETE_WINDOW', PaEllipse2016TK_OnDestroy)

	pes1 = PaEllipseDef(0, 0, 300, 75, 0, 0)
	pes2 = PaEllipseDef(0, 0, 50, 200, 0, 0)

	A_ovals1 = [None for i in xrange(conf__nCount)]
	A_ovals2 = [None for i in xrange(conf__nCount)]
	for i in range(conf__nCount):
		A_ovals1[i] = objCanvas.create_oval(0, 0, 1, 1, fill=conf__strColor, width=0)
		A_ovals2[i] = objCanvas.create_oval(0, 0, 1, 1, fill=conf__strColor, width=0)

	objThread = Timer(m_nTimerInterval, PaEllipse2016TK_OnTimer)
	objThread.start()

	objFrame.bind('<Configure>', PaEllipse2016TK_OnResize)

	mainloop()
