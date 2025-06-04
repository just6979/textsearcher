import string


class TextSearcher(object):
    file = None

    def __init__(self):
        pass

    def load(self, file_path: str) -> bool:
        if file_path is None:
            return False

        try:
            self.file = open(file_path)
        except FileNotFoundError:
            return False

        return True

    def search(self, word: str, context: int = 0) -> list:
        result = []
        for line in self.file:
            line = line.strip()
            words = line.split(' ')
            if word in words:
                for x in range(line.count(word)):
                    if context > 0:
                        loc = words.index(word)
                        result.append(' '.join(words[loc - context: loc + context + 1]))
                    else:
                        result.append(word)

        return result
