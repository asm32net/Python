#!/usr/bin/python
# -*- coding: utf-8 -*-

# Python 2.7
# PaClock2016wx.pyw

import wx, datetime, math

PI2 = math.pi * 2
conf__strColor = '#000000'
conf__strBackgroundColor = '#FFFFFF'

class PaClock2016wx(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, title='PaClock2016wx.pyw', size=(600, 450))
		self.SetBackgroundColour(conf__strBackgroundColor)

		self.m_nClientWidth, self.m_nClientHeight = self.GetClientSize()

		self.m_nClockRadius = self.m_nClockDiameter = self.m_nStartX = self.m_nStartY = 0

		self.objFont = wx.Font(24,
			wx.FONTFAMILY_DEFAULT,
			wx.FONTSTYLE_NORMAL,
			wx.FONTWEIGHT_BOLD,
			face='Arial Black')
		self.objPen3 = wx.Pen(conf__strColor, 3, wx.SOLID)
		self.objPen5 = wx.Pen(conf__strColor, 5, wx.SOLID)
		self.objPen7 = wx.Pen(conf__strColor, 7, wx.SOLID)
		self.m_bmFace = None
		self.m_dcFace = None
		self.m_bmMemory = None
		self.objTimer =wx.Timer(self)

		self.Bind(wx.EVT_PAINT, self.OnPaint)
		self.Bind(wx.EVT_SIZE, self.OnResize)
		self.Bind(wx.EVT_WINDOW_DESTROY, self.OnDestroy)
		self.Bind(wx.EVT_TIMER, self.OnTimer, self.objTimer)

		self.objTimer.Start(1000)

	def DoDisplay(self):
		m_dcMemory = wx.BufferedDC(None, self.m_bmMemory)
		m_dcMemory.SetBackground(wx.Brush(conf__strBackgroundColor))
		m_dcMemory.Clear()

		dt = datetime.datetime.now() # datetime.datetime(2016, 5, 22, 3, 17, 3, 203000)

		m_strDisplay = '%04d-%02d-%02d %02d:%02d:%02d' % (dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)
		m_dcMemory.SetBackgroundMode(wx.SOLID)
		m_dcMemory.SetTextBackground(conf__strBackgroundColor)
		m_dcMemory.SetTextForeground('#000000')
		m_dcMemory.DrawText(m_strDisplay, 0, 0)

		m_dcMemory.Blit(self.m_nStartX, self.m_nStartY, self.m_nClockDiameter, self.m_nClockDiameter, self.m_dcFace, 0, 0, wx.COPY)

		cx = self.m_nClientWidth / 2
		cy = self.m_nClientHeight / 2

		m_fStart = 0.08
		A_objPens = [self.objPen3, self.objPen5, self.objPen7]
		A_fEnd = [0.7, 0.5, 0.4]
		A_fAngle = [
			PI2 * dt.second / 60,
			PI2 * (60 * dt.minute + dt.second) / 3600,
			PI2 * (60 * ( 60 * ( dt.hour % 12 ) + dt.minute) + dt.second) / 43200]
		for i in range(3):
			dx1 = math.sin(A_fAngle[i]) * self.m_nClockRadius
			dy1 = math.cos(A_fAngle[i]) * self.m_nClockRadius
			m_dcMemory.SetPen(A_objPens[i])
			m_dcMemory.DrawLine(cx + dx1 * m_fStart, cy - dy1 * m_fStart,
				cx + dx1 * A_fEnd[i], cy - dy1 * A_fEnd[i])
		self.Refresh()

	def DoInit(self):
		self.m_nClientWidth, self.m_nClientHeight = self.GetClientSize()
		self.m_bmMemory = wx.EmptyBitmap(self.m_nClientWidth, self.m_nClientHeight)

		self.m_nClockRadius = (self.m_nClientHeight<self.m_nClientWidth and self.m_nClientHeight or self.m_nClientWidth) * 9 / 10 / 2
		self.m_nClockDiameter = self.m_nClockRadius + self.m_nClockRadius

		self.m_nStartX = (self.m_nClientWidth - self.m_nClockDiameter) / 2
		self.m_nStartY = (self.m_nClientHeight - self.m_nClockDiameter) / 2
		
		self.m_bmFace = wx.EmptyBitmap(self.m_nClockDiameter, self.m_nClockDiameter)
		self.m_dcFace = wx.BufferedDC(None, self.m_bmFace)
		self.m_dcFace.SetBackground(wx.Brush(conf__strBackgroundColor))
		self.m_dcFace.Clear()
		self.m_dcFace.SetPen(self.objPen7)
		self.m_dcFace.DrawEllipse(3, 3, self.m_nClockDiameter-7, self.m_nClockDiameter-7)
		self.m_dcFace.DrawEllipse(self.m_nClockRadius-5, self.m_nClockRadius-5, 10, 10)

		self.m_dcFace.SetFont(self.objFont)
		self.m_dcFace.SetTextForeground('#57B777')

		for i in range(60):
			angle1 = PI2 * i / 60
			dx1 = math.sin(angle1) * (self.m_nClockRadius - 7)
			dy1 = math.cos(angle1) * (self.m_nClockRadius - 7)
			s1 = 0
			if i % 5 == 0:
				s1 = 0.9
				self.m_dcFace.SetPen(self.objPen5)

				str1 = '%d' % (i / 5)
				self.m_dcFace.DrawText(str1,
					self.m_nClockRadius + dx1 * 0.8 - 10, self.m_nClockRadius - dy1 * 0.8 - 23)
			else:
				s1 = 0.94
				self.m_dcFace.SetPen(self.objPen3)
			self.m_dcFace.DrawLine(self.m_nClockRadius + dx1, self.m_nClockRadius + dy1,
				self.m_nClockRadius + dx1 * s1, self.m_nClockRadius + dy1 * s1)

		self.DoDisplay()

	def OnPaint(self, event):
		wx.BufferedPaintDC(self, self.m_bmMemory)

	def OnResize(self, event):
		self.DoInit()

	def OnDestroy(self, event):
		self.objTimer.Stop()

	def OnTimer(self, event):
		self.DoDisplay()

if __name__ == '__main__':
	app = wx.App()
	ex = PaClock2016wx()
	ex.Show()
	app.MainLoop()
