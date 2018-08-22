#!/usr/bin/python
# -*- encoding: utf-8 -*-

#filename: PaStars2016wx.pyw

import wx
import math, random

conf__nCount = 30
conf__strBackgroundColor = '#000000'
PI2 = math.pi * 2

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

class PaStars2016wx(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, title='PaStars2016wx.pyw', size=(600, 450))
		self.SetBackgroundColour(conf__strBackgroundColor)

		self.m_nClientWidth, self.m_nClientHeight = self.GetClientSize()

		self.m_nSelected = 0
		self.m_bmMemory = None
		self.objTimer = wx.Timer(self)
		self.A_objStart = [Star2016Def() for n in xrange(conf__nCount)]
		for i in range(conf__nCount):
			self.SetItem(i)

		self.Bind(wx.EVT_PAINT, self.OnPaint)
		self.Bind(wx.EVT_SIZE, self.OnSize)
		self.Bind(wx.EVT_LEFT_DOWN, self.OnLButtonDown)
		self.Bind(wx.EVT_WINDOW_DESTROY, self.OnDestroy)
		self.Bind(wx.EVT_TIMER, self.OnTimer, self.objTimer)

		self.objTimer.Start(200)

	def SetItem(self, i):
		r = 20 + random.randint(0, self.m_nClientWidth/20)
		self.A_objStart[i].Init(r,
			r + random.randint(0, self.m_nClientWidth - r - r),
			r + random.randint(0, self.m_nClientHeight - r - r))

	def DoInit(self):
		for i in range(conf__nCount):
			self.SetItem(i)
		self.DoDisplay()

	def DoDisplay(self):
		m_dcMemory = wx.BufferedDC(None, self.m_bmMemory)
		m_dcMemory.SetBackground(wx.Brush(conf__strBackgroundColor))
		m_dcMemory.Clear()

		for i in range(conf__nCount):
			m_strColor = self.A_objStart[i].strColor
			pen1 = wx.Pen(m_strColor, 1, wx.SOLID)
			brush1 = wx.Brush(m_strColor)
			m_dcMemory.SetPen(pen1)
			m_dcMemory.SetBrush(brush1)
			m_dcMemory.DrawPolygon(self.A_objStart[i].pts, xoffset=0, yoffset=0, fillStyle=wx.ODDEVEN_RULE)
		self.Refresh(False)

	def OnPaint(self, event):
		wx.BufferedPaintDC(self, self.m_bmMemory)

	def OnSize(self, event):
		self.m_nClientWidth, self.m_nClientHeight = self.GetClientSize()
		self.m_bmMemory = wx.EmptyBitmap(self.m_nClientWidth, self.m_nClientHeight)
		self.DoInit()

	def OnLButtonDown(self, event):
		self.DoInit()

	def OnDestroy(self, event):
		self.objTimer.Stop()

	def OnTimer(self, event):
		self.m_nSelected = (self.m_nSelected + 1) % conf__nCount
		self.SetItem(self.m_nSelected)
		self.DoDisplay()

if __name__ == '__main__':
	app = wx.App()
	ex = PaStars2016wx()
	ex.Show()
	app.MainLoop()
