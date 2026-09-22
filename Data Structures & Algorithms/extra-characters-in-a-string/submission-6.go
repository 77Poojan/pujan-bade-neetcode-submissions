type TrieNode struct {
    children [26]*TrieNode
    isWord   bool
}

type Trie struct {
    root *TrieNode
}

func newTrie() *Trie {
    return &Trie{root: &TrieNode{}}
}

func (t *Trie) addWord(word string) {
    curr := t.root
    for _, c := range word {
        idx := c - 'a'
        if curr.children[idx] == nil {
            curr.children[idx] = &TrieNode{}
        }
        curr = curr.children[idx]
    }
    curr.isWord = true
}

func minExtraChar(s string, dictionary []string) int {
    trie := newTrie()
    for _, word := range dictionary {
        trie.addWord(word)
    }

    dp := make([]int, len(s)+1)
    for i := range dp {
        dp[i] = -1
    }

    var dfs func(i int) int
    dfs = func(i int) int {
        if i == len(s) {
            return 0
        }
        if dp[i] != -1 {
            return dp[i]
        }

        res := 1 + dfs(i+1)
        curr := trie.root

        for j := i; j < len(s); j++ {
            idx := s[j] - 'a'
            if curr.children[idx] == nil {
                break
            }
            curr = curr.children[idx]
            if curr.isWord {
                res = min(res, dfs(j+1))
            }
        }

        dp[i] = res
        return res
    }

    return dfs(0)
}