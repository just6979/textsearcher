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
        lines = self.file.readlines()
        words = []
        for line in lines:
            temp_words = [word.strip() for word in line.strip().split()]
            while '' in temp_words:
                temp_words.remove('')
            words.extend(temp_words)

        print(words)

        start_loc = 0
        matches_remaining = True

        while matches_remaining:
            try:
                match_loc = words.index(word, start_loc)
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
            if context_end > len(words):
                context_end = len(words)
            response = ' '.join(words[context_start: context_end])
            print(response)
            result.append(response)

        return result
