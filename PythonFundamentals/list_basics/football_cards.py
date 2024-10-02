team_a = [f'A-{x}' for x in range(1, 12)]
team_b = [f'B-{x}' for x in range(1, 12)]

cards = [x for x in (input().split())]

for card in cards:
    if card in team_a:
        team_a.remove(card)
    elif card in team_b:
        team_b.remove(card)

    if len(team_a) < 7 or len(team_b) < 7:
        print(f'Team A - {len(team_a)}; Team B - {len(team_b)}')
        print('Game was terminated')
        break

else:
    print(f'Team A - {len(team_a)}; Team B - {len(team_b)}')