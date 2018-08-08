#!/usr/bin/python
# -*- coding: utf-8 -*-

# Python 2.7
# PaClock2016TK.pyw

from Tkinter import *
#import tkFont
from threading import Timer
import math, time, datetime


conf__strColor = '#000000'
PI2 = math.pi * 2

m_nClientWidth, m_nClientHeight = (600, 450)
m_isRunning = True
m_nTimerInterval = 0.1
m_nClockRadius = 0



image1_data = 'R0lGODlh7wAFAaIAAKbTTOjo59bitv//mbHNZ////+Tm2s/iiSH5BAQUAP8ALAAAAADvAAUBAAP/WLrc' \
	'/jDKSau9OCsTejBCKBhaaZ5oqq5sKwpeLH9ia994ru8POP8yEYlHLBqPPKBSxukgn9CodAFbWpWjqXbL' \
	'PYGq13Ds2y2bzwufeB3Mot/wI3s+CwXi+DyOTm969ICBJXx8fgZDgomKDGCEjjSLkYJ2j5Uhkphxl5Wc' \
	'l5mfXQECBZylbqCoU6WrHKmuT6uEfh6tr7Y7c4e6u7F/t0cghi8waK1hAgfJBMvMyQcjs4+HvzxfIdEf' \
	's2aNQMjM3+Dfz9h9o9Q5NORYnlKU3Qfh8fLQj+znK9my9khqP97hAAIKHCgQHL01s07dM/GlVK0nh7qB' \
	'I0ixIgCDEREe2rfw/4Iod7GgAIHHzKJJguDGZbyyC1FHCw17xYA1g+SykzgHioOmjsmulxc49OQEQk7N' \
	'bzmTBsQ49MdDoBHyyWxDhMTRkkqVMm06xiVUBxG5VirA0QW3AEizqr3IjKfYYF97XJva7U6OETJsrlUb' \
	'zi1LhXELfBErE0e/Dnr3rt16zFxgBSDpKsGB14MArIoXN+N5pSzQYISnoutwGXNmzQT8OtXlOC6vUsnY' \
	'tGYRwyYBi+Kcmd7blvOMlo8Fr1zzT96yA51nq7CcFuWBAdCjS3eWebOu1boev15j3DhyIEVb0JpY8Ln0' \
	'8+gHwOO9THXX7K4PijGuUx4QsspLzLJ9O6D59P8ATtdfVm1d5xN8X83FHXk4gQOeV4OAURpWBPwX4IXQ' \
	'radVewa+F16ClV0RD1/MTJYCJcVdFBCGLApI4DId0sJafIQxiBoBP5ByYhMT3kRAi0BmOGCDHA6XzUZx' \
	'KbgEf6cttcx9KIzSQTxBVjnAkCcxE+ORH37GVWJN1gelCcyBY6WVWOJW5IFdvmTkVWmGWeIY+WGAWEpn' \
	'VqlhlkVG89NXb8bQY5gUfRMECqThmaeecdZX4ZZ/QtVUc4Q6GgSEFdQmzqJnHpDTcVsemWRPYCbVjDKN' \
	'GmpZnRNUVpKFnAbZaEF9/hZYiEFQqmYyAZKE0pO0sBqBGj3GuuisbKUGqbD/1OCqKbLlBempk3P6goEa' \
	'NsFqLJDTqqlsjG2+5OydN2WpLYvrOShDBnYUu22esxY4Cwee3TPuP+aeC2Q8M7E7Qrbv5tltoX22VO85' \
	'9+6mk75VhrOuBgaQxHDAGKZa8C7MUvNmaSZVGLDDpNkV1IQULzqwo26FhWlHb5aqoscUqxsAchlEfByG' \
	'/J367sm0fitUpIBi42uhEwus6swrS9BMr+VWdLOxcYJqIIKuYaMwAEUfq+rBDYxAcnp7fpr1hTw30yHV' \
	'gJ6l8NhaA8t1GgeA8PR56ULL1kWcln3xRklHMlhLgG80w24/lkx3tRdcQ1J6dp/ENt0E+8xaxolY49Yw' \
	'/xgP3vTchkfXjLWtjsA5dE0rBrOeBKuEsXIbCdG3Fh1sF/jfree1eeGdCwisyK3KjXt0PJv+eIa/Pmpw' \
	'aq5ng/nkrxfBZWjBcjP0Urmjh3gFGy0DeaV4o45yS+kAHvvsw0xxFiHSlz48p3MSYwE8Fobd5G2/o+uo' \
	'5B7OTj5gwEDPxvQAEFjOeAUgksAgbjDRnnQat5bHDcxsrxHKkdg0uw/QRDLkGoiV5FcffR0HaRTI3u+C' \
	'J6f6XWhA33CP/lYoPiRg8FkFkVbjTrfAComief+iIfectq+eqY6F4HveCnlnmBd6wDbdY1Hp+GRCknxk' \
	'AhGz2X8YmJkeLsx1QMxiBf/vcj66XEYnLVrip+rnRCdI4AsKVA8VFZM1nplnGHCERvLGp0UirmBcC+qO' \
	'oZQRQ5ydBla7C11pPLdD3NjPOc5IpCLhuMKUiY9yMCEEUvqjR9OY8DxrJFoNQfcAEZwuk2ysWOQquRlH' \
	'ajEsKvCfB5pDSRQCBCVkm18S1QgNKNoMeIU0ycQ42DNStseUpwyXR/igoVSpqVAnJNTp4FFLCsCDkLms' \
	'yC5B2csUBhNwb4OAKqElRj7pi4R8SSIz33YZ83iKmg1M5g7ldc3JQQyPSthTK2lFIg+iE5aee0bGykm6' \
	'aFpkYirKJQG0CExIMqKLI0GJk0ZZIUXmDGyFnGINhiX/N/P4858Bot/VOvZKSrYTcNeKzJK6GdC7NRRd' \
	'BNwe93CHPGF5kngXpQjDFDkdVGXSmh9FmwREGk+FLXF0AsuleSrEPwY845lXimkHt8VLIiEvp0EJDYVc' \
	'ORBn7EyopItb3+JGwHsuhmIAHKPkgkm5OSSGpDSEmkAzpNVhhcBjTY3mJWMFTqcdB5gsfNv/WElP/5Ss' \
	'rqbL6jQi8NbnADaiuUvTT7eSReUxa69ULYhA1nfIdQr2dZfpp1KjlTt53k6j7KzjwT4ghkHdTbJY69xh' \
	'92JYfVIUqV7lS/U8t1FqEbWRjhTWYZbAoDTNNpqtPdgtV8s9ym6wtsn6pf6AaUcq/yBUUJgRo3FrSlPN' \
	'7jC4rDoEr4irzOk2bEPKvWZz8RMGMP2UU8VxZYXkqp5ksOoZHosticJh1Z3pLXL6FC8EeKq50mGJsslI' \
	'ro3Y6946zYyf8l2pd63Xs1Fe45raPAZyKWuxBGepvYMFC3yhs1neLBh4unJUfk9pYAmTdJZW7HDHMLwy' \
	'ZDyTuyqm5IdNa9dfeg2v7nSAGFxW1Q2quEEs1uZwf4waqNmtlKDJa352XNux6RMZRF5xMjKsYcNGeTEL' \
	'Xi2SSdyD8p54rr26siHdu9XnWNifaT3TkXtD1k4+N4OGlJaYxzzlYcX3zJUa0klNZqrwNhZTu/1BWMEY' \
	'pDnTGf+BPTBA4QyNZU71+bbBtGOgr6LLIH2R0WB0BqY+8qO4bnaNYFZin0d8Sh2/WRQbdSCe59deRDcg' \
	'YpmFMaZTG1SxPrjUDjj1hDCa4lnjTZ/NReMAfK2W6Wp5b/qDBFiasmtpyorYS2EmlZ2bWWhnhX22PuUT' \
	'ddyZQVOv17P+0bfc7F5rKwXbTr01C7e9bCvwGMXJPDGRxd3MV0csbuYW27FsjWNeeMbE3WRbScN9JTto' \
	'U5/5btB019zSP2f3uSmSKZAGjmlxj+PgIUi4t0Idy3T3+zrT7poVaNxHJcqbyInMLvI07i3jHpbNjR0v' \
	'I5bw1rW16JyrZqMz6vRWEOQ7apv/6hS/6yjzmWMBiYT248lVrIxnyOUyUGY5eW5jXIarO9kWxB7NXZZm' \
	'xkF754CGb9QTPuCqj5HUQwx5VNYxdaCiR9YXbairuxYC+LL8tAQxOxN/OMRspmEdSI+2qH2t6f3W/dJ3' \
	'16SPmfhUgjZP5N1IL/0ukrWlJ0ugcl+Zdu2e+IrUmolXX65Bje4Pyct48H1eq3sl4N6cfxpeY/z4dfwO' \
	'Fpqbfmkdd2ohj+OMYenT9UoFMDf9rEUU9EQEOXO7i1J/3d5rE3nAj+nnOYp2IK5AHcj3Ds64adv5yf0A' \
	'Qk4N3Getd44S9eOiYkEXkZ/8rutOrPfU3uo1DPXxM9r9uW95/+iTXcTS1137ZPNlIUYgO9cDYudp1kZ1' \
	'Qsd4WJRXj8cQ/ld3yVdfBcRjA6gUZGaA9dd5PaZmjEdqOFZUlFEHw6Ab8UCBFWiCFTJJSxFQk5csBZhr' \
	'b4V4P4ZOKfVse7d/gUN7qWQNJAhHNpUSi3QhcVSEJXhprAMCcRN9HUMgfuWB5nd+sidM/bMRKWeELpZI' \
	'egQ/DtWFXrgndQI/TEgwG0J5sBeFTzaFXWAwl5Nyk2OEV4iFcmgNcCEXCHgaXkU/LhcvO+E6Oqh2ZsCG' \
	'l4N8t5aFWmWFTwaI7/RuptN2yEUrLhdXKfECQOQ+wTEaohCEZzZgu2IyyNKHDbg/l0gEWP8YePP1ibzn' \
	'XUxSPHcVinzzhqOYBNkihy5mWxfoJA5lX69ki1Ioe9cQi9VQgorUiiLwdl/ohQFjUwImD2kYTMBYFRK4' \
	'OuynhamIgtWjgr7Ui76oiM9oAw+DH8iQBa0jge1Xjcd4juVISmnoixPVjVEgIwjyBVM2jtOYjtl4j8SI' \
	'RXhFAzzojhABHBuQhbl1hOQ4jJW0SJRIYjrlj4ngWDDAGgWGTTpIi3FEUAnJkNQQO7cmGMvDSDkljSDJ' \
	'jRh5DkayPIj4Qx5pOeo2khj5G1lEiSwZkzI5kzRZkzZ5kziZkzq5kzGZI6RgeyJwJJiTBkDDk7cgKKEY' \
	'jdKobiapkg//aJRw8Af8iCsJSY9T+FEwCZVlcAc+yZFJ+QJkJhmCeAlPqZU34ATRE45vSI65oYl6RBQA' \
	'aZZGkJaIYDnUSF/WaI++lAtrKZdkwm1m5JXhWJBCmHIo1YX4eDRhAIt+qQFp2YZ3WV3XqJf8ohFF2Zg6' \
	'thIcuXPnCDbHKGM3yCj3yAZxiZmv1oCGmIsZwlbYSB+p44k1JjMsMY6myQCZ6FDmCDxuGWK3OFl5U2GK' \
	'aQW0WZtkMYz1ZZCLtU57dlxRuDuz2Y/bAJY7J0duCJFgd5JZIApUEELf9x8qGJuuh39+tHHOKZw/ownC' \
	'uI5xhI7oKJ1ZCQGZyJoXuIvBZzSMpxFF/9c/0wiHd8mM7Pmf83dwnUZxDGV5CnaGG4cQd1CW6keRLuYd' \
	'ibRBoTkAIUBdc2dvmTWGJSSeGXWfYtA6RrCWRbiby5mCydeceoY1rPJSBmpo39ApqFieSwCiOzCW7Aeh' \
	'ZMOILyJNTkduZsaBvgmF5qcRo5c4X/l/zLh9vUkoAUp3vKKh6wRgYoUQ0HlGVWmXAFiBlMR0FyeDGQqk' \
	'Jfdde/ehIhlVSSaMSRqAqKViBWeJRJmhUHpdCxiFlpkCuHV7yodLBNph8OOmGyA3agSm34YmTlWnJ7B/' \
	'2QcQHHqHwdekC5AogSqoHApRHrqYZfp0A4mnixqnuqQS+9VpnFpcCP/qLaRZpF75M29oIxwXqZhWeKYW' \
	'a4IapjjIJ3NQpBJER7pgivD2dqHaqSIIX88Rq4PqPUxUqsPkJ7mqqmH0dZ4qg0+6pp03faRKpTBBDqwR' \
	'Ym3UqybRXkWVhUnVgkC6b8VKmhVgB/NyrTaHeoTnqk4qbtAqdasKIGv2HZZartgAkT4Fbq3KrgygXeK2' \
	'pMSWRoRaqAhBAWTpIe/mZOaWcokGp48IbfHqdQT7oVB0PvgqRhFrfxfFsNwGqw8bsOI6rmQqAQ/ir6nC' \
	'LQubgR07oB9bcbQmpENKrfBZss0mcTe3sFcCiBWFcy3qogs3pTL7AEqAro3CNhrrT2YGiIU1bC3/e38R' \
	'mx59lgt10hNEy2uVRWxJuzJHZWZNO2cKKK1qQgc8pw7JSlJiirUF12IudiVd67V5E7Wk2WIlazNmO6uE' \
	'16aG96RtK2beNUM4QprNxV+74G1PeLMQi7dPB6o9K2ZPC7Vwq6CdRLa60GRnS3DI41aKq60booqPlgv7' \
	'Jbm+MyvDw6h8WnDgR1iFs7cx9rKjGrMaIbQzGrorRqytmrY7lbqai4F01blSC7tDK7vbyih3qywUdWcs' \
	'N6GVm6C1umTmqaMURn62m7dcS3aNS6lO9bdB2wDmSbfxAnu5a2YiiB/blbsd82HfWqnZS3oPUrPONqd8' \
	'G71uFmu5q1jme77o//uhPBe7wBtnMFofTIe4nbRh9uu1vHdVj0ava7BTVGuFJ6eKGNtQwGW6hPVWpAOl' \
	'3RmhYAVe2DsHhDUUDCxv1ZuCKrVDpMM1CGbBs7VA4IXAI6tNbyZCIFw9q5a6yEBRimZYcVq/6gR/p/Yb' \
	'MjebSviIOoxJawXAETC+PzbEvPoiqdEHfQPENcdNSmxdK1XCfeOvFRxj10hFnyO2j/UXEVdjU7xqQxW+' \
	'4Fg4hItVhkO6MFgIZvyT2xvGalIyZGzFO0XBagSlY3yKPUyC9vq7RHtkOoxnLGXGsAYzi1sdydiiBuHG' \
	'FsBf8Mi9M2S+hCwkwrWEQ4XCxqKjDNXHB5I4Hv88uAAreAHYdXhmTuJHslyFxprsmV84yqyIPIVQlpBM' \
	'R0jKyNVIJRCVYDAzThWAVGw8PwyjujnoyUygAS+cqk2rXqAFZvJFPyBWw2ckNwKgHijHNBY2iehjqnAc' \
	'yq3DibjhLWGWh590udPMT0ebThnFyylkzIdCJkB8saP8wNgsJzV0qTfMYVq8wwwFnqXkCNxsm7dKs7e8' \
	'i92Rd/knPPf8OjcEzPscZv6sjvIhtneUzG9ImfLQgR36R5g0UAzNVVPUYauKJfgYkdLAoAq8vSpJooU5' \
	'PZWnyALSVhPwe3pan6K0MO35YHB5A/AUySpZkNNZgk0zNqDURMZjsHWnwkr/ZbgB9Rx/GCh8UKUG69P5' \
	'wzcOesuFu30EaD1Edbp3HDHToVTx+kDtYUSrggvjI0SVyJSTg0SqlhQTakDSPM33FtZyNalU/EFG1I46' \
	'0AQfiVvTU73epnxy7dVQBD81VMe9Vi10QaPQCAZkhVvRZTLZUjS9QTkbEUCJvYmV2xZTUZpFQId/XYg1' \
	'i9ebrCWXChkCq4yVMjx6ptcO8Z5QEJQfyZSmMcVgIzXVms+Hk8g2K2e9BJeyrQUWyZRyFMVJN1sQBBM5' \
	'pC3E/DLumyxnwUgaeaUofQQp6ZSsocz/lcI2UW8TgDT89Hbe17pdTCejaNwYm8I4BcqDJLEeFrK2VXqX' \
	'/6je9LvFUmNQnuR+cGfa8D3fvxHQqCCRV4PbtqFVBjW5Ans4RGKGsVJjJqIdbHg1/r0vOGWqElPKJI17' \
	'uxs5XXTdA45NhFvhSlogPLigHN4rBz7EQGdDThEcO5jGJF5AKcE3JWATKbys+LUawTGQIJxlOcMTjlkA' \
	'AJPjTLMr4CHgmWBK7Nu+QRUO15EBDf2iRi6v1Jfkj5GpvTnjk4dTT/HIoTvjBozk3ZDlEklyuOFknhVa' \
	'EFOcVF7lSk3m9D0qfi3PWoG87bXhfcLN06Bobw7ngCWj6D0qPo3mj7ZREEQvg7CgBw7n1iyyPF41bNLk' \
	'KyUvpGF8PSLm8BKjVxAY9/8qzzMsNSQg4FwpeVX+coI+A5LukkHs2+anOtrpBShuJt4Nfyyx6qwux963' \
	'JoFpAmCgibN1bC4+tEoeCZAM6srUJz95IqTQ6n8OVn7bxDNa7IugJLm+ijcCab0eJaSR6Xlqn6P2F7fy' \
	'XJNDnyscI3f0LOUSwhv9aKdGhfbS01yCp4xXME5A7ZARA4r6YcHM2DSnHXA8t2Fe0u4R6yrQCE3O7qx6' \
	'6H0M4qgQzx+cjSkjKDYA2bpSolp9ihvc6cFBphjD0ne1HRTvAupuV3iOKo1Y1gk8ipa5lgUWemNCGzKw' \
	'5SOCh+ctBvXtzu0U4eKREM9dHURFHPiOCbWMHUM0Gdv/Lh7Q5eopb8xS7QpFb/ShkiNJ741OIMkirfL4' \
	'+4zy3gvwbqdC8/MH3LvdaNbK1tdhL/Ybx8KLOfSusNfOI2iwPF9sv5gYCdWd4EJBoKu7/iiEgJHWHhJ6' \
	'7wvplWcF8vcjKQS98I5y/9x98QgyGfixg59RsH7ezsTWBNA1KT6y8fSYPlI1H8s7oUpnbZMfIfKR5/Yl' \
	'8GaauoVd3xk6SYmRjCtl8O6tP/p4X1qqD+MqiQcqDdQvj/qyQJx50PauKPyQT/zFb/bkqvy+z/wr7/xx' \
	'QPqSsfvSz9PQ/+/XrwfuPBXWv/39l/2WAf4NKf5ZR/6CIP4Oj/5SwPxvzP5RudffQQ//pFj970//018Y' \
	'goH/qbAK/G8LCCAS3P5OlUmrvTjrzbv/YCiOZHkFhiIUj+EGLKrAZm3feK7vORyoswdvCEoAADs='



def PaClock2016TK_DoInit():
	global m_nClockRadius
	m_nClockRadius = (m_nClientHeight<m_nClientWidth and m_nClientHeight or m_nClientWidth) * 9 / 10 / 2
	m_nClockDiameter = m_nClockRadius + m_nClockRadius

	cx,cy = (m_nClientWidth//2, m_nClientHeight//2)
	m_nStartX = (m_nClientWidth - m_nClockDiameter) // 2
	m_nStartY = (m_nClientHeight - m_nClockDiameter) // 2

	objCanvas.coords(objImage, (cx - 100, cy - 125))

	coords1 = m_nStartX+3, m_nStartY+3, m_nStartX+m_nClockDiameter-7, m_nStartY+m_nClockDiameter-7
	objCanvas.coords(circle1, coords1)
	coords1 = cx-5, cy-5, cx+10, cy+10
	objCanvas.coords(circle2, coords1)

	for i in range(60):
		angle1 = PI2 * i / 60
		dx1 = math.sin(angle1) * (m_nClockRadius - 7)
		dy1 = math.cos(angle1) * (m_nClockRadius - 7)
		s1 = 0
		if i % 5 == 0:
			s1 = 0.9
			coords1 = cx + dx1 * 0.8 + 1, cy - dy1 * 0.8 - 3
			objCanvas.coords(A_texts[i/5], coords1)
		else:
			s1 = 0.94
		coords1 = cx + dx1, cy + dy1, cx + dx1 * s1, cy + dy1 * s1
		objCanvas.coords(A_rulers[i], coords1)

	PaClock2016TK_DoPaint()

def PaClock2016TK_DoPaint():
	dt = datetime.datetime.now() # datetime.datetime(2016, 5, 22, 3, 17, 3, 203000)
	m_strDisplay = '%04d-%02d-%02d %02d:%02d:%02d' % (dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)

	objCanvas.itemconfig(objLabel, text=m_strDisplay)

	cx = m_nClientWidth // 2
	cy = m_nClientHeight // 2

	m_fStart = 0.05
	A_fEnd = [0.7, 0.5, 0.4]
	A_fAngle = [
		PI2 * dt.second / 60,
		PI2 * (60 * dt.minute + dt.second) / 3600,
		PI2 * (60 * ( 60 * ( dt.hour % 12 ) + dt.minute) + dt.second) / 43200]
	for i in range(3):
		dx1 = math.sin(A_fAngle[i]) * m_nClockRadius
		dy1 = math.cos(A_fAngle[i]) * m_nClockRadius
		coords1 = cx + int(dx1 * m_fStart), cy - int(dy1 * m_fStart), cx + int(dx1 * A_fEnd[i]), cy - int(dy1 * A_fEnd[i])
		objCanvas.coords(A_hands[i], coords1)

def PaClock2016TK_OnTimer():
	while m_isRunning:
		time.sleep(0.1)
		try:
			PaClock2016TK_DoPaint()
		except:
			pass

def PaClock2016TK_OnDestroy():
	global m_isRunning
	m_isRunning = False
	objThread.join()
	objFrame.destroy()
	print 'Destroy.'

def PaClock2016TK_OnResize(event):
	global m_nClientWidth, m_nClientHeight
	if(event.width!=m_nClientWidth) or (event.height!=m_nClientHeight):
		m_nClientWidth = event.width
		m_nClientHeight = event.height
		PaClock2016TK_DoInit()


if __name__ == '__main__':
	objFrame = Tk('PaClock2016TK.pyw')
	objFrame.title('PaClock2016TK.pyw')

	objCanvas = Canvas(objFrame, width=m_nClientWidth, height=m_nClientHeight, bg='#FFFFFF', bd=0)
	objCanvas.pack(expand=YES, fill=BOTH)



	#init interface items
	objLabel = objCanvas.create_text(10, 10, text='0000-00-00 00:00:00', anchor='w')

	A_rulers = [None for i in xrange(60)]
	A_texts = [None for i in xrange(12)]

	imgFace = PhotoImage(data=image1_data)
	objImage = objCanvas.create_image(0, 0,anchor=NW, image=imgFace)

	circle1 = objCanvas.create_oval(0, 0, 1, 1, width=7)
	circle2 = objCanvas.create_oval(0, 0, 1, 1, width=7)
	for i in range(60):
		width1 = (i % 5)==0 and 5 or 3
		A_rulers[i] = objCanvas.create_line(0, 0, 1, 1, fill=conf__strColor, width=width1)
	A_hands = [
		objCanvas.create_line(0, 0, 1, 1, fill=conf__strColor, width=3),
		objCanvas.create_line(0, 0, 1, 1, fill=conf__strColor, width=5),
		objCanvas.create_line(0, 0, 1, 1, fill=conf__strColor, width=7)]
	#font1 = tkFont.Font(family='Arial Black',size=24)
	for i in range(12):
		#A_texts[i] = objCanvas.create_text(0, 0, text=i, fill='#57B777', font=font1)
		A_texts[i] = objCanvas.create_text(0, 0, text=i, fill='#57B777', font=('Arial Black', 24))


	objFrame.bind('<Configure>', PaClock2016TK_OnResize)
	objFrame.protocol('WM_DELETE_WINDOW', PaClock2016TK_OnDestroy)

	objThread = Timer(m_nTimerInterval, PaClock2016TK_OnTimer)
	objThread.start()

	mainloop()
