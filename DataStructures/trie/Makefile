trie: trie.cpp trie.h
	g++ -c trie.cpp -o trie.o -Wno-c++11-extensions

test_trie: test_trie.cpp trie.h
	g++ -c test_trie.cpp -o test_trie.o

test: trie test_trie
	g++ trie.o test_trie.o -o test_trie

check: test
	./test_trie

clean:
	rm trie
