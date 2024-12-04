from Database import Database
from Database import Table
import os

db=Database("firstDb")

db.create_table("Job Search 3")

my_table = db.table

print(my_table.name)
print(my_table.table)