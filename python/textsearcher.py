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
        cur_line = 0
        for line in lines:
            line = line.strip()
            words = line.split(' ')
            if '' in words:
                words.remove('')
            if word in words:
                clean_word = word.strip()
                clean_word = clean_word.strip('"')
                for x in range(line.count(clean_word)):
                    if context > 0:
                        loc = words.index(clean_word)
                        context_start = loc - context
                        context_end = loc + context + 1
                        if context_start < 0:
                            if cur_line > 0:
                                words = lines[cur_line - 1].strip().split(' ')
                                words.extend(lines[cur_line].strip().split(' '))
                                print(words)
                                loc = words.index(clean_word)
                                context_start = loc - context
                                context_end = loc + context + 1
                            else:
                                context_start = 0
                        response = ' '.join(words[context_start: context_end])
                        print(response)
                        result.append(response)
                    else:
                        result.append(word)
            cur_line += 1

        return result
