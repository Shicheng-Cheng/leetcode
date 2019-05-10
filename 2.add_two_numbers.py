# -*- coding: utf-8 -*-
"""
Created on Fri May 10 21:47:32 2019

@author: Dell
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        p =dummy
        carry_digit = 0
        p1 = l1
        p2 = l2
        while p1 and p2:
            tmp = p1.val + p2.val + carry_digit
            quotient = tmp // 10
            remainder = tmp % 10
            p.next = ListNode(remainder)
            carry_digit = quotient
            p1 = p1.next
            p2 = p2.next
            p = p.next
        while p1:
            tmp = p1.val + carry_digit
            quotient = tmp // 10
            remainder = tmp % 10
            p.next = ListNode(remainder)
            carry_digit = quotient
            p1 = p1.next
            p = p.next
        while p2:
            tmp = p2.val + carry_digit
            quotient = tmp // 10
            remainder = tmp % 10
            p.next = ListNode(remainder)
            carry_digit = quotient
            p2 = p2.next
            p = p.next
        if carry_digit:
            p.next = ListNode(carry_digit)
        
        return dummy.next