import string


class TextSearcher(object):

    def __init__(self):
        self.shadow_words = []
        self.words = []

    def load(self, file_path: str) -> bool:
        if file_path is None:
            return False

        try:
            file = open(file_path)
        except FileNotFoundError:
            return False

        lines = file.readlines()
        for line in lines:
            # clean the line, get each word, clean the words, skip ''
            temp_words = [word.strip() for word in line.strip().split() if word != '']
            # make a shadow word list in all lowercase
            temp_shadow_words = [word.lower().strip().strip('"').strip('.') for word in temp_words]
            # save the line's words
            self.words.extend(temp_words)
            self.shadow_words.extend(temp_shadow_words)

        return True

    def search(self, word: str, context: int = 0) -> list:
        result = []
        start_loc = 0
        while True:
            clean_word = word.strip().strip('"').strip('.').lower()
            try:
                match_loc = self.shadow_words.index(clean_word, start_loc)
            except ValueError:
                break

            start_loc = match_loc + 1

            if context == 0:
                result.append(word)
                continue

            context_start = match_loc - context
            context_end = match_loc + context + 1
            if context_start < 0:
                context_start = 0
            if context_end > len(self.words):
                context_end = len(self.words)
            response = ' '.join(self.words[context_start: context_end])
            print(response)
            result.append(response)

        return result
