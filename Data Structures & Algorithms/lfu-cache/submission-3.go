type Entry struct {
	key   int
	value int
	freq  int
	order int
}

type LFUCache struct {
	cache    []Entry
	capacity int
	counter  int
}

func Constructor(capacity int) LFUCache {
	return LFUCache{
		cache:    make([]Entry, 0),
		capacity: capacity,
		counter:  0,
	}
}

func (this *LFUCache) Get(key int) int {
	for i := range this.cache {
		if this.cache[i].key == key {
			this.cache[i].freq++

			this.counter++
			this.cache[i].order = this.counter

			return this.cache[i].value
		}
	}

	return -1
}

func (this *LFUCache) Put(key int, value int) {
	if this.capacity == 0 {
		return
	}

	// Key already exists
	for i := range this.cache {
		if this.cache[i].key == key {
			this.cache[i].value = value
			this.cache[i].freq++

			this.counter++
			this.cache[i].order = this.counter
			return
		}
	}

	// Cache is full
	if len(this.cache) == this.capacity {
		removeIndex := 0

		for i := range this.cache {
			if this.cache[i].freq < this.cache[removeIndex].freq {
				removeIndex = i
			} else if this.cache[i].freq == this.cache[removeIndex].freq {
				if this.cache[i].order < this.cache[removeIndex].order {
					removeIndex = i
				}
			}
		}

		this.cache = append(
			this.cache[:removeIndex],
			this.cache[removeIndex+1:]...,
		)
	}

	this.counter++
	this.cache = append(this.cache, Entry{
		key:   key,
		value: value,
		freq:  1,
		order: this.counter,
	})
}