from operator import itemgetter

def scan(sentence):
    """Convert a string into a list of (type of token, token)
    tuples
    """
    # Initialization
    pairs = ((None, word, i) for i, word in enumerate(sentence.split()))
    output_pairs = []
    directions, pairs = test_directions(pairs)
    output_pairs.extend(directions) # Concatenation

    output_pairs = sorted(output_pairs, key=itemgetter(2))
    output_pairs = [(token, word) for token, word, i in output_pairs]
    return output_pairs

DIRECTIONS = frozenset(['north', 'south', 'east', 'west'])
direction_token = 'direction'

def test_directions(pairs):
    directions = []
    output_pairs = []
    for pair in pairs:
        if pair[1] in DIRECTIONS:
            directions.append((direction_token, pair[1], pair[2]))
        else:
            output_pairs.append(pair)

    return directions, output_pairs

__all__ = [scan]
