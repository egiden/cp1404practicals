from guitar import Guitar

gibson_guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
another_guitar = Guitar("Another Guitar", 2007, 23.41)


def test_get_age_method(guitar_instance, expected_value):
    print(f"{guitar_instance.name} get_age() - Expected {expected_value}. Got {guitar_instance.get_age()}")


def test_is_vintage_method(guitar_instance, expected_value):
    print(f"{guitar_instance.name} is_vintage() - Expected {expected_value}. Got {guitar_instance.is_vintage()}")


# Test get_age method
test_get_age_method(gibson_guitar, 103)
test_get_age_method(another_guitar, 18)

# Test is_vintage method
test_is_vintage_method(gibson_guitar, True)
test_is_vintage_method(another_guitar, False)
