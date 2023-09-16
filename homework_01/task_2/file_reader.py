class FileFilterReader:
    def __init__(self, filename, searching_words, file=None):
        self.file = None
        if file is not None:
            self.file = file
        else:
            self.file = open(filename)
        self.words_for_searching = set()
        for search_word in searching_words:
            self.words_for_searching.add(search_word.lower())

    def find_line(self):
        if len(self.words_for_searching) == 0:
            return []
        res = []
        while True:
            line = self.file.readline()
            if not line:
                break
            for word in line.split(" "):
                if word.lower() in self.words_for_searching:
                    res.append(line.strip())
                    break
        return res

    def __del__(self):
        if self.file is not None:
            self.file.close()
