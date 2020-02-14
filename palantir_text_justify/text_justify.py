
def text_justify(words, k):
    line_length = len(words[0])
    line_contents = [words[0]]
    line_iterator = 0
    for i in range(len(words)):
        line_length += 1+len(words[i+1])  # add 1 for space
        if (line_length < k):
            line_contents.append(words[i+1])
        else:
            # TODO: collect words for line
            nSpaces = k-

            # setup for new line
            line_length = len(words[i+1])
            line_contents = [words[i+1]]


words = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
k = 16

assert text_justify(words, k) == [
    "the  quick brown", "fox  jumps  over", "the   lazy   dog"]
