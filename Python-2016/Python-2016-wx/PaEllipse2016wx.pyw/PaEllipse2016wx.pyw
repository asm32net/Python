#!/usr/bin/python
# -*- coding: utf-8 -*-

# Python 2.7
# PaEllipse2016wx.pyw

import wx, math

conf__nCount = 40
conf__strColor = '#FFFF00'
conf__strBackgroundColor = '#000000'
PI2 = math.pi * 2



class PaEllipseDef:
	x, y, a, b, angle, rotate = (0, 0, 0, 0, 0, 0)
	def __init__(self):
		pass
	def __init__(self, x, y, a, b, angle, rotate):
		self.x = x
		self.y = y
		self.a = a
		self.b = b
		self.angle = angle
		self.rotate = rotate

class PaEllipse2016wx(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, title='PaEllipse2016wx.pyw', size=(600, 450))
		self.SetBackgroundColour(conf__strBackgroundColor)

		self.m_nClientWidth, self.m_nClientHeight = self.GetClientSize()

		self.m_bmMemory = None
		self.objPen = wx.Pen(conf__strColor, 1, wx.SOLID)
		self.objBrush = wx.Brush(conf__strColor)
		self.objTimer = wx.Timer(self)

		self.m_fStartAngle = 0
		self.pes1 = PaEllipseDef(0, 0, 300, 75, 0, 0)
		self.pes2 = PaEllipseDef(0, 0, 50, 200, 0, 0)


		self.Bind(wx.EVT_PAINT, self.OnPaint)
		self.Bind(wx.EVT_SIZE, self.OnResize)
		self.Bind(wx.EVT_WINDOW_DESTROY, self.OnDestroy)
		self.Bind(wx.EVT_TIMER, self.OnTimer, self.objTimer)

		self.objTimer.Start(50)

	def _rotate(self, x, y, angle):
		sin1 = math.sin(angle)
		cos1 = math.cos(angle)
		x1, y1 = (x, y)
		x = cos1 * x1 + sin1 * y1
		y = cos1 * y1 - sin1 * x1
		return (x, y)

	def DoInit(self):
		self.m_nClientWidth, self.m_nClientHeight = self.GetClientSize()
		self.m_bmMemory = wx.EmptyBitmap(self.m_nClientWidth, self.m_nClientHeight)
		self.DoDisplay()

	def DoDisplay(self):
		m_dcMemory = wx.BufferedDC(None, self.m_bmMemory)
		m_dcMemory.SetBackground(wx.Brush(conf__strBackgroundColor))
		m_dcMemory.Clear()
		m_dcMemory.SetPen(self.objPen)
		m_dcMemory.SetBrush(self.objBrush)

		x0 = self.m_nClientWidth / 2
		y0 = self.m_nClientHeight / 2
		fStep = PI2 / conf__nCount
		r = d = 0
		for i in range(conf__nCount):
			angle1 = i * fStep
			sin1 = math.sin(angle1 + self.m_fStartAngle)
			cos1 = math.cos(angle1 + self.m_fStartAngle)
			r = r==3 and 6 or 3 # r = r==3 ? 6 : 3
			d = r + r
			x1 = self.pes1.a * sin1
			y1 = self.pes1.b * cos1
			x1, y1 = self._rotate(x1, y1, self.m_fStartAngle)
			x1 += x0
			y1 += y0
			m_dcMemory.DrawEllipse(x1 - r, y1- r, d, d)
			x1 = self.pes2.a * sin1
			y1 = self.pes2.b * cos1
			x1, y1 = self._rotate(x1, y1, self.m_fStartAngle)
			x1 += x0
			y1 += y0
			m_dcMemory.DrawEllipse(x1 - r, y1- r, d, d)
		self.Refresh(False)

	def OnPaint(self, event):
		wx.BufferedPaintDC(self, self.m_bmMemory)

	def OnResize(self, event):
		self.DoInit()

	def OnDestroy(self, event):
		self.objTimer.Stop()

	def OnTimer(self, event):
		self.m_fStartAngle += PI2 / 160
		if(self.m_fStartAngle>=PI2):
			self.m_fStartAngle=0
		self.DoDisplay()

if __name__ == '__main__':
	app = wx.App()
	ex = PaEllipse2016wx()
	ex.Show()
	app.MainLoop()
