from random import shuffle


class Deck:

    def __init__(self, evaluator):

        # Generate all 52 cards
        # rank: 2-14
        # suit:
        # 0 = clubs
        # 1 = diamonds
        # 2 = hearts
        # 3 = spades

        self.cards = [
            evaluator.card_to_int(rank, suit)
            for rank in range(2, 15)
            for suit in range(4)
        ]

    def shuffle(self):

        shuffle(self.cards)

    def deal(self, num_cards):

        dealt_cards = self.cards[:num_cards]

        self.cards = self.cards[num_cards:]

        return dealt_cards

    def remaining(self):

        return len(self.cards)
