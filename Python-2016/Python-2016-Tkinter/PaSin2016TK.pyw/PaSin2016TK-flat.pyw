#!/usr/bin/python
# -*- coding:utf-8 -*-

# Python 2.7
# PaSin2016TK.py

from Tkinter import *
from threading import Timer
import random
import time
import math


m_nClientWidth = 600
m_nClientHeight = 450
m_nTimerInterval = 0.1
m_nCount = 200
m_nOffset = 0
PI2 = math.pi * 2
m_strColor = '#00FF00'
m_isRunning = True
m_nStartY = 0
m_nSizeY = 0
m_nWidth1 = 0


def PaSin2016TK_OnInit():
	objCanvas.delete('all')
	for i in xrange(m_nCount):
		A_rects[i] = objCanvas.create_rectangle(0, 0, 1, 1, fill=m_strColor, width=0)

def PaSin2016TK_OnDestroy():
	global m_isRunning
	m_isRunning = False
	objThread.join()
	objFrame.destroy()
	print 'Destroy.'

def PaSin2016TK_OnTimer():
	global m_nOffset
	while m_isRunning:
		time.sleep(0.02)
		m_nOffset = (m_nOffset + 5) % m_nCount
		PaSin2016TK_OnPaint()

def PaSin2016TK_OnPaint():
	#print 'PaSin2016TK_OnPaint()'
	try:
		for i in xrange(m_nCount):
			m_nStartX = m_nClientWidth * i / m_nCount
			sin1 = math.sin(PI2 * (i + m_nOffset) / m_nCount)
			m_nHeight1 = sin1 * m_nSizeY
			m_nOffsetY = m_nHeight1 * 0.9
			m_nStartY1 = m_nStartY - m_nOffsetY
			objCanvas.coords(A_rects[i], (m_nStartX, m_nStartY1, m_nStartX + m_nWidth1, m_nStartY1 - m_nHeight1 * 0.1))
	except Exception, e:
		print "Exception.", e


def PaSin2016TK_OnResize(event):
	global m_nClientWidth, m_nClientHeight
	global m_nStartY, m_nSizeY, m_nWidth1
	if(event.width!=m_nClientWidth) or (event.height!=m_nClientHeight):
		m_nClientWidth = event.width
		m_nClientHeight = event.height

		m_nStartY = m_nClientHeight / 2
		m_nSizeY = m_nClientHeight / 2
		m_nWidth1 = m_nClientWidth / m_nCount / 2
		print m_nClientWidth, m_nClientHeight

		#PaSin2016TK_OnInit()


if __name__ == '__main__':
	objFrame = Tk('PaSin2016TK.py')
	objFrame.title('PaSin2016TK.py')
	objCanvas = Canvas(objFrame, width=m_nClientWidth, height=m_nClientHeight, bg='#000000', bd=0)
	objCanvas.pack(expand=YES, fill=BOTH)

	A_rects = [None for i in xrange(m_nCount)]

	PaSin2016TK_OnInit()

	objFrame.bind('<Configure>', PaSin2016TK_OnResize)
	objFrame.protocol('WM_DELETE_WINDOW', PaSin2016TK_OnDestroy)

	objThread = Timer(m_nTimerInterval,PaSin2016TK_OnTimer)
	objThread.start()

	mainloop()
