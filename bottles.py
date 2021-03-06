class Bottles(object):

    @staticmethod
    def song():
        return Bottles.verses(99, 0)

    @staticmethod
    def verses(starting, ending):
        range_ = range(starting, ending - 1, -1)
        verses = "\n".join([Bottles.verse(n) for n in range_])
        return verses

    @staticmethod
    def container(number):
        container = "bottles"
        if number == 1:
            container = "bottle"
        return container

    @staticmethod
    def pronoun(number):
        pronoun = "one"
        if number == 1:
            pronoun = "it"
        return pronoun

    @staticmethod
    def quantity(number=0):
        quantity = number
        if number == 0:
            quantity = "no more"
        return quantity

    @staticmethod
    def verse(number):
        if number == 0:
            verse = (
                "No more bottles of beer on the wall, "
                "no more bottles of beer.\n"
                "Go to the store and buy some more, "
                "99 bottles of beer on the wall.\n"
            )
        elif number == 1:
            verse = (
                "{n} {container} of beer on the wall, "
                "{n} {container} of beer.\n"
                "Take {pronoun} down and pass it around, "
                "{quantity} bottles of beer on the wall.\n"
            ).format(
                n=number,
                quantity=Bottles.quantity(number-1),
                container=Bottles.container(number),
                pronoun=Bottles.pronoun(number),
            )
        else:
            verse = (
                "{n} {container} of beer on the wall, "
                "{n} {container} of beer.\n"
                "Take {pronoun} down and pass it around, "
                "{m} {container_after} of beer on the wall.\n"
            ).format(
                n=number,
                pronoun=Bottles.pronoun(number),
                container=Bottles.container(number),
                m=number-1,
                container_after=Bottles.container(number-1),
            )
        return verse
