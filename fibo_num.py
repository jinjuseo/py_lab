#!/usr/bin/python
import sys

# fibonum: now fibo num i
# x : fibonum i-2
# y : fibonum i-1
if __name__=='__main__':
	n = int(input("fibonacci number? "))
	
	y=1
	for i in range(1,n+1):
		if i == 1:
			fibo_num = 1
			#print("{0}".format(fibo_num));
			sys.stdout.write("%d"%fibo_num)
			x=0
			y=fibo_num
		
		else :
			
			fibo_num = x+y
			#print(",%d"%fibo_num, end=' ')
			#print(",%d"%fibo_num)
			sys.stdout.write(",%d"%fibo_num)
			x=y
			y=fibo_num	
	
	print("\nF%d = %d"%(n,fibo_num))
