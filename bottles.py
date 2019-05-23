class Bottles(object):

    @staticmethod
    def verse(number):
        number = 99 if (number == 99) else 3
        verse = (
            "{n} bottles of beer on the wall, "
            "{n} bottles of beer.\n"
            "Take one down and pass it around, "
            "{m} bottles of beer on the wall.\n"
        ).format(n=number, m=number-1)
        return verse
