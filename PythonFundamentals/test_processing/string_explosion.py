
text = input()
clean_text = list(text)
counter = 0
while counter < len(clean_text) - 1:
    if clean_text[counter] == '>' and clean_text[counter + 1].isdigit():
       for_change = int(clean_text[counter + 1])
       while for_change > 0 and counter < len(clean_text) - 1:
           if clean_text[counter + 1] == '>':
               if clean_text[counter + 2].isdigit():
                   for_change += int(clean_text[counter + 2])
               counter += 1
               continue
           for_change -= 1
           clean_text.pop(counter + 1)
    else:
        counter += 1

print(*clean_text, sep='')
