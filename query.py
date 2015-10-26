"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Start here.

# Part 2: Write queries

# Get the brand with the **id** of 8.
## SELECT * FROM Brands WHERE id = 8;
# id_is_8 = Brand.query.filter(Brand.id == 8).all()

# # Get all models with the **name** Corvette and the **brand_name** Chevrolet.
# ## SELECT * FROM Models WHERE name = "Corvette" AND brand_name = "Chevrolet";
# corvettes = Model.query.filter(Model.brand_name == 'Chevrolet', Model.name == 'Corvette').all()


# # Get all models that are older than 1960.
# ## SELECT * FROM Models WHERE (Models.year < 1960);
# oldies = Model.query.filter(Model.year < 1960).all()    #18 models

# # Get all brands that were founded after 1920.
# ## SELECT * FROM Brands WHERE founded > 1920;
# laters = Brand.query.filter(Brand.founded > 1920).all()     #5 brands

# # Get all models with names that begin with "Cor".
# ## SELECT * FROM Models WHERE Name LIKE 'Cor%';
# cors = Model.query.filter(Model.name.like('Cor%')).all()    #14 models

# # Get all brands with that were founded in 1903 and that are not yet discontinued.
# ## SELECT * FROM Brands WHERE founded == 1903 AND discontinued is null;
# live_since_1903 = Brand.query.filter(Brand.founded == 1903, Brand.discontinued == None).all()   #2 brands

# # Get all brands that are either discontinued or founded before 1950.
# ## SELECT * FROM Brands WHERE founded < 1950 OR discontinued is not null;
# earlies = Brand.query.filter((Brand.founded < 1950) | (Brand.discontinued != None)).all()    #14 brands

# # Get any model whose brand_name is not Chevrolet.
# ##SELECT * FROM Models LEFT JOIN Brands ON (Models.brand_name = Brands.name) WHERE Models.brand_name != 'Chevrolet';    #34 models
# not_chevies = Model.query.filter(Model.brand_name != 'Chevrolet').all()


# Fill in the following functions. (See directions for more info.)


def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    model_list = \
        db.session.query(Model.name, Model.brand_name, Brand.headquarters).\
        filter(Model.brand_name == Brand.name).\
        filter(Model.year == year).all()

    for i in model_list:                        
        print "Car: " + i.brand_name, i.name + "    Headquartered in: " + i.headquarters  
    ###ROO: Why aren't these objects printing with my repr formatting (if i just print i at the top of the loop?)


def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    makes = db.session.query(Model.name, Model.brand_name).all()
    for i in makes:
        print i.name + " " + i.brand_name


# -------------------------------------------------------------------


# Part 2.5: Advanced and Optional
def search_brands_by_name(mystr):
    """ Returns a list of objects from the Brands table which names equal or 
    contain the input string mystr. 

    Analagous SQL query:  
        SELECT * FROM Brands 
            WHERE Brands.name Brands.name == "mystr" OR LIKE ('%mystr%'); 
    """

    mystr = '%'+mystr+'%'                               #format for LIKE syntax
    mystr_list = (
        Brand.query.filter((Brand.name == mystr) | 
            (Brand.name.like(mystr))).all()
        )
    return mystr_list


def get_models_between(start_year, end_year):
    """ Returns a list of objects from the Models table which were made between
    the start_year and end_year, exclusive of both bounds.

    Analagous SQL query:
        Select * FROM Models
            WHERE Models.year > start_year AND Models.year < end_year;

    """
    tweens = Model.query.filter((Model.year > start_year) & (Model.year < end_year)).all()
    print tweens

    #Can't figure out how to use between :(


# -------------------------------------------------------------------

# Part 3: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?
###I don't know how to answer this.  It looks to be an object of the class 'flas_sqlalchemy.BaseQuery'
### and it doesn't have any of the properties of an object created from the class Brand (you can't check it's ID with dot notation)
### It should sort of point to the same object that means "the row in the Brands table that holds information about Ford" but it doesn't



# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?
###Association tables exist to manage an otherwise many-to-many relationship
###between two concepts in a database.  When you are unable to join two tables on
###a primary/foreign key relationship, that might be a good indicator to make an
###association table.  They are used to create two one-to-many relationships.
###These allow the user to get at single instances of each concept on either
###side of the table.
###Sometimes they only contain two columns/fields, one for the primary key of each table



