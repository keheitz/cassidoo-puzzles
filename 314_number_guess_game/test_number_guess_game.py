"""Tests for cassidoo challenge 314 - number guess game"""
from unittest.mock import patch
from random import randrange

from number_guess_game import NumberGuessGame

def test_game_initialize():
    """ Confirm game initializes with expected values"""
    game = NumberGuessGame('kelly', 100)
    assert game.player == 'kelly'
    assert game.turn_count == 0
    assert game.target_val <= 100

@patch('builtins.print')
def test_game_low_guess(mock_print):
    """ Test that a low guess receives matching feedback"""
    game = NumberGuessGame('kelly', 100)
    low_guess = randrange(game.target_val)
    game.take_turn(low_guess)
    mock_print.assert_called_with('higher')
    assert game.turn_count == 1

@patch('builtins.print')
def test_game_high_guess(mock_print):
    """ Test that a high guess receives feedback to guess lower"""
    game = NumberGuessGame('kelly', 100)
    high_guess = randrange(game.target_val, game.target_val + 100)
    game.take_turn(high_guess)
    mock_print.assert_called_with('lower')
    assert game.turn_count == 1

@patch('builtins.print')
def test_game_win(mock_print):
    """ Test that a low guess receives matching feedback"""
    game = NumberGuessGame('kelly', 5)
    print(game.target_val)
    game.take_turn(game.target_val)
    mock_print.assert_called_with('Congrats! You correctly guessed the target in 1 turns')
