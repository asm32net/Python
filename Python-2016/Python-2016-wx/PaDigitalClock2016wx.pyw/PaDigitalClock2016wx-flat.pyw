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

A_nDigits = [0 for i in xrange (12)]
A_nDigits1 = [0 for i in xrange (12)]
m_isRefresh = True
m_nItemW = m_nItemH = m_nStartX = m_nStartY = 0

def PaDigitalClock2016wx_DoDisplay():
	global m_isRefresh
	dt = datetime.datetime.now() # datetime.datetime(2016, 5, 22, 3, 17, 3, 203000)

	for i in range(12):
		A_nDigits1[i] = A_nDigits[i]

	m_nMillisecond = dt.microsecond / 1000 # 微妙转化成毫秒
	m_nSplitter = m_nMillisecond<500 and 10 or 12
	A_nDigits[0] = dt.hour / 10
	A_nDigits[1] = dt.hour % 10
	A_nDigits[2] = m_nSplitter
	A_nDigits[3] = dt.minute / 10
	A_nDigits[4] = dt.minute % 10
	A_nDigits[5] = m_nSplitter
	A_nDigits[6] = dt.second / 10
	A_nDigits[7] = dt.second % 10
	A_nDigits[8] = 11
	A_nDigits[9] = m_nMillisecond / 100
	A_nDigits[10] = m_nMillisecond % 100 / 10
	#A_nDigits[11] = m_nMillisecond % 10

	dc = wx.ClientDC(objFrame)
	if m_isRefresh:
		dc.Clear()

	if m_isRefresh or A_nDigits1[7] != A_nDigits[7]:
		dc.SetBackgroundMode(wx.SOLID)
		dc.SetTextBackground(m_strBackgroundColor)
		dc.SetTextForeground('#FFFFFF')
		m_strDisplay = '%04d-%02d-%02d %02d:%02d:%02d' % (dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)
		dc.DrawText(m_strDisplay, 10, 10)

	m_nOffsetX = m_nStartX
	for i in range(11):
		if m_isRefresh or A_nDigits1[i] != A_nDigits[i]:
			dc.Blit(m_nOffsetX, m_nStartY, m_nItemW, m_nItemH, m_dcDigits, A_nDigits[i] * m_nItemW, 0, wx.COPY)
		m_nOffsetX += m_nItemW
	m_isRefresh = False

def PaDigitalClock2016wx_DoInit():
	global m_nClientWidth, m_nClientHeight
	global m_dcDigits, m_isRefresh
	global m_nItemW, m_nItemH, m_nStartX, m_nStartY
	m_nClientWidth, m_nClientHeight = objFrame.GetClientSize()

	d = m_nClientWidth / 12 / 11 # 显示 12:00:00.00格式 (11字符,每个字符12点宽)
	if d<3 :
		d=3
	m_nItemW = d * 12
	m_nItemH = d * 22
	m_nStartX = (m_nClientWidth - m_nItemW * 11)/2
	m_nStartY = (m_nClientHeight - m_nItemH)/2
	m_nBitmapDigitW = m_nItemW * 13

	m_bmDigits = wx.EmptyBitmap(m_nBitmapDigitW, m_nItemH)
	m_dcDigits = wx.BufferedDC(None, m_bmDigits)
	m_dcDigits.SetBackground(wx.Brush('#0000FF'))
	m_dcDigits.Clear()
	m_dcDigits.SetPen(objPen)
	m_dcDigits.SetBrush(objBrush)
	m_nOffset=0
	for n in range(12):
		x = n * m_nItemW
		for i in range(22):
			ch = A_byteDigitMatrix[m_nOffset] | (A_byteDigitMatrix[m_nOffset+1]<<8)
			y = i * d
			for ii in range(12):
				if (ch & A_nMask[ii])>0:
					m_dcDigits.DrawEllipse(x + ii * d, y, d-2, d-2)
			m_nOffset += 2

	m_isRefresh = True
	objFrame.Refresh(False)

def PaDigitalClock2016wx_OnPaint(event):
	global m_isRefresh
	m_isRefresh = True
	PaDigitalClock2016wx_DoDisplay()

def PaDigitalClock2016wx_OnResize(event):
	PaDigitalClock2016wx_DoInit()

def PaDigitalClock2016wx_OnDestroy(event):
	objTimer.Stop()

def PaDigitalClock2016wx_OnTimer(event):
	PaDigitalClock2016wx_DoDisplay()


if __name__ == '__main__':
	app = wx.App()
	objFrame = wx.Frame(None, title='PaDigitalClock2016wx.pyw', size=(600, 450))
	objFrame.SetBackgroundColour(m_strBackgroundColor)

	objPen = wx.Pen('#FFFFFF', 1, wx.SOLID)
	objBrush = wx.Brush('#FFFFFF')

	m_bmDigits = None
	m_dcDigits = None
	m_nClientWidth, m_nClientHeight = objFrame.GetClientSize()
	objTimer = wx.Timer(objFrame)

	objFrame.Bind(wx.EVT_PAINT, PaDigitalClock2016wx_OnPaint)
	objFrame.Bind(wx.EVT_SIZE, PaDigitalClock2016wx_OnResize)
	objFrame.Bind(wx.EVT_WINDOW_DESTROY, PaDigitalClock2016wx_OnDestroy)
	objFrame.Bind(wx.EVT_TIMER, PaDigitalClock2016wx_OnTimer, objTimer)

	objTimer.Start(10)

	objFrame.Show()
	app.MainLoop()
