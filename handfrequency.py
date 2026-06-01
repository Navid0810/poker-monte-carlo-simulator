from collections import defaultdict

frequencies = defaultdict(int)

evaluator = PokerEvaluator()

for _ in range(100000):

    deck = Deck(evaluator)
    deck.shuffle()

    hole = deck.deal(2)
    board = deck.deal(5)

    rank = evaluator.evaluate_seven(hole + board)

    hand_type = rank[0]

    frequencies[hand_type] += 1

for hand_type in sorted(frequencies):
    percentage = (
        frequencies[hand_type]
        / 100000
        * 100
    )

    print(hand_type, percentage)
