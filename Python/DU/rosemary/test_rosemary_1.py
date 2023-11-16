import unittest
from rosemary import Item, update

class TestFac(unittest.TestCase):

## self.assertEqual(x,z)
 
    def test_bread_quality_decrese(self):
        bread = Item('Bread', days_left=5, quality=6)
        update(bread)
        self.assertEqual(bread.quality, 5)
    
    def test_bread_days_left_decrese(self):
        bread = Item('Bread', days_left=5, quality=6)
        update(bread)
        self.assertEqual(bread.days_left, 4)
    
    def test_bread_fast_quality_decrese(self):
        bread = Item('Bread', days_left=0, quality=6)
        update(bread)
        self.assertEqual(bread.quality, 4)
    
    def test_bread_fast_quality_0_limit_1(self):
        bread = Item('Bread', days_left=2, quality=0)
        update(bread)
        self.assertEqual(bread.quality, 0)
    
    def test_bread_fast_quality_0_limit_2(self):
        bread = Item('Bread', days_left=0, quality=0)
        update(bread)
        self.assertEqual(bread.quality, 0)
    
    def test_diamond_quality_same(self):
        diamond = Item('Diamond', days_left=5, quality=100)
        update(diamond)
        self.assertEqual(diamond.quality, 100)
    
    def test_diamond_days_left_same(self):
        diamond = Item('Diamond', days_left=5, quality=100)
        update(diamond)
        self.assertEqual(diamond.days_left, 5)
    
    def test_ticket_quality_increse_days_left_11(self):
        ticket = Item('Ticket', days_left=12, quality=2)
        update(ticket)
        self.assertEqual(ticket.quality, 3)
    
    def test_ticket_quality_increse_days_left_10(self):
        ticket = Item('Ticket', days_left=11, quality=8)
        update(ticket)
        self.assertEqual(ticket.quality, 10)
    
    def test_ticket_quality_increse_days_left_6(self):
        ticket = Item('Ticket', days_left=7, quality=10)
        update(ticket)
        self.assertEqual(ticket.quality, 12)
    
    def test_ticket_quality_increse_days_left_5(self):
        ticket = Item('Ticket', days_left=6, quality=10)
        update(ticket)
        self.assertEqual(ticket.quality, 13)
    
    def test_ticket_quality_increse_days_left_1(self):
        ticket = Item('Ticket', days_left=2, quality=10)
        update(ticket)
        self.assertEqual(ticket.quality, 13)
    
    def test_ticket_quality_increse_days_left_0(self):
        ticket = Item('Ticket', days_left=1, quality=10)
        update(ticket)
        self.assertEqual(ticket.quality, 0)
    
    def test_ticket_quality_decrese_days_left_less_0(self):
        ticket = Item('Ticket', days_left=-1, quality=10)
        update(ticket)
        self.assertEqual(ticket.quality, 0)
    
    def test_ticket_quality_50_limit_increse_1(self):
        ticket = Item('Ticket', days_left=12, quality=50)
        update(ticket)
        self.assertEqual(ticket.quality, 50)
    
    def test_ticket_quality_50_limit_increse_2(self):
        ticket = Item('Ticket', days_left=8, quality=50)
        update(ticket)
        self.assertEqual(ticket.quality, 50)
    
    def test_ticket_quality_50_limit_increse_3(self):
        ticket = Item('Ticket', days_left=4, quality=50)
        update(ticket)
        self.assertEqual(ticket.quality, 50)

    def test_aged_brie_quality_increse_days_left_1(self):
        brie = Item('Aged Brie', days_left=1, quality=10)
        update(brie)
        self.assertEqual(brie.quality, 11)
    
    def test_aged_brie_quality_increse_days_left_0(self):
        brie = Item('Aged Brie', days_left=0, quality=10)
        update(brie)
        self.assertEqual(brie.quality, 11)
     
if __name__ == "__main__":
    unittest.main()