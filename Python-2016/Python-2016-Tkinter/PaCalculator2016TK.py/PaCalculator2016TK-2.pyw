#!/usr/bin/env python
# -*- coding: utf-8 -*-

#PaCalculator2016TK.py

from Tkinter import *
from functools import partial

confFont = ('Arial', 16)
confButtons = '789*~\\456/C\\123-=\\0.+'
confAlphaTable = '0123456789.+-*/'
strBackspace = u'←'

class Calculator(Tk):
	def __init__(self):
		Tk.__init__(self)

		self.title('Python Tk 计算器')
		#self.resizable(width=False, height=False)
		self.geometry('300x300+%s+%s' % (self.winfo_screenwidth()/2-150, self.winfo_screenheight()/2-150))

		for i in xrange(5):
			self.rowconfigure(i, weight=1)
			self.columnconfigure(i, weight=1)

		self.strDisplay = StringVar()
		Entry(self, font=confFont, textvariable=self.strDisplay, justify=RIGHT).grid(row=0, \
				column=0, columnspan=5, padx=2, pady=2, sticky='nswe')
		self.strDisplay.set('3.1415926535897932384626')

		nRows, nCols = 1, 0
		for c in confButtons:
			if c=='\\':
				nRows += 1
				nCols = 0
				continue
			nColspan = 2 if c=='0' else 1
			nRowspan = 2 if c=='=' else 1
			if c=='~':c=strBackspace
			Button(self, text=c, font=confFont, command=partial(self.buttonClick, c) ) \
					.grid(row=nRows, column=nCols, padx=2, pady=2, rowspan=nRowspan, columnspan=nColspan, \
					sticky='nswe')
			nCols += nColspan

	def buttonClick(self, c):
		strDisplay_t = self.strDisplay.get()
		if c=='C':
			self.strDisplay.set('')
		elif c==strBackspace:
			if strDisplay_t:
				self.strDisplay.set(strDisplay_t[:-1])
		elif c=='=':
			if False in [ch in confAlphaTable for ch in strDisplay_t]:	# 防止手动输入的恶意表达式
				self.strDisplay.set('F')									# 攻击计算机，比如
				return														# open('1.txt','w').write('te')
			try:
				self.strDisplay.set( str( eval(strDisplay_t) ) )
			except Exception, e:
				self.strDisplay.set('E')
		elif c in '+-*/' and (not strDisplay_t or strDisplay_t[-1] in '+-*/'):
			pass
		elif c=='.':
			strDisplay_t_len = len(strDisplay_t)
			nFlag = 0
			for i in xrange(strDisplay_t_len):
				ch = strDisplay_t[strDisplay_t_len-i-1]
				if ch == '.':
					nFlag = 2
					break
				elif ch in '0123456789':
					nFlag = 1
				elif ch in '+-*/':
					break

			if nFlag == 0:
				self.strDisplay.set( strDisplay_t + '0' + c )
			elif nFlag==1:
				self.strDisplay.set( strDisplay_t + c )
		else:
			self.strDisplay.set( strDisplay_t + c )
		print self.strDisplay.get()

if __name__ == '__main__':
	#[Calculator() for i in xrange(3)]
	Calculator()
	mainloop()
