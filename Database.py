import os

class Table:
    class_variable = {}
    def __init__(self,name):
        self.name = name
        class_variable = {'name' : self.name}
        self.table = class_variable
        

class Database:
    def __init__(self, name):
        self.folder='Databases'
        os.makedirs(self.folder, exist_ok=True)

        self.file_path = os.path.join(self.folder, f"Database_{name}.txt")

        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w') as db_file:
                db_file.write(f"{name} db initialized")  # Create an empty file
        
    
        print(f"Database '{name}' initialized at '{self.file_path}'")
    def create_table(self, table_name):
        self.table = Table(table_name)
        with open(self.file_path, 'a') as db_file:
            db_file.write("\n " + str(self.table.table))

