#! /usr/bin/env python
# python challenge level5

import cPickle
file = open('banner.p')
for line in cPickle.load(file):
	print ''.join([x[0] * x[1] for x in line])
file.close()