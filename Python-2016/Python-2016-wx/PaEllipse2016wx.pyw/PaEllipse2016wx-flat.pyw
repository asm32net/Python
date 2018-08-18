#!/usr/bin/python
# -*- coding: utf-8 -*-

# Python 2.7
# PaEllipse2016wx.pyw

import wx, math

conf__nCount = 40
conf__strColor = '#FFFF00'
conf__strBackgroundColor = '#000000'
PI2 = math.pi * 2

m_fStartAngle = 0


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


def _rotate(x, y, angle):
	sin1 = math.sin(angle)
	cos1 = math.cos(angle)
	x1, y1 = (x, y)
	x = cos1 * x1 + sin1 * y1
	y = cos1 * y1 - sin1 * x1
	return (x, y)

def PaEllipse2016wx_DoInit():
	global m_nClientWidth, m_nClientHeight, m_bmMemory
	m_nClientWidth, m_nClientHeight = objFrame.GetClientSize()
	m_bmMemory = wx.EmptyBitmap(m_nClientWidth, m_nClientHeight)
	PaEllipse2016wx_DoDisplay()

def PaEllipse2016wx_DoDisplay():
	m_dcMemory = wx.BufferedDC(None, m_bmMemory)
	m_dcMemory.SetBackground(wx.Brush(conf__strBackgroundColor))
	m_dcMemory.Clear()
	m_dcMemory.SetPen(objPen)
	m_dcMemory.SetBrush(objBrush)

	x0 = m_nClientWidth / 2
	y0 = m_nClientHeight / 2
	fStep = PI2 / conf__nCount
	r = d = 0
	for i in range(conf__nCount):
		angle1 = i * fStep
		sin1 = math.sin(angle1 + m_fStartAngle)
		cos1 = math.cos(angle1 + m_fStartAngle)
		r = r==3 and 6 or 3 # r = r==3 ? 6 : 3
		d = r + r
		x1 = pes1.a * sin1
		y1 = pes1.b * cos1
		x1, y1 = _rotate(x1, y1, m_fStartAngle)
		x1 += x0
		y1 += y0
		m_dcMemory.DrawEllipse(x1 - r, y1- r, d, d)
		x1 = pes2.a * sin1
		y1 = pes2.b * cos1
		x1, y1 = _rotate(x1, y1, m_fStartAngle)
		x1 += x0
		y1 += y0
		m_dcMemory.DrawEllipse(x1 - r, y1- r, d, d)
	objFrame.Refresh(False)

def PaEllipse2016wx_OnPaint(event):
	wx.BufferedPaintDC(objFrame, m_bmMemory)

def PaEllipse2016wx_OnResize(event):
	PaEllipse2016wx_DoInit()

def PaEllipse2016wx_OnDestroy(event):
	objTimer.Stop()

def PaEllipse2016wx_OnTimer(event):
	global m_fStartAngle
	m_fStartAngle += PI2 / 160
	if(m_fStartAngle>=PI2):
		m_fStartAngle=0
	PaEllipse2016wx_DoDisplay()

if __name__ == '__main__':
	app = wx.App()
	objFrame = wx.Frame(None, title='PaEllipse2016wx.pyw', size=(600, 450))
	objFrame.SetBackgroundColour(conf__strBackgroundColor)

	m_nClientWidth, m_nClientHeight = objFrame.GetClientSize()

	m_bmMemory = None
	objPen = wx.Pen(conf__strColor, 1, wx.SOLID)
	objBrush = wx.Brush(conf__strColor)
	objTimer = wx.Timer(objFrame)

	pes1 = PaEllipseDef(0, 0, 300, 75, 0, 0)
	pes2 = PaEllipseDef(0, 0, 50, 200, 0, 0)


	objFrame.Bind(wx.EVT_PAINT, PaEllipse2016wx_OnPaint)
	objFrame.Bind(wx.EVT_SIZE, PaEllipse2016wx_OnResize)
	objFrame.Bind(wx.EVT_WINDOW_DESTROY, PaEllipse2016wx_OnDestroy)
	objFrame.Bind(wx.EVT_TIMER, PaEllipse2016wx_OnTimer, objTimer)

	objTimer.Start(50)

	objFrame.Show()
	app.MainLoop()
