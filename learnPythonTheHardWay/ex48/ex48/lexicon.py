from operator import itemgetter

def scan(sentence):
    """Convert a string into a list of (type of token, token)
    tuples
    """
    # Initialization
    pairs = ((None, word, i) for i, word in enumerate(sentence.split()))
    output_pairs = []

    # Check for each type of token
    for test in LEXICON_TESTS:
        identified, pairs = test(pairs)
        output_pairs.extend(identified) # Concatenation

    # Ideally, I would have concatenated the lists into a sorted set,
    # such that sorting here would not be necessary.
    # Of course, for small input sizes, it doesn't matter.
    output_pairs.extend(pairs)
    output_pairs = sorted(output_pairs, key=itemgetter(2))
    output_pairs = [(token, word) for token, word, i in output_pairs]
    return output_pairs

DIRECTIONS = frozenset(['north', 'south', 'east', 'west'])
VERBS = frozenset(['go', 'stop', 'kill', 'eat'])
DIRECTION_TOKEN = 'direction'
VERB_TOKEN = 'verb'

LEXICON = {
    DIRECTION_TOKEN: DIRECTIONS,
    VERB_TOKEN: VERBS
}

def make_test(token_name, whiteset):

    def test_pairs(pairs):
        passed = []
        failed = []
        for pair in pairs:
            if pair[1] in whiteset:
                passed.append((token_name, pair[1], pair[2]))
            else:
                failed.append(pair)
        return passed, failed

    return test_pairs

LEXICON_TESTS = [make_test(*item) for item in LEXICON.iteritems()]

__all__ = ['scan']
