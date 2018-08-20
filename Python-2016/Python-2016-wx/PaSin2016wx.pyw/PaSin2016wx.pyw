#!/usr/bin/python
# -*- coding: utf-8 -*-

# Python 2.7
# PaSin2016wx.py

import wx, math

conf__nCount = 200
conf__strColor = '#00FF00'
conf__strBackgroundColor = '#000000'
PI2 = math.pi * 2

class PaSin2016wx(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, title='PaSin2016wx.py', size=(600, 450))
		self.SetBackgroundColour(conf__strBackgroundColor)

		self.m_nOffset = 0
		self.m_nStartY = 0
		self.m_nSizeY = 0
		self.m_nWidth1 = 0

		self.m_nClientWidth, self.m_nClientHeight = (0, 0)
		self.DoInit()

		self.objTimer = wx.Timer(self)
		self.m_bmMemory = None
		self.m_objPen = wx.Pen(conf__strColor, 1, wx.SOLID)
		self.m_objBrush = wx.Brush(conf__strColor)

		self.Bind(wx.EVT_PAINT, self.OnPaint)
		self.Bind(wx.EVT_SIZE, self.OnResize)
		self.Bind(wx.EVT_WINDOW_DESTROY, self.OnDestroy)
		self.Bind(wx.EVT_TIMER, self.OnTimer, self.objTimer)

		self.objTimer.Start(10)

	def DoInit(self):
		self.m_nClientWidth, self.m_nClientHeight = self.GetClientSize()
		self.m_bmMemory = wx.EmptyBitmap(self.m_nClientWidth, self.m_nClientHeight)

		self.m_nStartY = self.m_nClientHeight / 2
		self.m_nSizeY = self.m_nClientHeight / 2
		self.m_nWidth1 = self.m_nClientWidth / conf__nCount / 2

	def DoDisplay(self):
		m_dcMemory = wx.BufferedDC(None, self.m_bmMemory)
		m_dcMemory.SetBackground(wx.Brush(conf__strBackgroundColor))
		m_dcMemory.Clear()
		m_dcMemory.SetPen(self.m_objPen)
		m_dcMemory.SetBrush(self.m_objBrush)

		for i in range(conf__nCount):
			m_nStartX = self.m_nClientWidth * i / conf__nCount
			sin1 = math.sin(PI2 * (i + self.m_nOffset) / conf__nCount)
			m_nHeight1 = - sin1 * self.m_nSizeY
			self.m_nOffsetY = m_nHeight1 * 0.9
			self.m_nStartY1 = self.m_nStartY + self.m_nOffsetY
			m_dcMemory.DrawRectangle(m_nStartX, self.m_nStartY1, self.m_nWidth1, m_nHeight1 * 0.1)
		self.Refresh(False)

	def OnPaint(self, event):
		wx.BufferedPaintDC(self, self.m_bmMemory)

	def OnResize(self, event):
		self.DoInit()

	def OnDestroy(self, event):
		self.objTimer.Stop()

	def OnTimer(self, event):
		self.m_nOffset = (self.m_nOffset + 5) % conf__nCount
		self.DoDisplay()


if __name__ == '__main__':
	app = wx.App()
	ex = PaSin2016wx()
	ex.Show()
	app.MainLoop()
