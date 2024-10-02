cards = input().split()
count = int(input())
a = int(len(cards) / 2)



for i in range(count):
    first_deck = cards[:a]
    second_deck = cards[a:]

    for e in range(0, a, 2):
        cards[e] = first_deck[int(e / 2)]
        cards[e + 1] = second_deck[int(e / 2)]
        cards[2 * a -1 - e] = second_deck[-1 - int(e / 2)]
        cards[2 * a -2 - e] = first_deck[-1 - int(e / 2)]

print(cards)