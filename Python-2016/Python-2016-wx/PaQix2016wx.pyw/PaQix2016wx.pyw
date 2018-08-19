#!/usr/bin/python
# -*- coding: utf-8 -*-

# Python 2.7
# PaQix2016wx.pyw

import wx, random

conf__nCount = 200
conf__strBackgroundColor = '#000000'

class PaQixDef():
	def __init__(self):
		self.x = [0, 0, 0, 0]
		self.y = [0, 0, 0, 0]
		self.dx = [0, 0, 0, 0]
		self.dy = [0, 0, 0, 0]
		self.cr = self.cg = self.cb = 255
		self.dr = self.dg = self.db = 5

	def Config(self, nClientWidth, nClientHeight):
		self.m_nClientWidth = nClientWidth
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

class PaQix2016wx(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, title='PaQix2016wx.pyw', size=(600, 450))
		self.SetBackgroundColour(conf__strBackgroundColor)

		self.pqs = PaQixDef()
		self.m_nClientWidth, self.m_nClientHeight = self.GetClientSize()

		self.m_bmMemory = None
		self.objTimer = wx.Timer(self)

		self.Bind(wx.EVT_PAINT, self.OnPaint)
		self.Bind(wx.EVT_SIZE, self.OnResize)
		self.Bind(wx.EVT_LEFT_DOWN, self.OnLButtonDown)
		self.Bind(wx.EVT_WINDOW_DESTROY, self.OnDestroy)
		self.Bind(wx.EVT_TIMER, self.OnTimer, self.objTimer)

		self.objTimer.Start(10)

	def DoInit(self):
		self.m_nClientWidth, self.m_nClientHeight = self.GetClientSize()
		self.m_bmMemory = wx.EmptyBitmap(self.m_nClientWidth, self.m_nClientHeight)
		self.pqs.Config(self.m_nClientWidth, self.m_nClientHeight)
		self.pqs.Init()
		self.DoDisplay()

	def DoDisplay(self):
		m_dcMemory = wx.BufferedDC(None, self.m_bmMemory)
		m_dcMemory.SetBackground(wx.Brush(conf__strBackgroundColor))
		m_dcMemory.Clear()

		for i in range(conf__nCount):
			if i==5:
				self.pqs.Update(True)
			s1 = 1.0 * i / conf__nCount
			m_strColor = '#%02X%02X%02X' % (self.pqs.cr * s1, self.pqs.cg * s1, self.pqs.cb * s1)
			objPen = wx.Pen(m_strColor, 1, wx.SOLID)
			m_dcMemory.SetPen(objPen)
			m_dcMemory.DrawLine(self.pqs.x[0], self.pqs.y[0], self.pqs.x[1], self.pqs.y[1])
			self.pqs.Move()
		self.pqs.Update(False)
		self.pqs.NextColor()
		self.Refresh(False)

	def OnPaint(self, event):
		wx.BufferedPaintDC(self, self.m_bmMemory)

	def OnResize(self, event):
		self.DoInit()

	def OnLButtonDown(self, event):
		self.pqs.Init()
		self.DoDisplay()

	def OnDestroy(self, event):
		self.objTimer.Stop()

	def OnTimer(self, event):
		self.DoDisplay()


if __name__ == '__main__':
	app = wx.App()
	ex = PaQix2016wx()
	ex.Show()
	app.MainLoop()
