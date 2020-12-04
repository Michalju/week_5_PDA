import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
        # This is to setup countries for test
    def setUp(self):
        self.ace_of_spades = Card("spade", 1)
        self.five_of_spades = Card("spade", 5)
        self.six_of_spades = Card("spade", 6)
        self.deck_of_cards = [self.ace_of_spades, self.five_of_spades, self.six_of_spades]
        self.card_game = CardGame()

    def test_check_for_ace(self):
        self.assertTrue(self.card_game.check_for_ace(self.ace_of_spades))
        self.assertFalse(self.card_game.check_for_ace(self.five_of_spades))

    def test_highest_card(self):        
        self.highest_card = self.card_game.highest_card(self.five_of_spades, self.six_of_spades)
        self.assertEqual(self.highest_card.value, 6)

        self.highest_card = self.card_game.highest_card(self.six_of_spades, self.five_of_spades)
        self.assertEqual(self.highest_card.value, 6)

    def test_cards_total(self):
        self.assertEqual(self.card_game.cards_total(self.deck_of_cards),"You have a total of 12")