import random
import csv
from random import shuffle
# Reads csv a prints it in lists
card_name_to_value_dict = {}
with open('cardfile.csv', newline='') as csvfile:
   
    reader = csv.DictReader(csvfile, delimiter= '\t')
    reader.fieldnames = [field.strip().lower() for field in reader.fieldnames]
   
    for row in reader:
        print(row.keys())
        print(row.items())
        print(row.values())
            
        print(row['face'], row['suit'], row['value'])





#_________________________
#CSV Notes
 # writer??? fieldnames = ['Show_Number', 'Air_Date', 'Round', 'Category', 'Value', 'Question', 'Answer']
    #rows = list(reader)



    # card_name_to_value_dict = {}
# suit_list = []
# with open('cardfile.csv')as csvfile:
#      PlayingCards = csv.reader(csvfile, delimiter = ',')
#      for row in PlayingCards:
#          new_cardname, new_cardvalue, new_suitvalue = row
#          if new_cardname:
#             card_name_to_value_dict[new_cardname] = new_cardvalue
#          if new_suitvalue.strip():
#             suit_list.append(new_suitvalue.replace("\n",""))
# string_result = "\n".join(["\t".join([name, value]) for each_suit in suit_list for name,value in card_name_to_value_dict.items()])      
# print (string_result)
# The string result can be saved into a file for submission

#Card Notes  _______________________________________________________________________  

# def RANKS(): return [ "Ace", "2", "3", "4", "5", "6", "7","8", "9", "10", "Jack", "Queen", "King" ]
# def SUITS(): return [ "Clubs", "Diamonds", "Hearts", "Spades" ]

# class Card:
#     def __init__(self, value, color):
#         self.value = value
#         self.color = color

# colors = ['heart', 'diamonds', 'spades', 'clubs']


# deck = [Card(value, color) for value in range(1, 14) for color in colors]

# print(RANKS())
# print(SUITS())