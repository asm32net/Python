#!/usr/bin/python
# -*- coding:utf-8 -*-

# Python 2.7
# PaEllipse2016TK.pyw

from Tkinter import *
from threading import *
import random, time, math


conf__nCount = 40
conf__strColor = '#FFFF00'
PI2 = math.pi * 2

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

class PaEllipse2016TK(Tk):
	def __init__(self):
		Tk.__init__(self, None)

		m_nTimerInterval = 0.1

		self.m_nClientWidth, self.m_nClientHeight = (600, 450)
		self.m_isRunning = True
		self.m_fStartAngle = 0

		self.title('PaEllipse2016TK.py')

		self.objCanvas = Canvas(self, width=self.m_nClientWidth, height=self.m_nClientHeight, bg='#000000' , bd=0)
		self.objCanvas.pack(expand=YES, fill=BOTH)

		self.protocol('WM_DELETE_WINDOW', self.OnDestroy)

		self.pes1 = PaEllipseDef(0, 0, 300, 75, 0, 0)
		self.pes2 = PaEllipseDef(0, 0, 50, 200, 0, 0)

		self.A_ovals1 = [None for i in xrange(conf__nCount)]
		self.A_ovals2 = [None for i in xrange(conf__nCount)]
		for i in range(conf__nCount):
			self.A_ovals1[i] = self.objCanvas.create_oval(0, 0, 1, 1, fill=conf__strColor, width=0)
			self.A_ovals2[i] = self.objCanvas.create_oval(0, 0, 1, 1, fill=conf__strColor, width=0)

		self.objThread = Timer(m_nTimerInterval, self.OnTimer)
		self.objThread.start()

		self.bind('<Configure>', self.OnResize)

	def DoEllipseRotate(self):
		self.m_fStartAngle += PI2 / 160
		if(self.m_fStartAngle>=PI2):
			self.m_fStartAngle=0


	def OnTimer(self):
		while self.m_isRunning:
			time.sleep(0.05)
			self.DoEllipseRotate()
			self.DoDisplay()

	def OnDestroy(self):
		self.m_isRunning = False
		self.objThread.join()
		self.destroy()
		print 'Destroy.'

	def _rotate(self, x, y, angle):
		sin1 = math.sin(angle)
		cos1 = math.cos(angle)
		x1, y1 = (x, y)
		x = cos1 * x1 + sin1 * y1
		y = cos1 * y1 - sin1 * x1
		return (x, y)

	def DoDisplay(self):
		#print 'self.DoDisplay()'

		x0 = self.m_nClientWidth / 2
		y0 = self.m_nClientHeight / 2
		step = PI2 / conf__nCount
		r = d = 0
		try:
			for i in xrange(conf__nCount):
				angle1 = i * step
				sin1 = math.sin(angle1 + self.m_fStartAngle)
				cos1 = math.cos(angle1 + self.m_fStartAngle)
				r = r==3 and 6 or 3 # r = r==3 ? 6 : 3
				d = r + r
				x1 = self.pes1.a * sin1
				y1 = self.pes1.b * cos1
				x1, y1 = self._rotate(x1, y1, self.m_fStartAngle)
				x1 += x0
				y1 += y0
				self.objCanvas.coords(self.A_ovals1[i], (x1 - r, y1- r, x1 + r, y1 + r))
				x1 = self.pes2.a * sin1
				y1 = self.pes2.b * cos1
				x1, y1 = self._rotate(x1, y1, self.m_fStartAngle)
				x1 += x0
				y1 += y0
				self.objCanvas.coords(self.A_ovals2[i], (x1 - r, y1- r, x1 + r, y1 + r))
		except Exception, e:
			pass

	def OnResize(self, event):
		if (event.width!=self.m_nClientWidth) or (event.height!=self.m_nClientHeight):
			self.m_nClientWidth = event.width
			self.m_nClientHeight = event.height

if __name__ == '__main__':
	PaEllipse2016TK()
	mainloop()
