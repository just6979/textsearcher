package text

import (
)

// TextSearcher structure
// TODO: add in objects/data structures required by the Search function
type TextSearcher struct {
}

// NewSearcher returns a TextSearcher from the given file
// TODO: Load/process the file so that the Search function work
func NewSearcher(filePath string) (*TextSearcher, error) {
	return &TextSearcher{}, nil
}

// Search searchs the file loaded when NewSearcher was called for the given word and
// returns a list of matches surrounded by the given number of context words
// TODO: Implement this function to pass the tests in search_test.go
func (ts *TextSearcher) Search(word string, context int) []string {
	return []string{}
}
