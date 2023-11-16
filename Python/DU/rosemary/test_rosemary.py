import unittest
from rosemary import Item, update

##class TestFac(unittest.TestCase):

def test_days_and_quality():
    bread = Item('Bread', days_left=1, quality=6)
    update(bread)
    return bread.quality == 5 and bread.days_left == 0

def test_bread_name():
    bread = Item('Bread', days_left=6, quality=1)
    update(bread)
    return bread.name == 'Bread'

def test_bread_quality_decrese():
    bread = Item('Bread', days_left=5, quality=6)
    update(bread)
    return bread.quality == 5

def test_bread_days_left_decrese():
    bread = Item('Bread', days_left=5, quality=6)
    update(bread)
    return bread.days_left == 4

def test_bread_fast_quality_decrese():
    bread = Item('Bread', days_left=0, quality=6)
    update(bread)
    return bread.quality == 4

def test_bread_fast_quality_0_limit_1():
    bread = Item('Bread', days_left=2, quality=0)
    update(bread)
    return bread.quality == 0

def test_bread_fast_quality_0_limit_2():
    bread = Item('Bread', days_left=0, quality=1)
    update(bread)
    return bread.quality == 0

def test_diamond_quality_same():
    diamond = Item('Diamond', days_left=5, quality=100)
    update(diamond)
    return diamond.quality == 100

def test_diamond_days_left_same():
    diamond = Item('Diamond', days_left=5, quality=100)
    update(diamond)
    return diamond.days_left == 5

def test_diamond_name():
    diamond = Item('Diamond', days_left=0, quality=50)
    update(diamond)
    return diamond.name == 'Diamond'

def test_ticket_quality_increse_days_left_11():
    ticket = Item('Tickets', days_left=12, quality=2)
    update(ticket)
    return ticket.quality == 3

def test_ticket_quality_increse_days_left_10():
    ticket = Item('Tickets', days_left=11, quality=8)
    update(ticket)
    return ticket.quality == 9

def test_ticket_quality_increse_days_left_6():
    ticket = Item('Tickets', days_left=7, quality=10)
    update(ticket)
    return ticket.quality == 12

def test_ticket_quality_increse_days_left_5():
    ticket = Item('Tickets', days_left=6, quality=10)
    update(ticket)
    return ticket.quality == 12

def test_ticket_quality_increse_days_left_4():
    ticket = Item('Tickets', days_left=4, quality=10)
    update(ticket)
    return ticket.quality == 13

def test_ticket_quality_increse_days_left_9():
    ticket = Item('Tickets', days_left=9, quality=10)
    update(ticket)
    return ticket.quality == 12

def test_ticket_quality_increse_days_left_1():
    ticket = Item('Tickets', days_left=2, quality=10)
    update(ticket)
    return ticket.quality == 13

def test_ticket_quality_increse_days_left_0():
    ticket = Item('Tickets', days_left=0, quality=10)
    update(ticket)
    return ticket.quality == 0

def test_ticket_quality_decrese_days_left_less_0():
    ticket = Item('Tickets', days_left=-1, quality=50)
    update(ticket)
    return ticket.quality == 0

def test_ticket_quality_50_limit_increse_1():
    ticket = Item('Tickets', days_left=12, quality=50)
    update(ticket)
    return ticket.quality == 50

def test_ticket_quality_50_limit_increse_2():
    ticket = Item('Tickets', days_left=8, quality=50)
    update(ticket)
    return ticket.quality == 50

def test_ticket_quality_50_limit_increse_3():
    ticket = Item('Tickets', days_left=4, quality=50)
    update(ticket)
    return ticket.quality == 50

def test_ticket_quality_1_days():
    ticket = Item('Tickets', days_left=11, quality=45)
    update(ticket)
    return ticket.quality == 46 and ticket.days_left == 10

def test_ticket_quality_2_days():
    ticket = Item('Tickets', days_left=6, quality=45)
    update(ticket)
    return ticket.quality == 47 and ticket.days_left == 5

def test_ticket_quality_3_days():
    ticket = Item('Tickets', days_left=1, quality=45)
    update(ticket)
    return ticket.quality == 48 and ticket.days_left == 0

def test_ticket_days_decrese():
    ticket = Item('Tickets', days_left=4, quality=50)
    update(ticket)
    return ticket.days_left == 3

def test_ticket_name():
    brie = Item('Tickets', days_left=0, quality=50)
    update(brie)
    return brie.name == 'Tickets'

def test_ticket_days_decrese():
    brie = Item('Tickets', days_left=4, quality=50)
    update(brie)
    return brie.days_left == 3

def test_aged_brie_days_decrese():
    brie = Item('Aged Brie', days_left=1, quality=10)
    update(brie)
    return brie.days_left == 0

def test_aged_brie_quality_increse_days_left_1():
    brie = Item('Aged Brie', days_left=1, quality=10)
    update(brie)
    return brie.quality == 11

def test_aged_brie_quality_increse_days_left_0():
    brie = Item('Aged Brie', days_left=0, quality=10)
    update(brie)
    return brie.quality == 11

def test_aged_brie_quality_increse_days_below_0():
    brie = Item('Aged Brie', days_left=-1, quality=10)
    update(brie)
    return brie.quality == 11

def test_aged_brie_quality_maximal_50_increse_1():
    brie = Item('Aged Brie', days_left=0, quality=50)
    update(brie)
    return brie.quality == 50

def test_aged_brie_name():
    brie = Item('Aged Brie', days_left=0, quality=50)
    update(brie)
    return brie.name == 'Aged Brie'
##if __name__ == "__main__":
  ##  unittest.main()