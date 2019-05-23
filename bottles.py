class Bottles(object):

    @staticmethod
    def verse(number):
        if number == 2:
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
