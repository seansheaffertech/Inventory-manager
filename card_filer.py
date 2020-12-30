### Imports ###
import os
import sys  
import random

class Cards(object):
    
    def __init__(self, name, year, brand, product, c_num, id_num, img):
        '''
        Initializes program variables
        -----------------------------
        self.id is a randomly generated number
        self.name is a manual input
        self.year ia a manual input
        self.brand ia a manual input
        self.product is a manual input
        self.c_num is a manual input (card number)
        '''
        self.name = name
        self.year = year
        self.brand = brand
        self.product = product
        self.c_num = c_num
        self.id_num = id_num
        self.img = img

    def class_builder(self):
        '''
        Creates object in the Cards() class,
        and calls the builder function

        Returns
        -------
        New objects in Cards class with unique id (c_??????)
        '''            
        while True:           
            c_id = 'c_' + ''.join(str(random.randint(0,6)) for x in range(6))
            c_id = Cards(input('Please enter a name: '), input('Please enter a year: '), input('Please enter a brand: '), 
                                     input('Please enter a product: '), input('Please enter a card number: '), str(c_id),
                                     input('Please enter image file name: '))             
            c_id.dict_builder()
    
    def dict_builder(self):  
        '''
        Adds to cards dictionary,
        Creates a randomly generated key (c_ + random 6 digit),
        Creates value dictionary
        Creates keys (i.e. 'name', 'year', .etc.)
        Adds user input to key's values.'
        
        Gives user option to exit program,
        
        Writes "cards" dictionary onto config.py
        
        Gives user option to keep formatting in the future or to finish formattin 
        for the dictionary (cards)

        '''
        cards[self.id_num] = {}
        cards[self.id_num]['name'] = self.name
        cards[self.id_num]['year'] = self.year
        cards[self.id_num]['brand'] = self.brand
        cards[self.id_num]['product'] = self.product
        cards[self.id_num]['c_num'] = self.c_num
        cards[self.id_num]['id_num'] = self.id_num
        cards[self.id_num]['image path'] = str(self.img) + ".jpg"
        
        reference[self.id_num] = {}
        reference[self.id_num]['name'] = self.name
        reference[self.id_num]['year'] = self.year
        reference[self.id_num]['brand'] = self.brand
        reference[self.id_num]['product'] = self.product
        reference[self.id_num]['c_num'] = self.c_num
        reference[self.id_num]['id_num'] = self.id_num
        reference[self.id_num]['image path'] = str(self.img) + ".jpg"
              
        quit_prog = input('Press e to exit or any other key to continue: ').capitalize()
        print(self.id_num)        
        file_path = "config.py"
        if quit_prog == 'E':
            cards_dict = reference.copy()
            print(cards_dict)
            start.ref_builder(reference)
            with open(file_path, 'a') as file:
                file.write("\n") 
                file.write('              ' + str(cards)[1:].rstrip('}') + '}')    
                
                kill_file = input('Press (X) to finish file or any key keep it open ').capitalize()
                if kill_file == 'X':
                    file.write('}')
                    sys.exit()
                    
                else:
                    file.write(',')
                    sys.exit()
        else:
            if os.path.exists(file_path): #optional check if file exists
                with open(file_path, 'a') as file:
                    file.write("\n")
                    file.write('              ' + str(cards)[1:].rstrip('}') + '}' + ',') 
                    cards.clear()
                
            else:
                with open(file_path, 'w') as data:
                    data.write('cards_dict = ' + str(cards).rstrip('}') + '}' + ',')  
                    cards.clear()
    
    def ref_builder(self, reference):
        '''
        Takes in dictionary copy and reformats 
        key: 'name'
        value: 'id_num'
        
        Allows for better visibility when 
        
        '''
        
        for k, v in reference.items():
            if v['name'] in ref_dict:
                ref_dict[str(v['name'])] += ', ' + "'" + str(v['id_num']) + "'"
            else:
                ref_dict[str(v['name'])] = "'" + v['id_num'] + "'"
                    
        x = len(ref_dict)    
        file_path = 'config2.py'
        
        for v in ref_dict.keys():
            x -= 1
            if os.path.exists(file_path):
                with open(file_path, 'a') as file:
                    file.write('\n')
                    if x == 0:
                        file.write('            ' "'" + str(v) + "' " + ': ' + "[" + str(ref_dict[str(v)]) + "]" + '}')
                        
                    else:
                        file.write('            ' "'" + str(v) + "' " + ': ' + "[" + str(ref_dict[str(v)]) + "]" + ',')
                        file.write
                        print(x)
        
            else:
                with open(file_path, 'w') as data:
                    data.write('ref_dict = {' + "'" + str(v) + "' " + ': ' + "[ " + str(ref_dict[str(v)]) + " ]" + ',')

if __name__ == '__main__':
     ref_dict = {}
     cards = {}
     reference = {}
     start = Cards('-----', '-----', '-----', '------', '-----', '-----', '-----')
     start.class_builder()

