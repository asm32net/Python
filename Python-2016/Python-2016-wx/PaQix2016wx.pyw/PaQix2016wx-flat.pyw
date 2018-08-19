#!/usr/bin/python
# -*- coding: utf-8 -*-

#filename: PaQix2016wx.pyw

import wx
import random

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


def PaQix2016wx_DoInit():
	global m_nClientWidth, m_nClientHeight, m_bmMemory
	m_nClientWidth, m_nClientHeight = objFrame.GetClientSize()
	m_bmMemory = wx.EmptyBitmap(m_nClientWidth, m_nClientHeight)
	pqs.Config(m_nClientWidth, m_nClientHeight)
	pqs.Init()
	PaQix2016wx_DoDisplay()

def PaQix2016wx_DoDisplay():
	m_dcMemory = wx.BufferedDC(None, m_bmMemory)
	m_dcMemory.SetBackground(wx.Brush(conf__strBackgroundColor))
	m_dcMemory.Clear()

	for i in range(conf__nCount):
		if i==5:
			pqs.Update(True)
		s1 = 1.0 * i / conf__nCount
		m_strColor = '#%02X%02X%02X' % (pqs.cr * s1, pqs.cg * s1, pqs.cb * s1)
		pen1 = wx.Pen(m_strColor, 1, wx.SOLID)
		m_dcMemory.SetPen(pen1)
		m_dcMemory.DrawLine(pqs.x[0], pqs.y[0], pqs.x[1], pqs.y[1])
		pqs.Move()
	pqs.Update(False)
	pqs.NextColor()
	objFrame.Refresh(False)

def PaQix2016wx_OnPaint(event):
	wx.BufferedPaintDC(objFrame, m_bmMemory)

def PaQix2016wx_OnResize(event):
	PaQix2016wx_DoInit()

def PaQix2016wx_LButtonDown(event):
	pqs.Init()
	PaQix2016wx_DoDisplay()

def PaQix2016wx_OnDestroy(event):
	objTimer.Stop()

def PaQix2016wx_OnTimer(event):
	PaQix2016wx_DoDisplay()


if __name__ == '__main__':
	pqs = PaQixDef()

	app = wx.App()
	objFrame = wx.Frame(None, title='PaQix2016wx.pyw', size=(600, 450))
	objFrame.SetBackgroundColour(conf__strBackgroundColor)

	m_nClientWidth, m_nClientHeight = objFrame.GetClientSize()

	m_bmMemory = None
	objTimer = wx.Timer(objFrame)

	objFrame.Bind(wx.EVT_PAINT, PaQix2016wx_OnPaint)
	objFrame.Bind(wx.EVT_SIZE, PaQix2016wx_OnResize)
	objFrame.Bind(wx.EVT_LEFT_DOWN, PaQix2016wx_LButtonDown)
	objFrame.Bind(wx.EVT_WINDOW_DESTROY, PaQix2016wx_OnDestroy)
	objFrame.Bind(wx.EVT_TIMER, PaQix2016wx_OnTimer, objTimer)

	objTimer.Start(10)

	objFrame.Show()
	app.MainLoop()
