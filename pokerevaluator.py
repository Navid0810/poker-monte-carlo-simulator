lass PokerEvaluator:

    def __init__(self):

        # Prime number assigned to each rank.
        # For future optimisation
        self.rank_to_prime = {
            2: 2,
            3: 3,
            4: 5,
            5: 7,
            6: 11,
            7: 13,
            8: 17,
            9: 19,
            10: 23,
            11: 29,  # Jack
            12: 31,  # Queen
            13: 37,  # King
            14: 41   # Ace
        }

    # CARD ENCODING

    def card_to_int(self, rank, suit):

        rank_bit = 1 << (rank - 2)
        prime = self.rank_to_prime[rank]

        # Pack everything into one integer:
        # bits 0-12   : rank bitmask
        # bits 13-15  : suit
        # bits 16+    : prime number
        return rank_bit | (suit << 13) | (prime << 16)

    def get_rank(self, card):

        rank_mask = card & 0x1FFF

        for rank in range(2, 15):
            if rank_mask == (1 << (rank - 2)):
                return rank

    def get_suit(self, card):

        return (card >> 13) & 0x7

    def get_prime(self, card):

        return (card >> 16) & 0xFFF

    # STRAIGHT DETECTION

    def is_straight(self, ranks):

        unique = sorted(set(ranks))

        if len(unique) != 5:
            return False, None

        # Wheel straight:
        # A-2-3-4-5
        if unique == [2, 3, 4, 5, 14]:
            return True, 5

        if unique[-1] - unique[0] == 4:
            return True, unique[-1]

        return False, None

    # 5 CARD EVALUATION

    def evaluate_five(self, cards):

        ranks = [self.get_rank(card) for card in cards]
        suits = [self.get_suit(card) for card in cards]

        counts = Counter(ranks)

        frequencies = sorted(
            counts.values(),
            reverse=True
        )

        is_flush = len(set(suits)) == 1

        is_straight, straight_high = self.is_straight(ranks)

        sorted_ranks = sorted(ranks, reverse=True)

        # Straight Flush
        if is_flush and is_straight:
            return (8, straight_high)

        # Four of a Kind
        if frequencies == [4, 1]:

            quad_rank = max(
                rank
                for rank, count in counts.items()
                if count == 4
            )

            kicker = max(
                rank
                for rank, count in counts.items()
                if count == 1
            )

            return (7, quad_rank, kicker)

        # Full House
        if frequencies == [3, 2]:

            trip_rank = max(
                rank
                for rank, count in counts.items()
                if count == 3
            )

            pair_rank = max(
                rank
                for rank, count in counts.items()
                if count == 2
            )

            return (6, trip_rank, pair_rank)

        # Flush
        if is_flush:
            return (5, *sorted_ranks)

        # Straight
        if is_straight:
            return (4, straight_high)

        # Three of a Kind
        if frequencies == [3, 1, 1]:

            trip_rank = max(
                rank
                for rank, count in counts.items()
                if count == 3
            )

            kickers = sorted(
                [
                    rank
                    for rank, count in counts.items()
                    if count == 1
                ],
                reverse=True
            )

            return (3, trip_rank, *kickers)

        # Two Pair
        if frequencies == [2, 2, 1]:

            pairs = sorted(
                [
                    rank
                    for rank, count in counts.items()
                    if count == 2
                ],
                reverse=True
            )

            kicker = max(
                rank
                for rank, count in counts.items()
                if count == 1
            )

            return (2, pairs[0], pairs[1], kicker)

        # One Pair
        if frequencies == [2, 1, 1, 1]:

            pair_rank = max(
                rank
                for rank, count in counts.items()
                if count == 2
            )

            kickers = sorted(
                [
                    rank
                    for rank, count in counts.items()
                    if count == 1
                ],
                reverse=True
            )

            return (1, pair_rank, *kickers)

        # High Card
        return (0, *sorted_ranks)

    # 7 CARD HOLD'EM EVALUATION

    def evaluate_seven(self, cards):

        best_hand = None

        for five_card_combo in combinations(cards, 5):

            rank = self.evaluate_five(five_card_combo)

            if best_hand is None or rank > best_hand:
                best_hand = rank

        return best_hand
