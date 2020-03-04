
def text_justify(words, k):
    lines = []
    line_iterator = 0
    line_contents = [words[0]]
    line_length = len(words[0])
    for i in range(len(words)-1):
        temp = line_length+1+len(words[i+1])
        if (temp < k):
            line_contents.append(words[i+1])
            line_length += 1+len(words[i+1])  # add 1 for space

        if temp >= k or i == len(words)-2:
            gaps = len(line_contents)-1
            fill = k - line_length + gaps
            even_spacing = int(fill/gaps)
            rem = fill % gaps
            # allocate whitespace as evenly as possible
            if rem == 0:
                lines.append((' '*even_spacing).join(line_contents))
            else:
                lines.append(
                    (' '*(even_spacing+1)).join(line_contents[0:(gaps-rem+1)]))
                if rem > 1:
                    lines[line_iterator] = lines[line_iterator] + \
                        (' ' *
                         even_spacing).join(line_contents[(gaps-rem+1):len(line_contents)])
                else:
                    lines[line_iterator] = lines[line_iterator] + \
                        (' ' * even_spacing) + \
                        line_contents[len(line_contents)-1]

            line_iterator += 1
            # setup for new line
            line_length = len(words[i+1])
            line_contents = [words[i+1]]

    return lines


words = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
k = 16

assert text_justify(words, k) == [
   "the  quick brown", "fox  jumps  over", "the   lazy   dog"]
