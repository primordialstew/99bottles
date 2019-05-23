class Bottles(object):

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
                "1 bottle of beer on the wall, "
                "1 bottle of beer.\n"
                "Take it down and pass it around, "
                "no more bottles of beer on the wall.\n"
            )
        elif number == 2:
            verse = (
                "2 bottles of beer on the wall, "
                "2 bottles of beer.\n"
                "Take one down and pass it around, "
                "1 bottle of beer on the wall.\n"
            )
        else:
            verse = (
                "{n} bottles of beer on the wall, "
                "{n} bottles of beer.\n"
                "Take one down and pass it around, "
                "{m} bottles of beer on the wall.\n"
            ).format(n=number, m=number-1)
        return verse

    @staticmethod
    def verses(a, b):
        return Bottles.verse(a) + "\n" + Bottles.verse(b)
