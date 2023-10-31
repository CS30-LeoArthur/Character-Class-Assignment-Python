# class Character():
#     def __init__(self, name, phrase1, phrase2, level):
#         self.character_name = name
#         self.character_phrase1 = phrase1
#         self.character_phrase2 = phrase2
#         self.character_level = level

#     def speak(self, phrase_num):
#         if phrase_num == 1:
#             print(self.character_phrase1)
#         elif phrase_num == 2:
#             print(self.character_phrase2)
        
#     def set_level(self, new_level):
#         self.character_level == new_level
#         print(str(self.character_level))

# spiderman = Character("Spiderman", "Your friendly neighbourhood spiderman!", "My Spider-Sense is tingling", 0)

# juggernaut = Character("Juggernaut", "I'm the Juggernaut!", "Ain't nothin' -- ain't nobody -- can beat me!", 0)

# spiderman.speak(1)
# juggernaut.set_level(2)
# juggernaut.speak(2)

class Backpack():
    def __init__(self, color, size, items, open):
        self.backpack_color = color
        self.backpack_size = size
        self.backpack_items = items
        self.backpack_open = open
    
    def open_bag(self):
        self.backpack_open = True
        print(f"{self.backpack_size} {self.backpack_color} is now open")
    
    def close_bag(self):
        self.backpack_open = False
        print(f"{self.backpack_size} {self.backpack_color} is now closed")
    
    def put_in(self, item):
        if self.backpack_open == True:
            self.backpack_items.append(item)
            print(f"{item} has been put in to {self.backpack_size} {self.backpack_color}")
        else:
            print("This backpack is not open")
    
    def take_out(self, item):
        if self.backpack_open == True:
            self.backpack_items.pop(item)
            print(f"{item} has been taken out of {self.backpack_size} {self.backpack_color}")
        else:
            print("This backpack is not open")
    
backpack1 = Backpack("blue", "small", [], False)



