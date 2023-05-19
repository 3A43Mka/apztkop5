from event_bus import EventBus


def add_a(obj):
    obj['a'] = 'here I am'


def do_something_funny(journal):
    journal.append('Did something funny')


def do_something_scary(journal):
    journal.append('Did something scary')


def call_grandma(journal):
    journal.append('Called my grandma')


EVENT_A = 'event_a'
FUNNY_EVENT = 'funny_event'
SCARY_EVENT = 'scary_event'
IN_AWKWARD_SITUATION = 'in_awkward_situation'


def test1():
    bus = EventBus()
    some_obj = {}
    bus.add_event_listener(EVENT_A, add_a)
    bus.emit(EVENT_A, some_obj)
    assert some_obj == {'a': 'here I am'}


def test2():
    bus = EventBus()
    logs = []
    bus.add_event_listener(FUNNY_EVENT, do_something_funny)
    bus.emit(FUNNY_EVENT, logs)
    assert logs == ['Did something funny']


def test3():
    bus = EventBus()
    logs = []
    bus.add_event_listener(SCARY_EVENT, do_something_scary)
    bus.unsubscribe(SCARY_EVENT, do_something_scary)
    bus.emit(SCARY_EVENT, logs)
    assert logs == []


def test4():
    bus = EventBus()
    logs = []
    bus.add_event_listener(IN_AWKWARD_SITUATION, do_something_funny)
    bus.add_event_listener(IN_AWKWARD_SITUATION, call_grandma)

    bus.emit(IN_AWKWARD_SITUATION, logs)

    assert logs == ['Did something funny', 'Called my grandma']
