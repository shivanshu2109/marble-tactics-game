from src.config import STARTING_BASE_HP, SHOP_PRICES

class Team:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.outer_position = 0
        self.base_hp = STARTING_BASE_HP
        self.inventory = {"FOOD" : 0, "DRUGS": 0, "ALCOHOL": 0, "PROTEIN": 0}
        self.cards = {"POS_CARD": [], "NEG_CARD": []}

    def add_points(self, amount):
        self.points += amount
        return self.points
    
    def deduct_points(self, amount):
        self.points  = max(0, self.points - amount)
        return self.points

    def buy_item(self, item_name):
        if item_name not in SHOP_PRICES:
            return False
        cost = SHOP_PRICES[item_name]

        if self.points < cost:
            return False
        
        self.points -= cost
        if item_name in self.inventory:
            self.inventory[item_name] += 1
        
        return True
    
    def use_resource(self, resource_name):
        if resource_name in self.inventory and self.inventory[resource_name] > 0:
            self.inventory[resource_name] -= 1
            return True 
        else:
            return False