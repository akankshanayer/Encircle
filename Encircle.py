# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 11:58:22 2020

@author: Akanksha
"""
#!/usr/bin/env python

import sys
import re
stack = [];
class Calculator:
    def __init__(self,operation,numbers):
        self.operation=operation;
        self.numbers=numbers;
        
    
def get_user_input():
    user_input=sys.argv[1];
    return user_input


def calculate(stack):
    arr = []
    sum = 0
    product = 1
    while stack[-1] != '*' and stack[-1] != '+':
        arr.append(stack.pop())
    arr.append(stack.pop())

    if arr[-1] == '+':
        for i in range(0, len(arr) - 1):
            sum = sum + arr[i]
        result = sum

    elif arr[-1] == '*':
        for i in range(0, len(arr) - 1):
            product = product * arr[i]
        result = product
    stack.append(result)


def parsing_input():
    a = re.split('\)| ', get_user_input())
    for i in a:
        if i == '(add':
            stack.append('+')
        elif i == '(multiply':
            stack.append('*')
        elif i == '':
            calculate(stack)
        else:
            stack.append(int(i))
    

parsing_input();


print('\nFinal Result:')
print(stack.pop())
