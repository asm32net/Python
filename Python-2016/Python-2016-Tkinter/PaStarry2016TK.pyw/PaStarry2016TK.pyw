#!/usr/bin/python
# -*- coding:utf-8 -*-

# Python 2.7
# PaStarry2016TK.py

from Tkinter import *
from threading import Timer
import random
import time

conf__nCount = 150

class PaStarry():
	def __init__(self):
		self.x1 = self.y1 = self.x2 = self.y2 = 0
		self.cr = self.cg = self.cb = 255

class PaStarry2016TK(Tk):
	def __init__(self):
		Tk.__init__(self, None)

		m_nTimerInterval = 0.02
		self.m_nClientWidth, self.m_nClientHeight = 600, 450
		self.m_isRunning = True
		self.m_nSelected = 0

		self.title('PaStarry2016TK.py')

		self.objCanvas = Canvas(self, width=self.m_nClientWidth, height=self.m_nClientHeight, bg='#000000', bd=0)
		self.objCanvas.pack(expand=YES, fill=BOTH)

		self.A_objItem = [PaStarry() for i in xrange(conf__nCount)]
		self.A_ovals = [None for i in xrange(conf__nCount)]

		self.DoInit()

		self.bind('<Button-1>', self.OnLButtonDown)
		self.bind('<Configure>', self.OnResize)
		self.protocol('WM_DELETE_WINDOW', self.OnDestroy)

		self.objThread = Timer(m_nTimerInterval, self.OnTimer)
		self.objThread.start()


	def SetItem(self, i):
		d = random.randint(2, 5)
		self.A_objItem[i].x1 = random.randint(0, self.m_nClientWidth - d)
		self.A_objItem[i].y1 = random.randint(0, self.m_nClientHeight - d)
		self.A_objItem[i].x2 = self.A_objItem[i].x1 + d
		self.A_objItem[i].y2 = self.A_objItem[i].y1 + d
		self.A_objItem[i].cr = random.randint(0, 255) # 0 <= rand <= 255
		self.A_objItem[i].cg = random.randint(0, 255) # 0 <= rand <= 255
		self.A_objItem[i].cb = random.randint(0, 255) # 0 <= rand <= 255

	def DoInit(self):
		self.objCanvas.delete('all')
		for i in range(conf__nCount):
			self.SetItem(i)
			m_strColor = '#%02X%02X%02X' % (self.A_objItem[i].cr, self.A_objItem[i].cg, self.A_objItem[i].cb)
			self.A_ovals[i] = self.objCanvas.create_oval(self.A_objItem[i].x1, self.A_objItem[i].y1,
					self.A_objItem[i].x2, self.A_objItem[i].y2, fill=m_strColor, width=0)

	def OnLButtonDown(self, event):
		self.DoInit()

	def OnDestroy(self):
		self.m_isRunning = False
		self.objThread.join()
		self.destroy()
		print "Destroy."

	def OnTimer(self):
		while self.m_isRunning:
			time.sleep(0.02)
			self.m_nSelected = (self.m_nSelected + 1) % conf__nCount
			self.SetItem(self.m_nSelected)
			m_strColor = '#%02X%02X%02X' % (self.A_objItem[self.m_nSelected].cr,
				self.A_objItem[self.m_nSelected].cg, self.A_objItem[self.m_nSelected].cb)
			try:
				self.objCanvas.coords(self.A_ovals[self.m_nSelected], (
					self.A_objItem[self.m_nSelected].x1, self.A_objItem[self.m_nSelected].y1,
					self.A_objItem[self.m_nSelected].x2, self.A_objItem[self.m_nSelected].y2))
				self.objCanvas.itemconfig(self.A_ovals[self.m_nSelected], fill=m_strColor)
			except:
				del m_strColor

	def OnResize(self, event):
		if(event.width!=self.m_nClientWidth) or (event.height!=self.m_nClientHeight):
			self.m_nClientWidth = event.width
			self.m_nClientHeight = event.height
			self.DoInit()


if __name__ == '__main__':
	PaStarry2016TK()
	mainloop()
