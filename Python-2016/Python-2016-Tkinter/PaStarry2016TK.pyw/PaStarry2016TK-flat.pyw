#!/usr/bin/python
# -*- coding:utf-8 -*-

# Python 2.7
# PaStarry2016TK.py

from Tkinter import *
from threading import Timer
import random
import time

conf__nCount = 150

m_nClientWidth = 600
m_nClientHeight = 450
m_nTimerInterval = 0.02
m_isRunning = True
m_nSelected = 0

class PaStarry():
	def __init__(self):
		self.x1 = self.y1 = self.x2 = self.y2 = 0
		self.cr = self.cg = self.cb = 255

def PaStarry2016TK_SetItem(i):
	d = random.randint(2, 5)
	A_objItem[i].x1 = random.randint(0, m_nClientWidth - d)
	A_objItem[i].y1 = random.randint(0, m_nClientHeight - d)
	A_objItem[i].x2 = A_objItem[i].x1 + d
	A_objItem[i].y2 = A_objItem[i].y1 + d
	A_objItem[i].cr = random.randint(0, 255) # 0 <= rand <= 255
	A_objItem[i].cg = random.randint(0, 255) # 0 <= rand <= 255
	A_objItem[i].cb = random.randint(0, 255) # 0 <= rand <= 255

def PaStarry2016TK_DoInit():
	objCanvas.delete('all')
	for i in range(conf__nCount):
		PaStarry2016TK_SetItem(i)
		m_strColor = '#%02X%02X%02X' % (A_objItem[i].cr, A_objItem[i].cg, A_objItem[i].cb)
		A_ovals[i] = objCanvas.create_oval(A_objItem[i].x1, A_objItem[i].y1,
				A_objItem[i].x2, A_objItem[i].y2, fill=m_strColor, width=0)

def PaStarry2016TK_LButtonDown(event):
	PaStarry2016TK_DoInit()

def PaStarry2016TK_OnDestroy():
	global m_isRunning
	m_isRunning = False
	objThread.join()
	objFrame.destroy()
	print "Destroy."

def PaStarry2016TK_Timer():
	global m_nSelected, m_nClientWidth, m_nClientHeight
	while m_isRunning:
		time.sleep(0.02)
		m_nSelected = (m_nSelected + 1) % conf__nCount
		PaStarry2016TK_SetItem(m_nSelected)
		m_strColor = '#%02X%02X%02X' % (A_objItem[m_nSelected].cr,
			A_objItem[m_nSelected].cg, A_objItem[m_nSelected].cb)
		try:
			objCanvas.coords(A_ovals[m_nSelected], (
				A_objItem[m_nSelected].x1, A_objItem[m_nSelected].y1,
				A_objItem[m_nSelected].x2, A_objItem[m_nSelected].y2))
			objCanvas.itemconfig(A_ovals[m_nSelected], fill=m_strColor)
		except:
			del m_strColor

def PaStarry2016TK_Resize(event):
	global m_nClientWidth, m_nClientHeight
	if(event.width!=m_nClientWidth) or (event.height!=m_nClientHeight):
		m_nClientWidth = event.width
		m_nClientHeight = event.height
		PaStarry2016TK_DoInit()


if __name__ == '__main__':
	objFrame = Tk('PaStarry2016TK.py')
	objFrame.title('PaStarry2016TK.py')

	objCanvas = Canvas(objFrame, width=m_nClientWidth, height=m_nClientHeight, bg='#000000', bd=0)
	objCanvas.pack(expand=YES, fill=BOTH)

	A_objItem = [PaStarry() for i in xrange(conf__nCount)]
	A_ovals = [None for i in xrange(conf__nCount)]

	PaStarry2016TK_DoInit()

	objFrame.bind('<Button-1>', PaStarry2016TK_LButtonDown)
	objFrame.bind('<Configure>', PaStarry2016TK_Resize)
	objFrame.protocol('WM_DELETE_WINDOW', PaStarry2016TK_OnDestroy)

	objThread = Timer(m_nTimerInterval,PaStarry2016TK_Timer)
	objThread.start()

	mainloop()
