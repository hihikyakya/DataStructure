# -*- coding: utf-8 -*-
"""
Created on Tue May 20 13:53:17 2025

@author: cic
"""
class Astack:
    def __init__(self, capacity):
        self.stack = []
        self.capacity = capacity

    def push(self, item):
        if len(self.stack) < self.capacity:
            self.stack.append(item)
        else:
            print("스택이 가득 찼습니다!")

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]