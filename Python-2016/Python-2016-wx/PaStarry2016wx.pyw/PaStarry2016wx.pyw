#/usr/bin/python
# -*- coding:utf-8 -*-

# Python 2.7
# PaStarry2016wx.pyw

import wx, random


conf__nCount = 150
conf__strBackgroundColor = '#000000'


class PaStarry():
	def __init__(self):
		self.d, self.x, self.y = 10, 10, 10
		self.cr, self.cg, self.cb = 255, 255, 255

class PaStarry2016wx(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, title='PaStarry2016wx.pyw', size=(600, 450))
		self.SetBackgroundColour(conf__strBackgroundColor)

		self.A_objItem = [PaStarry() for i in xrange(conf__nCount)]

		self.m_nClientWidth, self.m_nClientHeight = self.GetClientSize()

		self.m_nSelected = 0
		self.m_bmMemory = None
		self.objTimer = wx.Timer(self)

		self.Bind(wx.EVT_PAINT, self.OnPaint)
		self.Bind(wx.EVT_SIZE, self.OnResize)
		self.Bind(wx.EVT_LEFT_DOWN, self.OnLButtonDown)
		self.Bind(wx.EVT_WINDOW_DESTROY, self.OnDestroy)
		self.Bind(wx.EVT_TIMER, self.OnTimer, self.objTimer)

		self.objTimer.Start(20)


	def SetItem(self, i):
		self.A_objItem[i].d = random.randint(2, 5)
		self.A_objItem[i].x = random.randint(0, self.m_nClientWidth - self.A_objItem[i].d)
		self.A_objItem[i].y = random.randint(0, self.m_nClientHeight - self.A_objItem[i].d)
		self.A_objItem[i].cr = random.randint(0, 255) # 0 <= rand <= 255
		self.A_objItem[i].cg = random.randint(0, 255) # 0 <= rand <= 255
		self.A_objItem[i].cb = random.randint(0, 255) # 0 <= rand <= 255

	def DoInit(self):
		self.m_nClientWidth, self.m_nClientHeight = self.GetClientSize()
		self.m_bmMemory = wx.EmptyBitmap(self.m_nClientWidth, self.m_nClientHeight)
		for i in xrange(conf__nCount):
			self.SetItem(i)
		self.DoDisplay()

	def DoDisplay(self):
		m_dcMemory = wx.BufferedDC(None, self.m_bmMemory)
		m_dcMemory.SetBackground(wx.Brush(conf__strBackgroundColor))
		m_dcMemory.Clear()

		for i in xrange(conf__nCount):
			m_strColor = '#%02X%02X%02X' % (self.A_objItem[i].cr, self.A_objItem[i].cg, self.A_objItem[i].cb)
			pen1 = wx.Pen(m_strColor, 1, wx.SOLID)
			m_dcMemory.SetPen(pen1)
			brush1 = wx.Brush(m_strColor)
			m_dcMemory.SetBrush(brush1)
			m_dcMemory.DrawEllipse(self.A_objItem[i].x, self.A_objItem[i].y, self.A_objItem[i].d, self.A_objItem[i].d)
		self.Refresh(False)

	def OnPaint(self, event):
		wx.BufferedPaintDC(self, self.m_bmMemory)

	def OnResize(self, event):
		self.DoInit()

	def OnLButtonDown(self, event):
		self.DoInit()

	def OnDestroy(self, event):
		self.objTimer.Stop()

	def OnTimer(self, event):
		self.m_nSelected = (self.m_nSelected + 1) % conf__nCount
		self.SetItem(self.m_nSelected)
		self.DoDisplay()

if __name__ == '__main__':
	app = wx.App()
	ex = PaStarry2016wx()
	ex.Show()
	app.MainLoop()
