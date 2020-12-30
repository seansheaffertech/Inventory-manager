# Inventory-manager

The program is specifically laid out under its current state to function as a dictionary building tool for trading card collections where user can add cards and images then
review with Best.py specific instances of a certain card by searching by the Players name.





#### card_filer.py

1. Creates objects in class Cards(object) with a unique ID(c_id) generator function class_builder(self)
2. Initializes objects created by class_builder function with __init__() function.
3. creates a dictionary(cards) from newly created object.
4. creates a dictionary(reference) from newly created object.
5. Writes cards_dict dictionary to file config.py from reference dictionary
6. Calls in ref_builder(self, reference) function and creates ref_dict reference dictionary with Key: 'c_id' Value: 'name'
7. Writes and formats ref_dict to file name config2.py

#### Best.py
Loads interface with option to search player by name
returns: all instances of objects created with the same attribute 'name' by 'c_id'

Inputs first c_id from list and allows user to select instances up and down the list with forward and back buttons.

Searches unique instances of objects created with identical attribute 'name' from ref_dict

Displays all values from cards_dict and image of card/product.
name
year
brand
product
card number
c_id
image path


