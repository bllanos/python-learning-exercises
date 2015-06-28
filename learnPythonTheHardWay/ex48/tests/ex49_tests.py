from nose.tools import *
import ex48
from ex48.parser import *
from ex48.lexicon import *

@raises(ParserError)
def test_empty():
    parse_sentence([])

def test_subject_verb_obj():
    words = [(NOUN_TOKEN, 'I'), (VERB_TOKEN, 'went'), (NOUN_TOKEN, 'there')]
    words_copy = words[:]
    sentence = parse_sentence(words)
    assert_equal(sentence.subject, words_copy[0][1])
    assert_equal(sentence.verb, words_copy[1][1])
    assert_equal(sentence.object, words_copy[2][1])

def test_with_stops():
    words = [(STOP_TOKEN, 'a'),
             (NOUN_TOKEN, 'I'),
             (STOP_TOKEN, 'a'),
             (VERB_TOKEN, 'went'),
             (STOP_TOKEN, 'a'),
             (NOUN_TOKEN, 'there'),
             (STOP_TOKEN, 'a')]
    words_copy = words[1::2]
    sentence = parse_sentence(words)
    assert_equal(sentence.subject, words_copy[0][1])
    assert_equal(sentence.verb, words_copy[1][1])
    assert_equal(sentence.object, words_copy[2][1])

@raises(ParserError)
def test_subject_obj():
    words = [(NOUN_TOKEN, 'I'), (STOP_TOKEN, 'a'), (NOUN_TOKEN, 'there')]
    sentence = parse_sentence(words)

def test_player_verb_direction():
    words = [(VERB_TOKEN, 'Find'), (DIRECTION_TOKEN, 'north')]
    words_copy = words[:]
    sentence = parse_sentence(words)
    assert_equal(sentence.subject, PLAYER_TOKEN)
    assert_equal(sentence.verb, words_copy[0][1])
    assert_equal(sentence.object, words_copy[1][1])

@raises(ParserError)
def test_missing_object():
    words = [(NOUN_TOKEN, 'I'), (VERB_TOKEN, 'went'), (VERB_TOKEN, 'ran')]
    sentence = parse_sentence(words)

# Testing some uncovered code by breaking the public-private barrier
def test_match():
    match = getattr(ex48.parser, 'match')
    assert_is_none(match([], NOUN_TOKEN))
    assert_is_none(match([(VERB_TOKEN, 'Find')], NOUN_TOKEN))
