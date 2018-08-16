#!/usr/bin/python
# -*- coding: utf-8 -*-

# Python 2.7
# PaDigitalClock2016wx.pyw

import wx, datetime

A_byteDigitMatrix = (
	254, 3, 253, 5, 251, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 3, 6, 1, 4, 0, 0, 1, 4, 
	3, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 251, 6, 253, 5, 254, 3, 0, 0, 0, 0, 1, 0, 
	3, 0, 7, 0, 7, 0, 7, 0, 7, 0, 7, 0, 3, 0, 1, 0, 0, 0, 1, 0, 3, 0, 7, 0, 7, 0, 
	7, 0, 7, 0, 7, 0, 3, 0, 1, 0, 0, 0, 0, 0, 254, 3, 253, 1, 251, 0, 7, 0, 7, 0, 
	7, 0, 7, 0, 7, 0, 3, 0, 253, 1, 254, 3, 252, 5, 0, 6, 0, 7, 0, 7, 0, 7, 0, 7, 
	0, 7, 248, 6, 252, 5, 254, 3, 0, 0, 254, 3, 253, 1, 251, 0, 7, 0, 7, 0, 7, 0, 
	7, 0, 7, 0, 3, 0, 253, 1, 254, 3, 253, 1, 3, 0, 7, 0, 7, 0, 7, 0, 7, 0, 7, 0, 
	251, 0, 253, 1, 254, 3, 0, 0, 0, 0, 1, 4, 3, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 
	3, 6, 253, 5, 254, 3, 253, 1, 3, 0, 7, 0, 7, 0, 7, 0, 7, 0, 7, 0, 3, 0, 1, 0, 
	0, 0, 0, 0, 254, 3, 252, 5, 248, 6, 0, 7, 0, 7, 0, 7, 0, 7, 0, 7, 0, 6, 252, 
	5, 254, 3, 253, 1, 3, 0, 7, 0, 7, 0, 7, 0, 7, 0, 7, 0, 251, 0, 253, 1, 254, 3, 
	0, 0, 254, 3, 252, 5, 248, 6, 0, 7, 0, 7, 0, 7, 0, 7, 0, 7, 0, 6, 252, 5, 254, 
	3, 253, 5, 3, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 251, 6, 253, 5, 254, 3, 0, 0, 
	254, 3, 253, 1, 251, 0, 7, 0, 7, 0, 7, 0, 7, 0, 7, 0, 3, 0, 1, 0, 0, 0, 1, 0, 
	3, 0, 7, 0, 7, 0, 7, 0, 7, 0, 7, 0, 3, 0, 1, 0, 0, 0, 0, 0, 254, 3, 253, 5, 
	251, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 3, 6, 253, 5, 254, 3, 253, 5, 3, 6, 7, 
	7, 7, 7, 7, 7, 7, 7, 7, 7, 251, 6, 253, 5, 254, 3, 0, 0, 254, 3, 253, 5, 251, 
	6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 3, 6, 253, 5, 254, 3, 253, 1, 3, 0, 7, 0, 7, 
	0, 7, 0, 7, 0, 7, 0, 251, 0, 253, 1, 254, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
	0, 112, 0, 112, 0, 112, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 112, 0, 112, 0, 112, 
	0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
	0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 112, 0, 112, 0, 
	112, 0, 0, 0, 0, 0)

m_strBackgroundColor = '#000000'
A_nMask = (2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1)


class PaDigitalClock2016wx(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, title='PaDigitalClock2016wx.pyw', size=(600, 450))
		self.SetBackgroundColour(m_strBackgroundColor)

		self.A_nDigits = [0 for i in xrange (12)]
		self.A_nDigits1 = [0 for i in xrange (12)]
		self.m_isRefresh = True
		self.m_nItemW = self.m_nItemH = self.m_nStartX = self.m_nStartY = 0

		self.objPen = wx.Pen('#FFFFFF', 1, wx.SOLID)
		self.objBrush = wx.Brush('#FFFFFF')

		self.m_bmDigits = None
		self.m_dcDigits = None
		self.m_nClientWidth, self.m_nClientHeight = self.GetClientSize()
		self.objTimer = wx.Timer(self)

		self.Bind(wx.EVT_PAINT, self.OnPaint)
		self.Bind(wx.EVT_SIZE, self.OnResize)
		self.Bind(wx.EVT_WINDOW_DESTROY, self.OnDestroy)
		self.Bind(wx.EVT_TIMER, self.OnTimer, self.objTimer)

		self.objTimer.Start(10)

	def DoDisplay(self):
		dt = datetime.datetime.now() # datetime.datetime(2016, 5, 22, 3, 17, 3, 203000)

		for i in range(12):
			self.A_nDigits1[i] = self.A_nDigits[i]

		m_nMillisecond = dt.microsecond / 1000 # 微妙转化成毫秒
		m_nSplitter = m_nMillisecond<500 and 10 or 12
		self.A_nDigits[0] = dt.hour / 10
		self.A_nDigits[1] = dt.hour % 10
		self.A_nDigits[2] = m_nSplitter
		self.A_nDigits[3] = dt.minute / 10
		self.A_nDigits[4] = dt.minute % 10
		self.A_nDigits[5] = m_nSplitter
		self.A_nDigits[6] = dt.second / 10
		self.A_nDigits[7] = dt.second % 10
		self.A_nDigits[8] = 11
		self.A_nDigits[9] = m_nMillisecond / 100
		self.A_nDigits[10] = m_nMillisecond % 100 / 10
		#self.A_nDigits[11] = m_nMillisecond % 10

		dc = wx.ClientDC(self)
		if self.m_isRefresh:
			dc.Clear()

		if self.m_isRefresh or self.A_nDigits1[7] != self.A_nDigits[7]:
			dc.SetBackgroundMode(wx.SOLID)
			dc.SetTextBackground(m_strBackgroundColor)
			dc.SetTextForeground('#FFFFFF')
			m_strDisplay = '%04d-%02d-%02d %02d:%02d:%02d' % (dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)
			dc.DrawText(m_strDisplay, 10, 10)

		m_nOffsetX = self.m_nStartX
		for i in range(11):
			if self.m_isRefresh or self.A_nDigits1[i] != self.A_nDigits[i]:
				dc.Blit(m_nOffsetX, self.m_nStartY, self.m_nItemW, self.m_nItemH, self.m_dcDigits, self.A_nDigits[i] * self.m_nItemW, 0, wx.COPY)
			m_nOffsetX += self.m_nItemW
		self.m_isRefresh = False

	def DoInit(self):
		self.m_nClientWidth, self.m_nClientHeight = self.GetClientSize()

		d = self.m_nClientWidth / 12 / 11 # 显示 12:00:00.00格式 (11字符,每个字符12点宽)
		if d<3 :
			d=3
		self.m_nItemW = d * 12
		self.m_nItemH = d * 22
		self.m_nStartX = (self.m_nClientWidth - self.m_nItemW * 11)/2
		self.m_nStartY = (self.m_nClientHeight - self.m_nItemH)/2
		m_nBitmapDigitW = self.m_nItemW * 13

		self.m_bmDigits = wx.EmptyBitmap(m_nBitmapDigitW, self.m_nItemH)
		self.m_dcDigits = wx.BufferedDC(None, self.m_bmDigits)
		self.m_dcDigits.SetBackground(wx.Brush('#0000FF'))
		self.m_dcDigits.Clear()
		self.m_dcDigits.SetPen(self.objPen)
		self.m_dcDigits.SetBrush(self.objBrush)
		m_nOffset=0
		for n in range(12):
			x = n * self.m_nItemW
			for i in range(22):
				ch = A_byteDigitMatrix[m_nOffset] | (A_byteDigitMatrix[m_nOffset+1]<<8)
				y = i * d
				for ii in range(12):
					if (ch & A_nMask[ii])>0:
						self.m_dcDigits.DrawEllipse(x + ii * d, y, d-2, d-2)
				m_nOffset += 2

		self.m_isRefresh = True
		self.Refresh(False)

	def OnPaint(self, event):
		self.m_isRefresh = True
		self.DoDisplay()

	def OnResize(self, event):
		self.DoInit()

	def OnDestroy(self, event):
		self.objTimer.Stop()

	def OnTimer(self, event):
		self.DoDisplay()


if __name__ == '__main__':
	app = wx.App()
	ex = PaDigitalClock2016wx()
	ex.Show()
	app.MainLoop()
