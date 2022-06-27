import random
import numpy as np
from math import gcd,sqrt
class functions:
	'''
	Variance: measures how spread out the data is
	mean: find the mean of data
	squared_difference: the sum of squared difference from the mean
	'''
	@staticmethod
	def do_variance(line):
		'''Find the mean, difference from the mean, square that difference, find the mean of it'''
		data=[random.randint(1,1000) for x in range(random.randint(2,7))]
		mean = sum(data)/len(data)
		difference_from_mean = [x-mean for x in data]
		squared_difference = [x*x for x in difference_from_mean]
		variance = sum(squared_difference)/len(squared_difference)
		ans = f"Find the population variance of {[x for x in data]}"
		return(ans,round(variance,2))
	@staticmethod
	def do_mean(line):
		'''Find the mean by adding them altogether and divide by the number of numbers'''
		data=[random.randint(1,1000) for x in range(random.randint(2,7))]
		mean = sum(data)/len(data)
		ans = f"Find the mean of {[x for x in data]}"
		return(ans,round(float(mean),2))
	@staticmethod
	def do_squared_difference(line):
		'''Find the mean, difference from the mean, square that difference'''
		data=[random.randint(1,1000) for x in range(random.randint(2,7))]
		mean = sum(data)/len(data)
		difference_from_mean = [x-mean for x in data]
		squared_difference = [round(x*x,2) for x in difference_from_mean]
		ans = f"Find the square difference of {data}"
		return(ans,squared_difference)

