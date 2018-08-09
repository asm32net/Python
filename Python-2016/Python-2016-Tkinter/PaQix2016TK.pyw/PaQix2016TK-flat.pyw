#!/usr/bin/python
# -*- coding:utf-8 -*-

# Python 2.7
# PaQix2016TK.pyw

from Tkinter import *
from threading import Timer
import random
import time

conf__nCount = 100

m_nClientWidth = 600
m_nClientHeight = 450
m_isRunning = True
m_nTimerInterval = 0.1

class PaQixDef():
	def __init__(self):
		self.x = [0, 0, 0, 0]
		self.y = [0, 0, 0, 0]
		self.dx = [0, 0, 0, 0]
		self.dy = [0, 0, 0, 0]
		self.cr = self.cg = self.cb = 255
		self.dr = self.dg = self.db = 5
	def Config(self, nClientWidth, nClientHeight):
		self.m_nClientWidth  = nClientWidth
		self.m_nClientHeight = nClientHeight
	def Init(self):
		for i in range(2):
			self.x[i] = random.randint(0, self.m_nClientWidth)
			self.y[i] = random.randint(0, self.m_nClientHeight)
			self.dx[i] = random.randint(2, 5)
			self.dy[i] = random.randint(2, 5)
		self.cr = random.randint(0, 255)
		self.cg = random.randint(0, 255)
		self.cb = random.randint(0, 255)
	def Update(self, isUpdate):
		for i in range(2):
			if isUpdate:
				from1 = i
				to1 = i + 2
			else:
				from1 = i + 2
				to1 = i
			self.x[to1] = self.x[from1]
			self.y[to1] = self.y[from1]
			self.dx[to1] = self.dx[from1]
			self.dy[to1] = self.dy[from1]
	def Move(self):
		for i in range(2):
			nx = self.x[i] + self.dx[i]
			if (self.dx[i]>0) and (nx>self.m_nClientWidth) or (self.dx[i]<0) and (nx<0):
				self.dx[i] = -self.dx[i]
			else:
				self.x[i] = nx
			ny = self.y[i] + self.dy[i]
			if (self.dy[i]>0) and (ny>self.m_nClientHeight) or (self.dy[i]<0) and (ny<0):
				self.dy[i] = -self.dy[i]
			else:
				self.y[i] = ny
	def NextColor(self):
		nb = self.cb + self.db
		if (self.db>0 and nb>255) or (self.db<0 and nb<0):
			self.db = -self.db
			ng = self.cg + self.dg
			if (self.dg>0 and ng>255) or (self.dg<0 and ng<0):
				self.dg = -self.dg
				nr = self.cr + self.dr
				if (self.dr>0 and nr>255) or (self.dr<0 and nr<0):
					self.dr = -self.dr
				else:
					self.cr = nr
			else:
				self.cg = ng
		else:
			self.cb = nb

def PaQix2016TK_DoInit():
	pqs.Config(m_nClientWidth, m_nClientHeight)
	pqs.Init()

def PaQix2016TK_DoPaint():
	try:
		for i in range(conf__nCount):
			if i==5:
				pqs.Update(True)
			s1 = 1.0 * i / conf__nCount
			m_strColor = '#%02X%02X%02X' % (pqs.cr * s1, pqs.cg * s1, pqs.cb * s1)
			objCanvas.itemconfig(A_lines[i], fill=m_strColor)
			objCanvas.coords(A_lines[i], (pqs.x[0], pqs.y[0], pqs.x[1], pqs.y[1]))
			pqs.Move()
		pqs.NextColor()
		pqs.Update(False)
	except:
		print 'Exception.'

def PaQix2016TK_LButtonDown(event):
	PaQix2016TK_DoInit()

def PaQix2016TK_OnTimer():
	while m_isRunning:
		time.sleep(0.02)
		PaQix2016TK_DoPaint()

def PaQix2016TK_OnDestroy():
	global m_isRunning
	m_isRunning = False
	objThread.join()
	objFrame.destroy()
	print 'Destroy.'

def PaQix2016TK_OnResize(event):
	global m_nClientWidth, m_nClientHeight
	if(event.width!=m_nClientWidth) or (event.height!=m_nClientHeight):
		m_nClientWidth = event.width
		m_nClientHeight = event.height
		PaQix2016TK_DoInit()


if __name__ == '__main__':
	pqs = PaQixDef()

	objFrame = Tk('PaQix2016TK.py')
	objFrame.title('PaQix2016TK.py')

	objCanvas = Canvas(objFrame, width=m_nClientWidth, height=m_nClientHeight, bg='#000000', bd=0)
	objCanvas.pack(expand=YES, fill=BOTH)

	A_lines = [None for i in xrange(conf__nCount)]
	objCanvas.delete('all')
	for i in range(conf__nCount):
		A_lines[i] = objCanvas.create_line(0, 0, 1, 1)

	PaQix2016TK_DoInit()
	PaQix2016TK_DoPaint()

	objThread = Timer(m_nTimerInterval, PaQix2016TK_OnTimer)
	objThread.start()

	objFrame.bind('<Button-1>', PaQix2016TK_LButtonDown)
	objFrame.bind('<Configure>', PaQix2016TK_OnResize)
	objFrame.protocol('WM_DELETE_WINDOW', PaQix2016TK_OnDestroy)

	mainloop()
