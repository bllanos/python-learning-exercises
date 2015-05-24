from score_keeper import ScoreKeeper
from arithmetic_expression import ArithmeticExpression

def _prompt_for_integer():
    while True:
        try:
            string = raw_input("> ")
            return int(string)
        except ValueError as err:
            print "Please enter an integer."

class Game(object):
    """A small console-based arithmetic quiz game."""
    
    def __init__(self):
        self._score = ScoreKeeper()
        
    def run(self):
        print """
        Try to answer the following questions correctly and quickly.
        Press Enter to begin. Press CTRL+D to exit any time.
        """
        try:
            raw_input()
        except EOFError:
            print "See you later."
            return None
            
        correct = True
        try:
            while correct:
                expression = ArithmeticExpression()
                print "%s" % expression.get_question_string()
                self._score.start_round()
                test_answer = _prompt_for_integer()
                correct = expression.check_answer(test_answer)
                self._score.end_round(correct)
                if correct:
                    print "Correct!"
                    raw_input("Press Enter to continue.")
                else:
                    print "Incorrect. The answer is: "
                    correct = False
                    print "%s" % expression.get_answer_string()
            print "End of game."
        except EOFError:
            print "You have quit."
            
        print self._score
        return None
    
__all__ = [Game]
