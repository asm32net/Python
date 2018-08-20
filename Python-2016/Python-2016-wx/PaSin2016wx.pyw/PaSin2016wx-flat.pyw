#!/usr/bin/python
# -*- coding: utf-8 -*-

#filename: PaSin2016wx.py

import wx, math

conf__nCount = 200
conf__strColor = '#00FF00'
conf__strBackgroundColor = '#000000'
PI2 = math.pi * 2

m_nOffset = 0
m_nStartY = 0
m_nSizeY = 0
m_nWidth1 = 0



def PaSin2016wx_DoInit():
	global m_nClientWidth, m_nClientHeight, m_bmMemory
	global m_nStartY, m_nSizeY, m_nWidth1
	m_nClientWidth, m_nClientHeight = objFrame.GetClientSize()
	m_bmMemory = wx.EmptyBitmap(m_nClientWidth, m_nClientHeight)

	m_nStartY = m_nClientHeight / 2
	m_nSizeY = m_nClientHeight / 2
	m_nWidth1 = m_nClientWidth / conf__nCount / 2

def PaSin2016wx_DoDisplay():
	m_dcMemory = wx.BufferedDC(None, m_bmMemory)
	m_dcMemory.SetBackground(wx.Brush(conf__strBackgroundColor))
	m_dcMemory.Clear()
	m_dcMemory.SetPen(objPen)
	m_dcMemory.SetBrush(objBrush)

	for i in range(conf__nCount):
		m_nStartX = m_nClientWidth * i / conf__nCount
		sin1 = math.sin(PI2 * (i + m_nOffset) / conf__nCount)
		m_nHeight1 = - sin1 * m_nSizeY
		m_nOffsetY = m_nHeight1 * 0.9
		m_nStartY1 = m_nStartY + m_nOffsetY
		m_dcMemory.DrawRectangle(m_nStartX, m_nStartY1, m_nWidth1, m_nHeight1 * 0.1)
	objFrame.Refresh(False)

def PaSin2016wx_OnPaint(event):
	wx.BufferedPaintDC(objFrame, m_bmMemory)

def PaSin2016wx_OnResize(event):
	PaSin2016wx_DoInit()

def PaSin2016wx_OnDestroy(event):
	objTimer.Stop()

def PaSin2016wx_OnTimer(event):
	global m_nOffset
	m_nOffset = (m_nOffset + 5) % conf__nCount
	PaSin2016wx_DoDisplay()


if __name__ == '__main__':
	app = wx.App()
	objFrame = wx.Frame(None, title='PaSin2016wx.py', size=(600, 450))
	objFrame.SetBackgroundColour(conf__strBackgroundColor)

	m_nClientWidth, m_nClientHeight = (0, 0)
	PaSin2016wx_DoInit()
	objTimer = wx.Timer(objFrame)
	objPen = wx.Pen(conf__strColor, 1, wx.SOLID)
	objBrush = wx.Brush(conf__strColor)

	objFrame.Bind(wx.EVT_PAINT, PaSin2016wx_OnPaint)
	objFrame.Bind(wx.EVT_SIZE, PaSin2016wx_OnResize)
	objFrame.Bind(wx.EVT_WINDOW_DESTROY, PaSin2016wx_OnDestroy)
	objFrame.Bind(wx.EVT_TIMER, PaSin2016wx_OnTimer, objTimer)

	objTimer.Start(10)

	objFrame.Show()
	app.MainLoop()
