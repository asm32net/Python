#!/usr/bin/python
# -*- encoding: utf-8 -*-

#filename: PaStars2016wx.pyw

import wx
import math, random

conf__nCount = 30
conf__strBackgroundColor = '#000000'
PI2 = math.pi * 2
m_nSelected = 0

class Star2016Def:
	def __init__(self):
		self.cx = self.cy= self.r = 0
		self.strColor = '#FFFFFF'
		self.pts = [wx.Point() for i in xrange(10)]

	def Init(self, r, cx, cy):
		self.r, self.cx, self.cy = (r, cx, cy)
		r2 = r / 2
		a1 = PI2 / 10
		for i in range(5):
			n = i + i
			a2 = PI2 * i / 5
			self.pts[n].Set(cx + math.sin(a2) * r, cy - math.cos(a2) * r)
			a2 += a1
			self.pts[n+1].Set(cx + math.sin(a2) * r2, cy - math.cos(a2) * r2)
		self.strColor = '#%02X%02X%02X' % (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def PaStars2016wx_SetItem(i):
	r = 20 + random.randint(0, m_nClientWidth/20)
	A_objStart[i].Init(r,
		r + random.randint(0, m_nClientWidth - r - r),
		r + random.randint(0, m_nClientHeight - r - r))

def PaStars2016wx_DoInit():
	for i in range(conf__nCount):
		PaStars2016wx_SetItem(i)
	PaStars2016wx_DoDisplay()

def PaStars2016wx_DoDisplay():
	m_dcMemory = wx.BufferedDC(None, m_bmMemory)
	m_dcMemory.SetBackground(wx.Brush(conf__strBackgroundColor))
	m_dcMemory.Clear()

	for i in range(conf__nCount):
		m_strColor = A_objStart[i].strColor
		pen1 = wx.Pen(m_strColor, 1, wx.SOLID)
		brush1 = wx.Brush(m_strColor)
		m_dcMemory.SetPen(pen1)
		m_dcMemory.SetBrush(brush1)
		m_dcMemory.DrawPolygon(A_objStart[i].pts, xoffset=0, yoffset=0, fillStyle=wx.ODDEVEN_RULE)
	objFrame.Refresh(False)

def PaStars2016wx_OnPaint(event):
	wx.BufferedPaintDC(objFrame, m_bmMemory)

def PaStars2016wx_OnResize(event):
	global m_nClientWidth, m_nClientHeight, m_bmMemory
	m_nClientWidth, m_nClientHeight = objFrame.GetClientSize()
	m_bmMemory = wx.EmptyBitmap(m_nClientWidth, m_nClientHeight)
	PaStars2016wx_DoInit()

def PaStars2016wx_LButtonDown(event):
	PaStars2016wx_DoInit()

def PaStars2016wx_OnDestroy(event):
	objTimer.Stop()

def PaStars2016wx_OnTimer(event):
	global m_nSelected
	m_nSelected = (m_nSelected + 1) % conf__nCount
	PaStars2016wx_SetItem(m_nSelected)
	PaStars2016wx_DoDisplay()


if __name__ == '__main__':
	app = wx.App()
	objFrame = wx.Frame(None, title='PaStars2016wx.pyw', size=(600, 450))
	objFrame.SetBackgroundColour(conf__strBackgroundColor)

	m_nClientWidth, m_nClientHeight = objFrame.GetClientSize()

	m_bmMemory = None
	objTimer = wx.Timer(objFrame)
	A_objStart = [Star2016Def() for n in xrange(conf__nCount)]
	for i in range(conf__nCount):
		PaStars2016wx_SetItem(i)

	objFrame.Bind(wx.EVT_PAINT, PaStars2016wx_OnPaint)
	objFrame.Bind(wx.EVT_SIZE, PaStars2016wx_OnResize)
	objFrame.Bind(wx.EVT_LEFT_DOWN, PaStars2016wx_LButtonDown)
	objFrame.Bind(wx.EVT_WINDOW_DESTROY, PaStars2016wx_OnDestroy)
	objFrame.Bind(wx.EVT_TIMER, PaStars2016wx_OnTimer, objTimer)

	objTimer.Start(200)

	objFrame.Show()
	app.MainLoop()
