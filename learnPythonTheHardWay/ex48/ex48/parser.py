from .lexicon import DIRECTION_TOKEN, VERB_TOKEN, STOP_TOKEN, NOUN_TOKEN, NUMBER_TOKEN, ERROR_TOKEN

class ParserError(Exception):
    pass

class Sentence(object):

    def __init__(self, subject, verb, obj):
        self.subject = subject[1]
        self.verb = verb[1]
        self.object = obj[1]

def peek(word_list):
    if word_list:
        word = word_list[0]
        return word[0]
    else:
        return None

def match(word_list, expecting):
    if word_list:
        word = word_list.pop(0)
        if word[0] == expecting:
            return word
        else:
            return None
    else:
        return None

def skip(word_list, word_type):
    while peek(word_list) == word_type:
        match(word_list, word_type)

def parse_verb(word_list):
    skip(word_list, STOP_TOKEN)
    if peek(word_list) == VERB_TOKEN:
        return match(word_list, VERB_TOKEN)
    else:
        raise ParserError("Expected a verb next.")

def parse_object(word_list):
    skip(word_list, STOP_TOKEN)
    next_word = peek(word_list)
    if next_word == NOUN_TOKEN:
        return match(word_list, NOUN_TOKEN)
    elif next_word == DIRECTION_TOKEN:
        return match(word_list, DIRECTION_TOKEN)
    else:
        raise ParserError("Expected a noun or direction next.")

PLAYER_TOKEN = 'player'
def parse_subject(word_list):
    skip(word_list, STOP_TOKEN)
    next_word = peek(word_list)
    if next_word == NOUN_TOKEN:
        return match(word_list, NOUN_TOKEN)
    elif next_word == VERB_TOKEN:
        return (NOUN_TOKEN, PLAYER_TOKEN)
    else:
        raise ParserError("Expected a noun or a verb next.")

def parse_sentence(word_list):
    subj = parse_subject(word_list)
    verb = parse_verb(word_list)
    obj = parse_object(word_list)
    return Sentence(subj, verb, obj)

__all__ = ['ParserError', 'Sentence', 'parse_sentence', 'PLAYER_TOKEN']
