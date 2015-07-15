from score_keeper import ScoreKeeper
from arithmetic_expression import ArithmeticExpression

class GameOverMsg(Exception):
    pass

class BadInputMsg(Exception):
    pass

QUIT = 'quit'

def parse_input(input_str):
    words = input_str.split()
    if len(words) > 1:
        raise BadInputMsg("Expected a single word or number as input.")
    else:
        word = words[0]
        if word == QUIT:
            raise GameOverMsg("You have quit.")
        try:
            return int(input_str)
        except ValueError as err:
            raise BadInputMsg("Please enter an integer.")

def run_game():
    """A small arithmetic quiz game.

    Runs as a generator, which yields instructions for the player,
    and stops yielding messages after the game is over.
    """
    
    score = ScoreKeeper()
        
    yield "Try to answer the following questions correctly and quickly."
        "Press the button to proceed and to send input"
        "from the text field."
        "You can quit by typing '%s' into the field." % QUIT

    try:
        while True:
            expression = ArithmeticExpression()
            # Starting the round before displaying the question means
            # that network latency and rendering speed are not taken into account.
            score.start_round()
            question = expression.get_question_string()
            test_answer = (yield question)
            retry = True
            while retry:
                try:
                    test_answer = parse_input(test_answer)
                    retry = False
                    correct = expression.check_answer(test_answer)
                    score.end_round(correct)
                    if correct:
                        yield "Correct!"
                    else:
                        raise GameOverMsg("Incorrect. The answer is: "
                                "%s" % expression.get_answer_string()
                              )
                except BadInputMsg as err:
                    test_answer = (yield "%s The question was %s." % (err, question))
    except GameOverMsg as err:
        yield "%s End of game. %s" % (err, score)

    return
    
__all__ = [run_game]
