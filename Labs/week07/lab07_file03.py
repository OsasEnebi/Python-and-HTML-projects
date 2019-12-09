unique_words = []

with open('g_words.txt', 'r') as g:
    for lines in g:
        if lines[0] == 'g':
            line = lines.rstrip()
            unique_words.append(lines)
    print(unique_words)

