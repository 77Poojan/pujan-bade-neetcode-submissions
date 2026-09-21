type TrieNode struct {
	children [26]*TrieNode
	endOfWord bool
}

func NewTrieNode() *TrieNode {
	return &TrieNode{}
}

type WordDictionary struct {
    root *TrieNode
}

func Constructor() WordDictionary {
    return WordDictionary { root: NewTrieNode() } 
}

func (this *WordDictionary) AddWord(word string)  {
	curr := this.root

	for _, ch := range word {
        index := ch - 'a'
		if curr.children[index] == nil {
			curr.children[index] = NewTrieNode()
		}
		curr = curr.children[index]
	}
    
	curr.endOfWord = true
}

func (this *WordDictionary) Search(word string) bool {
	var dfs func(node *TrieNode, i int) bool

	dfs = func(node *TrieNode, i int) bool {
		if node == nil {
			return false
		}
		if i == len(word) {
			return node.endOfWord
		}

		ch := word[i]

		if ch == '.' {
			for _, child := range node.children {
				if child != nil && dfs(child, i+1) {
					return true
				}
			}
			return false
		}

		index := ch - 'a'
		return dfs(node.children[index], i+1)
	}

	return dfs(this.root, 0)
}