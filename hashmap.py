def new(num_buckets=256):
	"""Initializes a Map with the given number of buckets."""
	# appends 256 buckets (empty lists) to aMap (list)
	aMap = []
	# 0 to 255; that's 256 buckets
	for i in range(0, num_buckets):
		aMap.append([])
	return aMap

# % will always give a number that is smaller than the number you divide (in this case, result will be smaller than len(aMap))
def hash_key(aMap, key):
	"""Given a key this will create a number and then convert it to
	an index for the aMap's buckets."""
	return hash(key) % len(aMap)

# returns the specific EMPTY bucket located at the bucket_id inside the list of buckets (aMap)
def get_bucket(aMap, key):
	"""Given a key, find the bucket where it would go."""
	bucket_id = hash_key(aMap, key)
	return aMap[bucket_id]
	

def get_slot(aMap, key, default=None):
	"""
	Returns the index, key, and value of a slot found in a bucket.
	Returns -1, key, and default (None if not set) when not found.
	"""
	bucket = get_bucket(aMap, key)
	# does not go into this for loop if bucket is empty
	for i, kv in enumerate(bucket):
		k, v = kv
		if key == k:
			print "key == k"
			return i, k, v
	# returns -1, key, None if the bucket is empty
	return -1, key, default
	
def get(aMap, key, default=None):
	"""Gets the value in a bucket for the given key, or the default."""
	i, k, v = get_slot(aMap, key, default=default)
	return v
	
def set(aMap, key, value):
	"""Sets the key to the value, replacing any existing value."""
	bucket = get_bucket(aMap, key)
	print "before bucket: ", bucket
	i, k, v = get_slot(aMap, key)
	print "i, k, v: %d, %s, %s" % (i, k, v)
	if i >= 0:
		# the key exists, replace it
		bucket[i] = (key, value)
	else:
		# the key does not exist, append to create it
		print "key, value: %s, %s" % (key, value)
 		bucket.append((key, value))
		print "after bucket: ", bucket
		
def delete(aMap, key):
	"""Deletes the given key from the Map."""
	bucket = get_bucket(aMap, key)
	
	for i in xrange(len(bucket)):
		k, v = bucket[i]
		if key == k:
			del bucket[i]
			break
			
def list(aMap):
	"""Prints out what's in the Map."""
	for bucket in aMap:
		if bucket:
			for k, v in bucket:
				print k, v