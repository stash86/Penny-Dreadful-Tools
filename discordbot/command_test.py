from discordbot import command
from shared import whoosh_search
from shared.container import Container

def test_roughly_matches():
    assert command.roughly_matches('hello', 'hello')
    assert command.roughly_matches('signup', 'Sign Up')
    assert not command.roughly_matches('elephant', 'Tuba')
    assert command.roughly_matches('jmeka', 'j_meka')
    assert command.roughly_matches('modo bugs', 'modo-bugs')

def test_cards_from_queries2():
    bot = Container()
    bot.searcher = whoosh_search.WhooshSearcher()
    assert len(command.cards_from_queries2(['bolt'], bot)) == 1
    assert command.cards_from_queries2(['bolt'], bot)[0].name == 'Lightning Bolt'
