#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python 2.7
# PaStars2016TK.py

from Tkinter import *
from threading import Timer
import random, math, time


conf__nCount = 30
PI2 = math.pi * 2

m_nClientWidth = 600
m_nClientHeight = 450

m_nSelected = 0
m_isRunning = True

m_nTimerInterval = 0.1


class Star2016Def():
	def __init__(self):
		self.cx = self.cy = self.r = 0
		self.strColor = '#FFFFFF'
		self.pts = ()
	def Init(self, r, cx, cy):
		self.r, self.cx, self.cy = (r, cx, cy)
		r2 = r / 2
		a1 = PI2 / 10
		self.pts = ()
		for i in range(5):
			n = i + i
			a2 = PI2 * i / 5
			self.pts += (cx + int(math.sin(a2) * r), cy - int(math.cos(a2) * r))
			a2 += a1
			self.pts += (cx + int(math.sin(a2) * r2), cy - int(math.cos(a2) * r2))
		self.strColor = '#%02X%02X%02X' % (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def PaStars2016TK_SetItem(i):
	r = 20 + random.randint(0, m_nClientWidth/20)
	A_objStars[i].Init(r,
		r + random.randint(0, m_nClientWidth - r - r),
		r + random.randint(0, m_nClientHeight - r - r))

def PaStars2016TK_DoDisplayItem(i):
		try:
			objCanvas.coords(A_polygons[i], A_objStars[i].pts)
			objCanvas.itemconfig(A_polygons[i], fill=A_objStars[i].strColor)
		except Exception,e:
			pass

def PaStars2016TK_DoDisplay():
	for i in xrange(conf__nCount):
		PaStars2016TK_DoDisplayItem(i)

def PaStars2016TK_DoInit():
	for i in xrange(conf__nCount):
		PaStars2016TK_SetItem(i)
	PaStars2016TK_DoDisplay()

def PaStars2016TK_LButtonDown(event):
	PaStars2016TK_DoInit()

def PaStars2016TK_OnResize(event):
	global m_nClientWidth, m_nClientHeight
	if(event.width!=m_nClientWidth) or (event.height!=m_nClientHeight):
		m_nClientWidth = event.width
		m_nClientHeight = event.height
		PaStars2016TK_DoInit()

def PaStars2016TK_OnDestroy():
	global m_isRunning
	m_isRunning = False
	objThread.join()
	objFrame.destroy()
	print "Destroy."

def PaStars2016TK_OnTimer():
	global m_nSelected
	while m_isRunning:
		time.sleep(0.1)
		m_nSelected = (m_nSelected + 1) % conf__nCount
		PaStars2016TK_SetItem(m_nSelected)
		PaStars2016TK_DoDisplayItem(m_nSelected)


if __name__ == '__main__':
	objFrame = Tk('PaStars2016TK.py')
	objFrame.title('PaStars2016TK.py')

	objCanvas = Canvas(objFrame, width=m_nClientWidth, height=m_nClientHeight, bg='#000000', bd=0)
	objCanvas.pack(expand=YES, fill=BOTH)

	A_polygons = [None for i in xrange(conf__nCount)]
	A_objStars = [Star2016Def() for i in xrange(conf__nCount)]
	coords1 = [0, 1] * 10
	for i in xrange(conf__nCount):
		A_polygons[i] = objCanvas.create_polygon(coords1, fill='#000000', width=0)

	PaStars2016TK_DoInit()

	objFrame.bind('<Button-1>', PaStars2016TK_LButtonDown)
	objFrame.bind('<Configure>', PaStars2016TK_OnResize)
	objFrame.protocol('WM_DELETE_WINDOW', PaStars2016TK_OnDestroy)

	objThread = Timer(m_nTimerInterval, PaStars2016TK_OnTimer)
	objThread.start()

	mainloop()
