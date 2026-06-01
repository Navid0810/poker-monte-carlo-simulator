wins = 0
ties = 0

for _ in range(100000):

    deck = Deck(evaluator)

    deck.cards.remove(hero[0])
    deck.cards.remove(hero[1])

    deck.cards.remove(villain[0])
    deck.cards.remove(villain[1])

    deck.shuffle()

    board = deck.deal(5)

    hero_rank = evaluator.evaluate_seven(
        hero + board
    )

    villain_rank = evaluator.evaluate_seven(
        villain + board
    )

    if hero_rank > villain_rank:
        wins += 1

    elif hero_rank == villain_rank:
        ties += 1

equity = (wins + ties / 2) / 100000
