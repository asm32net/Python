#!/usr/bin/python
# -*- coding: utf-8 -*-

# PaTriangle2016wx.py

import wx
import random

conf__nCount = 150
conf__strBackgroundColor = '#000000'

class PaTriangleDef():
	def __init__(self):
		self.x, self.y, self.dx, self.dy = ([0] * 6, [0] * 6, [0] * 6, [0] * 6)
		self.cr = self.cg = self.cb = 255
		self.dr = self.dg= self.db = 5

		self.m_nClientWidth = 0
		self.m_nClientHeight = 0

	def Config(self, nClientWidth, nClientHeight):
		self.m_nClientWidth = nClientWidth
		self.m_nClientHeight = nClientHeight

	def Init(self):
		for i in range(3):
			self.x[i] = random.randint(0, self.m_nClientWidth)
			self.y[i] = random.randint(0, self.m_nClientHeight)
			self.dx[i] = random.randint(2, 5)
			self.dy[i] = random.randint(2, 5)
		self.cr = random.randint(0, 255)
		self.cg = random.randint(0, 255)
		self.cb = random.randint(0, 255)

	def Update(self, isUpdate):
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

	def Move(self):
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


class PaTriangle2016wx(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, title='PaTriangle2016wx.pyw', size=(600, 450))
		self.SetBackgroundColour(conf__strBackgroundColor)
		self.m_nClientWidth, self.m_nClientHeight = self.GetClientSize()

		self.m_bmMemory = None
		self.objTimer = wx.Timer(self)

		self.Bind(wx.EVT_PAINT, self.OnPaint)
		self.Bind(wx.EVT_SIZE, self.OnSize)
		self.Bind(wx.EVT_LEFT_DOWN, self.OnLButtonDown)
		self.Bind(wx.EVT_WINDOW_DESTROY, self.OnDestroy)

		self.Bind(wx.EVT_TIMER, self.OnTimer, self.objTimer)

		self.objTimer.Start(10)
		self.pts = PaTriangleDef()
		self.pts.Config(self.m_nClientWidth, self.m_nClientHeight)

	def DoInit(self):
		self.m_nClientWidth, self.m_nClientHeight = self.GetClientSize()
		self.m_bmMemory = wx.EmptyBitmap(self.m_nClientWidth, self.m_nClientHeight)
		self.pts.Config(self.m_nClientWidth, self.m_nClientHeight)
		self.pts.Init()
		self.DoDisplay()

	def DoDisplay(self):
		m_dcMemory = wx.BufferedDC(None, self.m_bmMemory)
		m_dcMemory.SetBackground(wx.Brush(conf__strBackgroundColor))
		m_dcMemory.Clear()

		for i in xrange(conf__nCount):
			if i == 5:
				self.pts.Update(True)
			s1 = 1.0 * i / conf__nCount
			m_strColor = '#%02X%02X%02X' % (self.pts.cr * s1, self.pts.cg * s1, self.pts.cb * s1)
			pen1 = wx.Pen(m_strColor, 1, wx.SOLID)
			m_dcMemory.SetPen(pen1)
			m_dcMemory.DrawLine(self.pts.x[0], self.pts.y[0], self.pts.x[1], self.pts.y[1])
			m_dcMemory.DrawLine(self.pts.x[1], self.pts.y[1], self.pts.x[2], self.pts.y[2])
			m_dcMemory.DrawLine(self.pts.x[2], self.pts.y[2], self.pts.x[0], self.pts.y[0])
			self.pts.Move()
		self.pts.Update(False)
		self.pts.NextColor()
		self.Refresh(False)

	def OnPaint(self, event):
		wx.BufferedPaintDC(self, self.m_bmMemory)

	def OnSize(self, event):
		self.DoInit()

	def OnLButtonDown(self, event):
		self.pts.Init()
		self.DoDisplay()

	def OnDestroy(self, event):
		self.objTimer.Stop()

	def OnTimer(self, event):
		self.DoDisplay()

if __name__ == '__main__':
	app = wx.App()
	ex = PaTriangle2016wx()
	ex.Show()
	app.MainLoop()
