import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

ds = pd.read_csv('./movie_metadata.csv')

print type(ds)
print ds.shape
# print ds

data = ds.values
print type(data)
print data.shape
# print data

# print ds.head(n=5)
# print ds.tail(n=3)

for i in ds.columns:
	print i

print "\n"
titles = ds.get('movie_title')
print len(titles)
print type(titles)

print "\n"
c = 0
for i in titles:
	if c < 10:
		print i
	c += 1

print "\n"
len_titles = []
for ix in titles:
    len_titles.append(len(ix))
# print len_titles    
print len(len_titles)
len_titles = np.array(len_titles)
# print len_titles

print "\n"
freq = dict()
for i in len_titles:
	try:
		freq[i]+=1
	except:
		freq[i] = 1

print freq		


plt.plot(freq.keys(), freq.values())
plt.show()

print "\n"
freq_values = np.array(freq.values())
freq_keys = np.array(freq.keys())
print "values ",freq_values
print "keys ", freq_keys
print np.argmax(freq_values)
print freq.keys()[np.argmax(freq_values)]

print "\n"
print "mean: ", len_titles.mean()
print "std: ", len_titles.std()
print "var: " ,len_titles.var()

# mean
s = 0
for i in len_titles:
	s += i
a = s/float(len(len_titles))
print "mean: ", a

# variance
v = 0
for i in len_titles:
	v += (i - a)**2
v = v/float(len(len_titles))
print "variance: ", v

# std
print "std:", np.sqrt(v)