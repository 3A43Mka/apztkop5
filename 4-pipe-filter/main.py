from pipeline import Pipeline


def add_bun(hamburger):
    hamburger.append('bun')


def add_cheese(hamburger):
    hamburger.append('cheese')


def add_sauce(hamburger):
    hamburger.append('sauce')


def add_ham(hamburger):
    hamburger.append('ham')


def main():
    pipeline = Pipeline()
    hamburger = []
    pipeline.add([add_bun, add_sauce, add_ham, add_cheese, add_bun])
    pipeline.execute(hamburger)
    print(hamburger)


if __name__ == '__main__':
    main()
