from random import randint

def make_fair_dice(sides):
    assert type(sides) == int and sides >= 1, 'Illegal value for sides'
    def dice():
        return randint(1,sides)
    return dice

four_sided = make_fair_dice(4)
six_sided = make_fair_dice(6)

def make_test_dice(*outcomes):

    assert len(outcomes) > 0, 'You must supply outcomes to make_test_dice'
    for o in outcomes:
        assert type(o) == int and o >= 1, 'Outcome is not a positive integer'
    index = len(outcomes) - 1
    def dice():
        nonlocal index
        index = (index + 1) % len(outcomes)
        return outcomes[index]
    return dice

def roll_dice(num_rolls, dice=six_sided):
    
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    total = 0
    while num_rolls > 0:
        if dice() == 1:
            return 1
        else:
            total += dice()
        num_rolls -= 1
    return total
roll_dice(2, make_test_dice(4,6,1))