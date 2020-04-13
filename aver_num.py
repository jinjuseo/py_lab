#!/usr/bin/python
import sys

if __name__=='__main__':
	n = int(input("How many numbers will you add? "))
	sum = 0
	for i in range(0,n) :
		num = int(input("input: "))
		sum += num;
	average = sum/n
	print("average is %d " % average) 
	
