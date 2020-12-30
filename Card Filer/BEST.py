### GUI Imports ###
import tkinter as tk
from tkinter import *
from tkinter import ttk
from config2 import ref_dict
from config import cards_dict
from PIL import ImageTk, Image
from tkinter import filedialog

# Create instance
root = Tk()
# Creates a title
root.title('Baseball card inventory manager')
# Allows window to be resizeable
root.resizable(width = True, height = True) 

def button_search():
    '''
    Searches ref_dict.items() by 'player name'

    Returns
    -------
    list of unique card ID numbers attributed to player

    '''
    output_playerName.delete(0, END)
    current = search_playerName.get()   
    search_idNum.delete(0, END)
    for k, v in ref_dict.items():
        try:
            if k == current:
                output_playerName.insert(0, v)
                search_idNum.insert(0, v[0:1])            
            elif current not in ref_dict:
                output_playerName.insert(0, 'Player not in registry')
                break
        except:
            pass
         
def button_profile():
    '''
    Searches cards_dict.items by Unique ID number

    Returns
    
    -------
    Card data attributed with unique ID 
    'name', 'year', 'brand', 'product', 'card number', (photo of card)

    '''
    output_idNum.delete(0, END)
    output_idNum.delete(0, END)
    output_name.delete(0, END)
    output_year.delete(0, END)
    output_brand.delete(0, END)
    output_product.delete(0, END)
    output_c_num.delete(0, END)
    
    current = search_idNum.get()
    
    for k, v in cards_dict.items():
        
        if k == current:
            output_idNum.insert(0, v['id_num'])
            output_name.insert(0, v['name'])
            output_year.insert(0, v['year'])
            output_brand.insert(0, v['brand'])
            output_product.insert(0, v['product'])
            output_c_num.insert(0, v['c_num'])
            
            
def nextButton():
    '''
    Locates next unique ID number from ref_dict

    Returns
    -------
    Next ID number

    '''
    entry_name = search_playerName.get()
    entry_id = search_idNum.get()
    test_key = 'is'
    temp = list(ref_dict[entry_name]) 
    for i in temp:
        try:
            if i == entry_id:
                res = temp[temp.index(i) + 1] 
                search_idNum.delete(0, END)
                search_idNum.insert(0, str(res))
        except IndexError:
            search_idNum.delete(0, END)
            search_idNum.insert(0, temp[-1])
    
def lastButton():
    '''
    Locates last unique ID number from ref_dict

    Returns
    -------
    Last ID number searched

    '''
    entry_name = search_playerName.get()
    entry_id = search_idNum.get()
    test_key = 'is'
    temp = list(ref_dict[entry_name]) 
    for i in temp:
        if i == entry_id:
            res = temp[temp.index(i) - 1]
            search_idNum.delete(0, END)
            search_idNum.insert(0, str(res))      
        else:
            search_idNum.delete(0, END)
            search_idNum.insert(0, temp[0])
            continue

def imageOpener():
    '''
    Finds image from file, resizes, and 

    Returns
    -------
    None.

    '''
    x = openfilename()
    img = Image.open(x)
    img = img.resize((500, 700), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    img_screen = Label(root, image=img)
    img_screen.image = img
    img_screen.grid(column=0, row=9, columnspan=5)
    
def openfilename():
    current = search_idNum.get()    
    for k, v in cards_dict.items():
        if k == current:
            filename = v['image_path']
    return filename
    
def doubleFunc():
    '''
    Calls button_profile function to load card info
    Calls imageOpener function to load card image

    Returns
    -------
    imageOpener() and button_profile() 

    '''
    imageOpener()
    button_profile()

        


# Entry fields
### Search by Name
search_playerName = Entry(root, width=35, borderwidth=5)
### Output for Player names ID numbers
output_playerName = Entry(root, width=35, borderwidth=5)

### Search by ID
search_idNum = Entry(root, width=35, borderwidth=5)
### Output for card info by ID numbers
output_idNum = Entry(root, width=35, borderwidth=5)
output_name = Entry(root, width=35, borderwidth=5)
output_year = Entry(root, width=35, borderwidth=5)
output_brand = Entry(root, width=35, borderwidth=5)
output_product = Entry(root, width=35, borderwidth=5)
output_c_num = Entry(root, width=35, borderwidth=5)
# output_img = Entry(root, width=35, borderwidth=5)


# Buttons
search_playerButton = Button(text="Search IDs by Player Name", command=button_search)  
search_idNumButton = Button(text="Search Cards by ID num", command=doubleFunc)
next_idnumButton = Button(text="Next id", width=15, command=nextButton)   
last_idnumButton = Button(text="Last id", width=15, command=lastButton) 

quit_button = Button(text="Exit Program", width=15, command=root.destroy)                

# Labels
name_label = Label(root, text='Name:')
year_label = Label(root, text='Year:')
brand_label = Label(root, text='Brand:')
product_label = Label(root, text='Product:')
c_num_label = Label(root, text='Card Number:')


img_label = Label(root, text="Card Image", font='ComicSans 18 bold') 



# Grid
search_playerName.grid(column=0, row=0, columnspan=2)
search_playerButton.grid(column=2, row=0, sticky='nesw', columnspan=2)     
output_playerName.grid(column=4, row=0)

last_idnumButton.grid(column=0, row=2, padx=0, pady=0, columnspan=1, sticky='nesw')
next_idnumButton.grid(column=1, row=2, padx=0, pady=0, columnspan=1,  sticky='nesw')

quit_button.grid(column=0, row=7)

search_idNum.grid(column=0, row=1, columnspan=2)
search_idNumButton.grid(column=2, row=1, sticky='nesw', columnspan =2)  
output_idNum.grid(column=4, row=1)

### Labels for output card info
name_label.grid(column=3, row=3, sticky="E")
year_label.grid(column=3, row=4, sticky="E")
brand_label.grid(column=3, row=5, sticky="E")
product_label.grid(column=3, row=6, sticky="E")
c_num_label.grid(column=3, row=7, sticky="E")

img_label.grid(column=0, row=8, columnspan=5)




### Sticks outputs Card info 
output_name.grid(column=4, row=3)
output_year.grid(column=4, row=4)
output_brand.grid(column=4, row=5)
output_product.grid(column=4, row=6)
output_c_num.grid(column=4, row=7)
# output_img.grid(column=2, row=1)





root.mainloop()