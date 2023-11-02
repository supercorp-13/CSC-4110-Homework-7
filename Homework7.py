#Revision 1 November 1, 2023
## Begin Nadinne Motta
#Homework 7

import tkinter as tk
from tkinter import filedialog, messagebox
import csv
import json

#main function to change the data by ordering by row, and changing from csv to a json format
def change_csv_to_json():
    #empty sales_data list
    sales_data = []

    #opens up file, and converts data to JSON format
    #all fields from document are listed
    try:
        with open('Homework7\SalesJan2009.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            for row in csv_reader:
                transaction_date, product, price, payment_type, name, city, state, country = [data.strip('\'"') for data in row]
                
                #each line processed and dictionary created of each
                sale = {
                    'Transaction_date': transaction_date,
                    'Product': product,
                    'Price': price,
                    'Payment_Type': payment_type,
                    'Name': name,
                    'City': city,
                    'State': state,
                    'Country': country
                }

                #appended to sales_data 
                sales_data.append(sale)
        
        #save to transaction_data.json
        with open('transaction_data.json', 'w') as json_file:
            json.dump(sales_data, json_file, indent=4)

    #message boxes used twice , once for the successful conversion, and one for a file not found error
        messagebox.showinfo("Success", "The data conversion from csv to JSON worked!")
    except FileNotFoundError:
        messagebox.showerror("Error", "SalesJan2009.csv was not found")

#using .quit()
def quit_application():
    root.quit()


#UI showing the WSU colors
root = tk.Tk()
root.title("Data Conversion for 2009 Sales")
root.geometry("800x400")
root.configure(bg = 'blue')

label = tk.Label(root, text = "Convert CSV file to JSON", font = ("Times New Roman", 16), bg = 'blue', fg = 'white')
label.pack(pady = 20)

#process button
process_button = tk.Button(root, text="Process CSV file to JSON", command = change_csv_to_json)
process_button.pack()

#quit button
quit_button = tk.Button(root, text="Quit", command = quit_application)
quit_button.pack()

root.mainloop()

#Revision 1 October 28, 2023
## END Nadinne Motta
#Homework 7