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
        for line in self.file:
            line = line.strip()
            if word in line:
                print(line)
                print(word)
                return [word]

        return []
