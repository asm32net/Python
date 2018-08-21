#/usr/bin/python
# -*- coding:utf-8 -*-

#filename: PaStarry2016wx.pyw

import wx
import random


conf__nCount = 150
conf__strBackgroundColor = '#000000'

m_nSelected = 0


class PaStarry:
	def __init__(self):
		self.d = self.x = self.y = 10
		self.cr = self.cg = self.cb = 255

def PaStarry2016wx_SetItem(i):
	A_objItem[i].d = random.randint(2, 5)
	A_objItem[i].x = random.randint(0, m_nClientWidth - A_objItem[i].d)
	A_objItem[i].y = random.randint(0, m_nClientHeight - A_objItem[i].d)
	A_objItem[i].cr = random.randint(0, 255) # 0 <= rand <= 255
	A_objItem[i].cg = random.randint(0, 255) # 0 <= rand <= 255
	A_objItem[i].cb = random.randint(0, 255) # 0 <= rand <= 255

def PaStarry2016wx_DoInit():
	global m_nClientWidth, m_nClientHeight, m_bmMemory
	m_nClientWidth, m_nClientHeight = objFrame.GetClientSize()
	m_bmMemory = wx.EmptyBitmap(m_nClientWidth, m_nClientHeight)
	for i in range(conf__nCount):
		PaStarry2016wx_SetItem(i)
	PaStarry2016wx_DoDisplay()

def PaStarry2016wx_DoDisplay():
	m_dcMemory = wx.BufferedDC(None, m_bmMemory)
	m_dcMemory.SetBackground(wx.Brush(conf__strBackgroundColor))
	m_dcMemory.Clear()

	for i in range(conf__nCount):
		m_strColor = '#%02X%02X%02X' % (A_objItem[i].cr, A_objItem[i].cg, A_objItem[i].cb)
		pen1 = wx.Pen(m_strColor, 1, wx.SOLID)
		m_dcMemory.SetPen(pen1)
		brush1 = wx.Brush(m_strColor)
		m_dcMemory.SetBrush(brush1)
		m_dcMemory.DrawEllipse(A_objItem[i].x, A_objItem[i].y, A_objItem[i].d, A_objItem[i].d)
		print (A_objItem[i].x, A_objItem[i].y, A_objItem[i].d)
	objFrame.Refresh(False)

def PaStarry2016wx_OnPaint(event):
	wx.BufferedPaintDC(objFrame, m_bmMemory)

def PaStarry2016wx_OnResize(event):
	PaStarry2016wx_DoInit()

def PaStarry2016wx_LButtonDown(event):
	PaStarry2016wx_DoInit()

def PaStarry2016wx_OnDestroy(event):
	objTimer.Stop()

def PaStarry2016wx_OnTimer(event):
	global m_nSelected
	m_nSelected = (m_nSelected + 1) % conf__nCount
	PaStarry2016wx_SetItem(m_nSelected)
	PaStarry2016wx_DoDisplay()


if __name__ == '__main__':
	app = wx.App()
	objFrame = wx.Frame(None, title='PaStarry2016wx.py', size=(600, 450))
	objFrame.SetBackgroundColour(conf__strBackgroundColor)

	A_objItem = [PaStarry() for i in xrange(conf__nCount)]

	m_nClientWidth, m_nClientHeight = objFrame.GetClientSize()

	m_bmMemory = None
	objTimer = wx.Timer(objFrame)

	objFrame.Bind(wx.EVT_PAINT, PaStarry2016wx_OnPaint)
	objFrame.Bind(wx.EVT_SIZE, PaStarry2016wx_OnResize)
	objFrame.Bind(wx.EVT_LEFT_DOWN, PaStarry2016wx_LButtonDown)
	objFrame.Bind(wx.EVT_WINDOW_DESTROY, PaStarry2016wx_OnDestroy)
	objFrame.Bind(wx.EVT_TIMER, PaStarry2016wx_OnTimer, objTimer)

	objTimer.Start(20)

	objFrame.Show()
	app.MainLoop()
