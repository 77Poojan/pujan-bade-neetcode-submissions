type Entry struct {
	value     string
	timestamp int
}

type TimeMap struct {
	store map[string][]Entry
}

func Constructor() TimeMap {
	return TimeMap{
		store: make(map[string][]Entry),
	}
}

func (this *TimeMap) Set(key string, value string, timestamp int) {
	this.store[key] = append(this.store[key], Entry{
		value:     value,
		timestamp: timestamp,
	})
}

func (this *TimeMap) Get(key string, timestamp int) string {
	entries, ok := this.store[key]
	if !ok || len(entries) == 0 {
		return ""
	}

	l := 0
	r := len(entries) - 1

	for l <= r {
		mid := (l + r) / 2
		if entries[mid].timestamp <= timestamp {
			l = mid + 1
		} else {
			r = mid - 1
		}
	}

	if l == 0 {
		return "" // no entry with timestamp <= target
	}
	return entries[l-1].value
}