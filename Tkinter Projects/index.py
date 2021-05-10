from tkinter import *
from tkinter import ttk, messagebox
import sqlite3


class Product:



	db_name = "database.db"


	def __init__(self, root):
		self.window = root
		self.window.title("SQL")
		self.window.resizable(0,0)

		#frame
		frame = LabelFrame(self.window, text="New Product", font=("Algerian", 10,"bold"),bg="blue").grid(row=0, column=0, columnspan=2, pady=15)
		#Nombre
		Label(frame, text="Nombre--> ", font=("Algerian", 12, "bold"), fg="blue").grid(row=1, column=1, padx=10)
		self.name = Entry(frame)
		self.name.grid(row=1, column=2, padx=20) 
		#Precio
		Label(frame, text="Precio--> ", font=("Algerian", 12, "bold"), fg="blue" ).grid(row=2, column=1, padx=10)
		self.price = Entry(frame)
		self.price.grid(row=2, column=2, pady=10)
		#button
		Button(frame, text="Save Product" , font=("Algerian", 12, "bold"), fg="blue", command= lambda: self.add()).grid(row=3, column=1, columnspan=2, sticky="W E")
		#tree
		self.tree = ttk.Treeview(height=10, column=2)
		self.tree.grid(row=4, column=1, columnspan=2, sticky="W E", pady=15)
		self.tree.heading("#0", text="Nombre")
		self.tree.heading("#1", text="Precio")
		#button
		Button(frame, text="Eliminar" , font=("Algerian", 12, "bold"), fg="blue", width=15, command= lambda: self.delete()).grid(row=5, column=1, sticky="W E")
		Button(frame, text="Editar" , font=("Algerian", 12, "bold"), fg="blue", width=10, command= lambda: self.edit_frame()).grid(row=5, column=2, sticky="W E")

		self.get_products()
				#Conectar sqlite	
	def run_query(self, query, parameters = ()):
		with sqlite3.connect(self.db_name) as db:
			cursor = db.cursor()
			result = cursor.execute(query, parameters)
			db.commit()
			return result
	#imprimir productos en tabla
	def get_products(self):
		records = self.tree.get_children()
		for element in records:
			self.tree.delete(element)
		query = "SELECT * FROM product ORDER BY name DESC"
		db_rows = self.run_query(query)
		for row in db_rows:
			self.tree.insert("",0, text= row[1], values= row[2])

	def delete(self):
		item = self.tree.item(self.tree.selection())["text"]
		item2 = self.tree.item(self.tree.selection())
		print(item2)
		query = "DELETE FROM product WHERE name = ?"
		self.run_query(query,(item,))
		self.get_products()

	def add(self):
		if self.validate():
			query = "INSERT INTO product VALUES(NULL,?,?)"
			parameters = (self.name.get(), self.price.get())
			self.run_query(query, parameters)
			self.get_products()
			self.name.delete(0,END)
			self.price.delete(0,END)
		else:
			messagebox.showinfo(message="Invalid Characters", title="Invalid")

	def edit_frame(self):
		
		if self.tree.selection():
			self.new_root = Toplevel()
			

			LabelFrame(self.new_root, text="New Frame").grid(row=0, column=0, pady=10)
			#old and new name
			old_name = self.tree.item(self.tree.selection())["text"]
			Label(self.new_root, text="old name--> ").grid(row=1, column=1, padx=10, pady=5)
			Label(self.new_root, text=old_name).grid(row=1, column=2, pady=5)
			Label(self.new_root, text="New name--> ").grid(row=2, column=1, padx=10, pady=5)
			self.new_root_name = Entry(self.new_root)
			self.new_root_name.grid(row=2, column=2, padx=10)
			#old and new price
			old_price = self.tree.item(self.tree.selection())["values"]
			Label(self.new_root, text="old price--> ").grid(row=3, column=1, padx=10, pady=5)
			Label(self.new_root, text=old_price).grid(row=3, column=2, pady=5, padx=10)
			Label(self.new_root, text="New price--> ").grid(row=4, column=1, pady=10, padx=10)
			self.new_root_price = Entry(self.new_root)
			self.new_root_price.grid(row=4, column=2, padx=10, pady=10)
		else:
			messagebox.showinfo(message="Select data")

		Button(self.new_root, text="Editar", command= lambda:self.edit()).grid(row=5, column=1, columnspan=2, sticky="W E")
	def edit(self):
		if len(self.new_root_name.get()) != 0 and  len(self.new_root_price.get()) != 0 :
			self.delete()
			new_price = self.new_root_price.get()
			new_name = self.new_root_name.get()
			parameters = (new_name, new_price)

			query= "INSERT INTO product VALUES(NULL,?,?)"

			self.run_query(query,(new_name,new_price))

			self.get_products()
			self.new_root.destroy()
		else:
			messagebox.showinfo(message="Invalid Characters", title="Invalid")

	def validate(self):
		return len(self.name.get()) != 0 and len(self.price.get()) != 0




if __name__ == '__main__':
    root = Tk()
    application = Product(root)
    root.mainloop()
