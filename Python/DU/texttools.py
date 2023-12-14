def compute_word_frequencies(file_name):
    dic = {}
    with open(file_name, "rt", encoding="UTF-8") as f:
        for line in f.readlines():
            words = []
            words = line.split()
            for i, _ in enumerate(words):
                print(dic != words[i])
                if dic != words[i]:
                    dic[words[i]] = 1
                else:
                    dic[words[i]] += 1
                
    return dic

if __name__ == "__main__":
    dic = compute_word_frequencies("example.txt")
    print(dic)