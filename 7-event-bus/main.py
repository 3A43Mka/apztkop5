from event_bus import EventBus


def sausage_cutter(pizza):
    pizza['sausages'] = True


def pizza_packer(pizza):
    pizza['is_in_the_box'] = True


def icing_on_the_cake_putter(pizza):
    pizza['icing'] = True


def delivery_man(args):
    print(f'Delivery Man: went out to deliver the pizza')


PIZZA_IS_READY = 'pizza_is_ready'
PIZZA_IS_BEING_PREPARED = 'pizza_is_being_prepared'
DELIVER_PIZZA = 'deliver_pizza'


def main():
    bus = EventBus()
    # subscribing event listeners to events
    bus.add_event_listener(PIZZA_IS_BEING_PREPARED, sausage_cutter)
    bus.add_event_listener(PIZZA_IS_READY, pizza_packer)
    bus.add_event_listener(PIZZA_IS_READY, icing_on_the_cake_putter)
    bus.add_event_listener(DELIVER_PIZZA, delivery_man)

    # now emitting events

    new_pizza = {}
    bus.emit(PIZZA_IS_BEING_PREPARED, new_pizza)
    print(f'Pizza should now have only sausages')
    print(new_pizza)
    bus.emit(PIZZA_IS_READY, new_pizza)
    print(f'Pizza now should have icing and be packed')
    print(new_pizza)
    bus.emit(DELIVER_PIZZA)
    print(f'Delivery man should now be on route to deliver pizza')


if __name__ == '__main__':
    main()
