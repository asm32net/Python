#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python 2.7
# py-bubblesort-demo-1.py

class BubbleSortDemo1():
    def DisplayData(self, data):
        print ', '.join([str(i) for i in data])
    def BubbleSort(self, data):
        n = len(data)
        for j in xrange(n - 1):
            for i in xrange(n - 1- j):
                if data[i] > data[i + 1]:
                    data[i], data[i + 1] = data[i + 1], data[i]

if __name__ == '__main__':
    data = [76, 11, 11, 43, 78, 35, 39, 27, 16, 55, 1, 41, 24, 19, 54, 7, 78, 69, 65, 82]
    bsd = BubbleSortDemo1()
    bsd.DisplayData(data)
    bsd.BubbleSort(data)
    bsd.DisplayData(data)