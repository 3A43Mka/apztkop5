from blackboard import Blackboard
from controller import Controller
from ai_text_generator import AITextGenerator
from ai_numbers_generator import AINumbersGenerator


TEXT_GENERATOR = 'TEXT_GENERATOR'
NUMBER_GENERATOR = 'NUMBER_GENERATOR'


def main():
    blackboard1 = Blackboard()
    text_generator = AITextGenerator()
    number_generator = AINumbersGenerator()
    controller1 = Controller(blackboard1)

    controller1.add_source(TEXT_GENERATOR, text_generator)
    controller1.add_source(NUMBER_GENERATOR, number_generator)

    # executing some AI computations
    controller1.execute_source(TEXT_GENERATOR, 'some args')
    controller1.execute_source(NUMBER_GENERATOR, 42)

    blackboard1.display_data()


if __name__ == '__main__':
    main()
