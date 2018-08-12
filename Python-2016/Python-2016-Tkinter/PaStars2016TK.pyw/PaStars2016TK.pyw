#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python 2.7
# PaStars2016TK.py

from Tkinter import *
from threading import Timer
import random, math, time


conf__nCount = 30
PI2 = math.pi * 2


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


class PaStars2016TK(Tk):
	def __init__(self):
		Tk.__init__(self, None)

		self.m_nClientWidth, self.m_nClientHeight = 600, 450

		m_nTimerInterval = 0.1

		self.m_nSelected = 0
		self.m_isRunning = True
		#frame = Tk('PaStars2016TK.py')
		self.title('PaStars2016TK.py')
		self.objCanvas = Canvas(self, width=self.m_nClientWidth, height=self.m_nClientHeight, bg='#000000', bd=0)
		self.objCanvas.pack(expand=YES, fill=BOTH)

		self.A_polygons = [None for i in xrange(conf__nCount)]
		self.A_objStars = [Star2016Def() for i in xrange(conf__nCount)]
		coords1 = [0, 1] * 10
		for i in xrange(conf__nCount):
			self.A_polygons[i] = self.objCanvas.create_polygon(coords1, fill='#000000', width=0)

		self.DoInit()

		self.bind('<Button-1>', self.OnLButtonDown)
		self.bind('<Configure>', self.OnResize)
		self.protocol('WM_DELETE_WINDOW', self.OnDestroy)

		self.objThread = Timer(m_nTimerInterval, self.OnTimer)
		self.objThread.start()

	def DoInit(self):
		for i in xrange(conf__nCount):
			self.SetItem(i)
		self.DoDisplay()

	def SetItem(self, i):
		r = 20 + random.randint(0, self.m_nClientWidth/20)
		self.A_objStars[i].Init(r,
			r + random.randint(0, self.m_nClientWidth - r - r),
			r + random.randint(0, self.m_nClientHeight - r - r))

	def DoDisplayItem(self, i):
			try:
				self.objCanvas.coords(self.A_polygons[i], self.A_objStars[i].pts)
				self.objCanvas.itemconfig(self.A_polygons[i], fill=self.A_objStars[i].strColor)
			except Exception,e:
				pass

	def DoDisplay(self):
		for i in xrange(conf__nCount):
			self.DoDisplayItem(i)

	def OnLButtonDown(self, event):
		self.DoInit()

	def OnResize(self, event):
		global self.m_nClientWidth, self.m_nClientHeight
		if(event.width!=self.m_nClientWidth) or (event.height!=self.m_nClientHeight):
			self.m_nClientWidth = event.width
			self.m_nClientHeight = event.height
			self.DoInit()

	def OnDestroy(self):
		self.m_isRunning = False
		self.objThread.join()
		self.destroy()
		print "Destroy."

	def OnTimer(self):
		while self.m_isRunning:
			time.sleep(0.1)
			self.m_nSelected = (self.m_nSelected + 1) % conf__nCount
			self.SetItem(self.m_nSelected)
			self.DoDisplayItem(self.m_nSelected)


if __name__ == '__main__':
	PaStars2016TK()

	mainloop()
