from bottles import Bottles


def test_the_first_verse():
    expected = (
        "99 bottles of beer on the wall, "
        "99 bottles of beer.\n"
        "Take one down and pass it around, "
        "98 bottles of beer on the wall.\n"
    )
    assert Bottles().verse(99) == expected


def test_another_verse():
    expected = (
        "3 bottles of beer on the wall, "
        "3 bottles of beer.\n"
        "Take one down and pass it around, "
        "2 bottles of beer on the wall.\n"
    )
    assert Bottles().verse(3) == expected


def test_verse_with_2_bottles():
    expected = (
        "2 bottles of beer on the wall, "
        "2 bottles of beer.\n"
        "Take one down and pass it around, "
        "1 bottle of beer on the wall.\n"
    )
    assert Bottles().verse(2) == expected


def test_verse_with_1_bottle():

    expected = (
        "1 bottle of beer on the wall, "
        "1 bottle of beer.\n"
        "Take it down and pass it around, "
        "no more bottles of beer on the wall.\n"
    )
    assert Bottles().verse(1) == expected


def test_verse_with_0_bottles():

    expected = (
        "No more bottles of beer on the wall, "
        "no more bottles of beer.\n"
        "Go to the store and buy some more, "
        "99 bottles of beer on the wall.\n"
    )
    assert Bottles().verse(0) == expected

def test_a_couple_verses():
    expected = (
        "99 bottles of beer on the wall, "
        "99 bottles of beer.\n"
        "Take one down and pass it around, "
        "98 bottles of beer on the wall.\n"
        "\n"
        "98 bottles of beer on the wall, "
        "98 bottles of beer.\n"
        "Take one down and pass it around, "
        "97 bottles of beer on the wall.\n"
    )
    assert Bottles.verses(99, 98) == expected
