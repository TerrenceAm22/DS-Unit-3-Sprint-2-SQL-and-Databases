import sqlite3

conn = sqlite3.connect('northwind_small.sqlite3')


def ten_most_expensive_items():
    #### Function to Return Ten most Expensive Items
    ten_items = """ SELECT prod.ProductName, prod.UnitPrice
    FROM Product as prod
    ORDER BY prod.UnitPrice DESC
    LIMIT 10;"""
    curs = conn
    ten_items = curs.execute(ten_items).fetchall()
    print("Top Ten Items", ten_items)

def average_age_of_employee():
    ### Function to return average age of employees by the time
    ### they are hired
    avg_age = """ SELECT AVG(HireDate - BirthDate) as avg_age
    FROM EMPLOYEE;"""
    curs = conn
    avg_age = curs.execute(avg_age).fetchall()
    print("Avergae Age of Employee when hired", avg_age)

def suppliers():
    ### Function to return top ten expensive items
    ### and their suppliers
    ten_suppliers = """SELECT prod.ProductName, prod.UnitPrice, sup.CompanyName
    FROM Product AS prod
    JOIn Supplier AS sup ON sup.ID = prod.SupplierID
    ORDER BY prod.UnitPrice DESC
    LIMIT 10;"""
    curs = conn
    ten_suppliers = curs.execute(ten_suppliers).fetchall()
    print("Top Ten Expensive Items and their Suppliers,", ten_suppliers)

def largest_category():
    ### Function to return largest category by number
    ### of Products
    num_products = """ SELECT cat.CategoryName, COUNT(prod.CategoryID)
    FROM Product AS prod
    INNER JOIN Category AS cat
    ON prod.CategoryID = cat.ID
    GROUP BY prod.CategoryID
    ORDER BY COUNT(prod.CategoryID) DESC
    LIMIT 1;"""
    curs = conn
    num_products = curs.execute(num_products).fetchall()
    print("Largest Category by Number of Products", num_products)


#ten_most_expensive_items()
#average_age_of_employee()
#suppliers()
#largest_category()