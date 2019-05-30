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
                "{n} bottle of beer on the wall, "
                "{n} bottle of beer.\n"
                "Take it down and pass it around, "
                "no more bottles of beer on the wall.\n"
            ).format(n=number)
        else:
            verse = (
                "{n} bottles of beer on the wall, "
                "{n} bottles of beer.\n"
                "Take one down and pass it around, "
                "{m} {container} of beer on the wall.\n"
            ).format(
                n=number,
                m=number-1,
                container=Bottles.container(number-1),
            )
        return verse
