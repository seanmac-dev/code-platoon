from practice import can_drink_beer


def test_can_drink_beer():
    # can drink and from Canada
    assert can_drink_beer(18, "Canada") == True

    # cannot drink and from Canada
    assert can_drink_beer(17, "Canada") == False
