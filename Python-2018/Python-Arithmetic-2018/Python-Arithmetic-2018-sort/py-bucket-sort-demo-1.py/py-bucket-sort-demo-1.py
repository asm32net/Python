#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python 2.7
# py-bucket-sort-demo-1.py

class BucketSortDemo1():
    MAX = 100
    bn = 5
    nFactor = (MAX / bn + 1) if MAX % bn else (MAX / bn)

    def __init__(self):
        self.C = [0] * self.bn

    def DisplayData(self, data):
        print ', '.join([str(i) for i in data])

    def InsertionSort(self, data, left, right):
        for i in xrange(left + 1, right + 1):
            get = data[i]
            j = i - 1
            while j >= left and data[j] > get:
                data[j + 1] = data[j]
                j -= 1
            data[j + 1] = get

    def CountingSort(self, data):
        n = len(data)

        def MapToBucket(x):
            return x / self.nFactor

        for i in xrange(self.bn):
            self.C[i] = 0
        for i in xrange(n):
            self.C[MapToBucket(data[i])] += 1
        for i in xrange(1, self.bn):
            self.C[i] = self.C[i] + self.C[i - 1]
        B = [0] * n
        for i in xrange(n - 1, -1, -1):
            b = MapToBucket(data[i])
            self.C[b] -= 1
            B[self.C[b]] = data[i]
        for i in xrange(n):
            data[i] = B[i]

    def BucketSort(self, data):
        self.CountingSort(data)
        for i in xrange(self.bn):
            left = self.C[i]
            right = (len(data) - 1) if (i == self.bn - 1) else  (self.C[i + 1] - 1)
            if left < right:
                self.InsertionSort(data, left, right)

if __name__ == '__main__':
    data = [76, 11, 11, 43, 78, 35, 39, 27, 16, 55, 1, 41, 24, 19, 54, 7, 78, 69, 65, 82]

    bsd = BucketSortDemo1()
    bsd.DisplayData(data)
    bsd.BucketSort(data)
    bsd.DisplayData(data)
