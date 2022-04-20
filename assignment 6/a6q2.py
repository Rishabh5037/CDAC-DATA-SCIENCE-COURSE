counts = dict()
line = input('Enter a line of text:')
line_list = list(line)
print(line_list)

for c in line:
    counts[c]=line.count(c)

print(counts)
print(sorted(counts.keys(),reverse=True))