from nose.tools import *
import unittest
import arithmetic_game_web.game as game

class test_GameOutput(unittest.TestCase):

    class MockScoreKeeper(object):
        def __str__(self):
            return "score"

    def test_format(self):
        """Ensure that the full interface of the class is as expected."""
        inst = "instruction"
        exp = "expression"
        err = Exception("error")
        score = type(self).MockScoreKeeper()
        gameOutputs = [
            game.GameOutput(inst, exp, err, score),
            game.GameOutput(
                score=score,
                instruction=inst,
                expression=exp,
                error=err
            )
        ]
        for gameOutput in gameOutputs:
            assert_is(gameOutput.instruction, inst)
            assert_is(gameOutput.expression, exp)
            assert_equal(gameOutput.error, err.__str__())
            assert_equal(gameOutput.score, score.__str__())

    def test_defaults(self):
        """Ensure that default values are provided for arguments."""
        gameOutput = game.GameOutput()
        assert_is_none(gameOutput.instruction)
        assert_is_none(gameOutput.expression)
        assert_is_none(gameOutput.error)
        assert_is_none(gameOutput.score)
        
    def test_str(self):
        """Check accuracy of debugging output."""
        inst = "instruction"
        exp = "expression"
        err = Exception("error")
        score = type(self).MockScoreKeeper()
        gameOutput = game.GameOutput(inst, exp, err, score)
        actual = gameOutput.__str__()
        expected = (type(gameOutput).__name__) + " = " + ({
            "instruction": inst,
            "expression": exp,
            "error": err.__str__(),
            "score": score.__str__()
        }.__str__())
        assert_equal(actual, expected)
