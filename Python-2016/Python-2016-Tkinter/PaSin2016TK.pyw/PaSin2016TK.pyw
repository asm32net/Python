#!/usr/bin/python
# -*- coding:utf-8 -*-

# Python 2.7
# PaSin2016TK.py

from Tkinter import *
from threading import Timer
import random
import time
import math


conf__nCount = 200
conf__strColor = '#00FF00'
PI2 = math.pi * 2

class PaSin2016TK(Tk):
	def __init__(self):
		Tk.__init__(self, None)

		m_nTimerInterval = 0.1
		self.m_nClientWidth, self.m_nClientHeight  = 600, 450
		self.m_isRunning = True
		self.m_nOffset = 0
		self.m_nStartY = 0
		self.m_nSizeY = 0
		self.m_nWidth1 = 0

		self.title('PaSin2016TK.py')
		self.objCanvas = Canvas(self, width=self.m_nClientWidth, height=self.m_nClientHeight, bg='#000000', bd=0)
		self.objCanvas.pack(expand=YES, fill=BOTH)

		self.A_rects = [None for i in xrange(conf__nCount)]

		self.OnInit()

		self.bind('<Configure>', self.OnResize)
		self.protocol('WM_DELETE_WINDOW', self.OnDestroy)

		self.objThread = Timer(m_nTimerInterval, self.OnTimer)
		self.objThread.start()


	def OnInit(self):
		self.objCanvas.delete('all')
		for i in xrange(conf__nCount):
			self.A_rects[i] = self.objCanvas.create_rectangle(0, 0, 1, 1, fill=conf__strColor, width=0)

	def OnDestroy(self):
		self.m_isRunning = False
		self.objThread.join()
		self.destroy()
		print 'Destroy.'

	def OnTimer(self):
		while self.m_isRunning:
			time.sleep(0.02)
			self.m_nOffset = (self.m_nOffset + 5) % conf__nCount
			self.OnPaint()

	def OnPaint(self):
		#print 'self.OnPaint()'
		try:
			for i in xrange(conf__nCount):
				m_nStartX = self.m_nClientWidth * i / conf__nCount
				sin1 = math.sin(PI2 * (i + self.m_nOffset) / conf__nCount)
				m_nHeight1 = sin1 * self.m_nSizeY
				self.m_nOffsetY = m_nHeight1 * 0.9
				self.m_nStartY1 = self.m_nStartY - self.m_nOffsetY
				self.objCanvas.coords(self.A_rects[i], (m_nStartX, self.m_nStartY1, m_nStartX + self.m_nWidth1, self.m_nStartY1 - m_nHeight1 * 0.1))
		except Exception, e:
			#print "Exception.", e
			pass

	def OnResize(self, event):
		if(event.width!=self.m_nClientWidth) or (event.height!=self.m_nClientHeight):
			self.m_nClientWidth = event.width
			self.m_nClientHeight = event.height

			self.m_nStartY = self.m_nClientHeight / 2
			self.m_nSizeY = self.m_nClientHeight / 2
			self.m_nWidth1 = self.m_nClientWidth / conf__nCount / 2
			#print self.m_nClientWidth, self.m_nClientHeight
			#self.OnInit()


if __name__ == '__main__':
	PaSin2016TK()
	mainloop()
