#!/usr/bin/python
# -*- coding:utf-8 -*-

# Python 2.7
# PaTriangle2016TK.py

from Tkinter import *
from threading import Timer
import random
import time


conf__nCount = 100
m_nTimerInterval = 0.1
m_nClientWidth, m_nClientHeight = 600, 450
m_isRunning = True

class PaTriangleDef():
	def __init__(self):
		self.x = [0, 0, 0, 0, 0, 0]
		self.y = [0, 0, 0, 0, 0, 0]
		self.dx = [0, 0, 0, 0, 0, 0]
		self.dy = [0, 0, 0, 0, 0, 0]
		self.cr = self.cg = self.cb = 255
		self.dr = self.dg= self.db = 5

	def Config(self, nClientWidth, nClientHeight):
		self.m_nClientWidth = nClientWidth
		self.m_nClientHeight = nClientHeight

	def init(self):
		for i in range(3):
			self.x[i] = random.randint(0, self.m_nClientWidth)
			self.y[i] = random.randint(0, self.m_nClientHeight)
			self.dx[i] = random.randint(2, 5)
			self.dy[i] = random.randint(2, 5)
		self.cr = random.randint(0, 255)
		self.cg = random.randint(0, 255)
		self.cb = random.randint(0, 255)

	def update(self, isUpdate):
		for i in range(3):
			if isUpdate:
				from1 = i
				to1 = i + 3
			else:
				from1 = i + 3
				to1 = i
			self.x[to1] = self.x[from1]
			self.y[to1] = self.y[from1]
			self.dx[to1] = self.dx[from1]
			self.dy[to1] = self.dy[from1]

	def move(self):
		for i in range(3):
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



pts = PaTriangleDef()
#pts.init()

def PaTriangle2016TK_OnTimer():
	while m_isRunning:
		time.sleep(0.02)
		PaTriangle2016TK_DoPaint()

def PaTriangle2016TK_DoPaint():
	global m_nClientWidth, m_nClientHeight
	try:
		for i in xrange(conf__nCount):
			if i==5:
				pts.update(True)
			objCanvas.coords(A_lines[i], (pts.x[0], pts.y[0], pts.x[1], pts.y[1], pts.x[2], pts.y[2], pts.x[0], pts.y[0]))
			s1 = 1.0 * i / conf__nCount
			m_strColor = '#%02X%02X%02X' % (pts.cr * s1, pts.cg * s1, pts.cb * s1)
			objCanvas.itemconfig(A_lines[i], fill=m_strColor)
			pts.move()
		pts.NextColor()
		pts.update(False)
	except:
		print "Exception: PaTriangle2016TK_DoPaint()"

def PaTriangle2016TK_LButtonDown(event):
	PaTriangle2016TK_DoInit()

def PaTriangle2016TK_DoInit():
	pts.Config(m_nClientWidth, m_nClientHeight)
	pts.init()

def PaTriangle2016TK_DoDestroy():
	global m_isRunning
	m_isRunning = False
	objThread.join()
	objFrame.destroy()
	print "Destory"

def PaTriangle2016TK_Resize(event):
	global m_nClientWidth, m_nClientHeight
	if(event.width!=m_nClientWidth) or (event.height!=m_nClientHeight):
		m_nClientWidth = event.width
		m_nClientHeight = event.height
		PaTriangle2016TK_DoInit()


if __name__ == '__main__':
	objFrame = Tk('PaTriangle2016TK.py')
	objFrame.title('PaTriangle2016TK.py')
	#objFrame.geometry('600x450')

	objCanvas = Canvas(objFrame, width=m_nClientWidth, height=m_nClientHeight, bg='#000000', bd=0)
	objCanvas.pack(expand=YES, fill=BOTH)

	A_lines = [None for i in xrange(conf__nCount)]
	objCanvas.delete("all")
	for i in range(conf__nCount):
		A_lines[i] = objCanvas.create_line(0, 0, 1, 1, width=1)

	PaTriangle2016TK_DoInit()

	#PaTriangle2016TK_DoPaint()


	objFrame.bind('<Button-1>', PaTriangle2016TK_LButtonDown)
	objFrame.bind('<Configure>', PaTriangle2016TK_Resize)
	objFrame.protocol('WM_DELETE_WINDOW',PaTriangle2016TK_DoDestroy)

	objThread = Timer(m_nTimerInterval,PaTriangle2016TK_OnTimer)
	objThread.start()

	mainloop()
