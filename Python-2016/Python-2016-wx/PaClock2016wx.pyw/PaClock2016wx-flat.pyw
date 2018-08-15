#!/usr/bin/python
# -*- coding: utf-8 -*-

# Python 2.7
# PaClock2016wx.pyw

import wx, datetime, math

PI2 = math.pi * 2
conf__strColor = '#000000'
conf__strBackgroundColor = '#FFFFFF'

m_nClockRadius = m_nClockDiameter = m_nStartX = m_nStartY = 0

def PaClock2016wx_DoDisplay():
	m_dcMemory = wx.BufferedDC(None, m_bmMemory)
	m_dcMemory.SetBackground(wx.Brush(conf__strBackgroundColor))
	m_dcMemory.Clear()

	dt = datetime.datetime.now() # datetime.datetime(2016, 5, 22, 3, 17, 3, 203000)

	m_strDisplay = '%04d-%02d-%02d %02d:%02d:%02d' % (dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)
	m_dcMemory.SetBackgroundMode(wx.SOLID)
	m_dcMemory.SetTextBackground(conf__strBackgroundColor)
	m_dcMemory.SetTextForeground('#000000')
	m_dcMemory.DrawText(m_strDisplay, 0, 0)

	m_dcMemory.Blit(m_nStartX, m_nStartY, m_nClockDiameter, m_nClockDiameter, m_dcFace, 0, 0, wx.COPY)

	cx = m_nClientWidth / 2
	cy = m_nClientHeight / 2

	m_fStart = 0.08
	A_objPens = [objPen3, objPen5, objPen7]
	A_fEnd = [0.7, 0.5, 0.4]
	A_fAngle = [
		PI2 * dt.second / 60,
		PI2 * (60 * dt.minute + dt.second) / 3600,
		PI2 * (60 * ( 60 * ( dt.hour % 12 ) + dt.minute) + dt.second) / 43200]
	for i in range(3):
		dx1 = math.sin(A_fAngle[i]) * m_nClockRadius
		dy1 = math.cos(A_fAngle[i]) * m_nClockRadius
		m_dcMemory.SetPen(A_objPens[i])
		m_dcMemory.DrawLine(cx + dx1 * m_fStart, cy - dy1 * m_fStart,
			cx + dx1 * A_fEnd[i], cy - dy1 * A_fEnd[i])
	objFrame.Refresh()

def PaClock2016wx_DoInit():
	global m_nClientWidth, m_nClientHeight, m_bmMemory, m_dcFace
	global m_nClockRadius, m_nClockDiameter, m_nStartX, m_nStartY
	m_nClientWidth, m_nClientHeight = objFrame.GetClientSize()
	m_bmMemory = wx.EmptyBitmap(m_nClientWidth, m_nClientHeight)

	m_nClockRadius = (m_nClientHeight<m_nClientWidth and m_nClientHeight or m_nClientWidth) * 9 / 10 / 2
	m_nClockDiameter = m_nClockRadius + m_nClockRadius

	m_nStartX = (m_nClientWidth - m_nClockDiameter) / 2
	m_nStartY = (m_nClientHeight - m_nClockDiameter) / 2
	
	m_bmFace = wx.EmptyBitmap(m_nClockDiameter, m_nClockDiameter)
	m_dcFace = wx.BufferedDC(None, m_bmFace)
	m_dcFace.SetBackground(wx.Brush(conf__strBackgroundColor))
	m_dcFace.Clear()
	m_dcFace.SetPen(objPen7)
	m_dcFace.DrawEllipse(3, 3, m_nClockDiameter-7, m_nClockDiameter-7)
	m_dcFace.DrawEllipse(m_nClockRadius-5, m_nClockRadius-5, 10, 10)

	m_dcFace.SetFont(objFont)
	m_dcFace.SetTextForeground('#57B777')

	for i in range(60):
		angle1 = PI2 * i / 60
		dx1 = math.sin(angle1) * (m_nClockRadius - 7)
		dy1 = math.cos(angle1) * (m_nClockRadius - 7)
		s1 = 0
		if i % 5 == 0:
			s1 = 0.9
			m_dcFace.SetPen(objPen5)

			str1 = '%d' % (i / 5)
			m_dcFace.DrawText(str1,
				m_nClockRadius + dx1 * 0.8 - 10, m_nClockRadius - dy1 * 0.8 - 23)
		else:
			s1 = 0.94
			m_dcFace.SetPen(objPen3)
		m_dcFace.DrawLine(m_nClockRadius + dx1, m_nClockRadius + dy1,
			m_nClockRadius + dx1 * s1, m_nClockRadius + dy1 * s1)

	PaClock2016wx_DoDisplay()

def PaClock2016wx_OnPaint(event):
	wx.BufferedPaintDC(objFrame, m_bmMemory)

def PaClock2016wx_OnResize(event):
	PaClock2016wx_DoInit()

def PaClock2016wx_OnDestroy(event):
	objTimer.Stop()

def PaClock2016wx_OnTimer(event):
	PaClock2016wx_DoDisplay()


if __name__ == '__main__':
	app = wx.App()
	objFrame = wx.Frame(None, title='PaClock2016wx.pyw', size=(600, 450))
	objFrame.SetBackgroundColour(conf__strBackgroundColor)

	m_nClientWidth, m_nClientHeight = objFrame.GetClientSize()

	objFont = wx.Font(24,
		wx.FONTFAMILY_DEFAULT,
		wx.FONTSTYLE_NORMAL,
		wx.FONTWEIGHT_BOLD,
		face='Arial Black')
	objPen3 = wx.Pen(conf__strColor, 3, wx.SOLID)
	objPen5 = wx.Pen(conf__strColor, 5, wx.SOLID)
	objPen7 = wx.Pen(conf__strColor, 7, wx.SOLID)
	m_bmFace = None
	m_dcFace = None
	m_bmMemory = None
	objTimer =wx.Timer(objFrame)

	objFrame.Bind(wx.EVT_PAINT, PaClock2016wx_OnPaint)
	objFrame.Bind(wx.EVT_SIZE, PaClock2016wx_OnResize)
	objFrame.Bind(wx.EVT_WINDOW_DESTROY, PaClock2016wx_OnDestroy)
	objFrame.Bind(wx.EVT_TIMER, PaClock2016wx_OnTimer, objTimer)

	objTimer.Start(1000)

	objFrame.Show()
	app.MainLoop()
