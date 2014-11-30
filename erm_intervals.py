def learn_interval(examples):
	# sorting is O(n*log(n))
	examples.sort_by(lambda ex: ex.x)
	# Iterate from leftmost positive to rightmost positive
	# filtering is O(n)
	positives = examples.zipWithIndex.filter(lambda ex: ex[0].y == +1) #first component of the tuple is the example, second is the index
	positive_indices = positives.map(lambda ex: ex[1]) #mapping is O(n)
	positives = positives.map(lambda ex: ex[0]) #still O(n)
	# maximally wide interval has maximum error
	best_interval = (0, len(examples), 1.0)
	# this loop takes time O(n^2): for each inside a for each
	for i in range(0, len(positive_indices)):
		a = positive_indices[i]
		# Iterate from rightmost positive to leftmost positive, one by one.
		for j in range(len(positive_indices) - 1, -1, -1):
			b = positive_indices[j]
			# the number of negative examples outside our current interval
			# these are *correctly* classified
			negatives_outside = a + (len(examples) - b)
			# how many *positives* are inside the interval?
			positives_inside = j - i + 1
			# the number of positives *outside* the interval -- ERROR
			positives_outside = len(positives) - positives_inside
			# how many *negatives* are inside the interval -- ERROR
			negatives_inside = (b - a + 1) - positives_inside
			error = (positives_outside + negatives_inside) / len(examples)
			if error < best_interval[2] then:
				best_interval = (a, b, error)
	return (best_interval[0], best_interval[1]) #return the tuple components aside from the error counter
