class Item:
    def __init__(self, name, days_left, quality):
        self.name = name
        self.days_left = days_left
        self.quality = quality
        pass
    
def update(item):
    item.days_left -= 1
    if(item.name == "Diamond"):
        item.days_left += 1
        item.quality = 100
        return
    elif(item.name == "Aged Brie"):
        if(item.quality < 50):
            item.quality += 1
            return
        else:
            item.quality = 50
            return
    elif(item.name == "Ticket"):
        if(item.days_left > 10):
            if(item.quality < 50):
                item.quality += 1
                return
            else:
                item.quality = 50
                return
        elif(item.days_left > 5):
            if(item.quality < 50):
                item.quality += 2
                return
            else:
                item.quality = 50
                return
        elif(item.days_left > 0):
            if(item.quality < 50):
                item.quality += 3
                return
            else:
                item.quality = 50
                return
        else:
            item.quality = 0
        return
    else:
        if(item.days_left <= 0):
            item.quality -= 1
            
        if(item.quality <= 0):
            item.quality = 0
            return
        else:
            item.quality -= 1
            return

def item_print(item):
    print(item.name)
    print(item.days_left)
    print(item.quality)

def updates(bread, brie, tickets, diamonds):
    update(bread)
    update(brie)
    update(tickets)
    update(diamonds)
    pass

if __name__ == "__main__":
    brie = Item('Aged Brie', days_left=3, quality=5)
    tickets = Item('Ticket', days_left=11, quality=2)
    diamonds = Item('Diamond', days_left=3, quality=85)
    bread  = Item('Bread', days_left=3, quality=5)

    for idx in range(15):
        updates(bread,brie,tickets,diamonds)
        print("Round:", idx)
        ##item_print(bread)
        ##item_print(brie)
        ##item_print(tickets)
        item_print(diamonds)