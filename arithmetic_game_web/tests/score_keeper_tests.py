from nose.tools import *
from mock import patch

from arithmetic_game_web.score_keeper import ScoreKeeper

@patch('time.time')
def test_start_round(mock_time):
    sk = ScoreKeeper()
    sk.start_round()
    assert_equal(sk._current_time, mock_time())
