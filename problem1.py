#!/usr/bin/env python

def count():
	sum = 0
	for i in range(0,1000):
		if i % 3 == 0 or i % 5 == 0:
			sum += i
	print sum
	return

def main():
	count()

if __name__ == '__main__': 
 main() 
