
def text_justify(words, k):
    line_length = 0

    for i in range(len(words)):
        line_length = len()


words = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
k = 16

assert text_justify(words, k) == [
    "the  quick brown", "fox  jumps  over", "the   lazy   dog"]
