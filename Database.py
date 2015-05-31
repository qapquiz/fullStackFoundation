from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker (bind = engine)
session = DBSession()

class Database:
    def add_restaurant(self, name = None):
        restaurant = Restaurant(name = name)
	session.add(restaurant)
        return restaurant

    def get_restaurants(self):
        return session.query(Restaurant).all()

    def add_menu_item(self, name = None, description = None, course = None, price = None, restaurant = None):
        menuItem = MenuItem(name = name, description = description, course = course, restaurant = restaurant)
        session.add(menuItem)
        return menuItem
    
    def query(self, tableClass):
        return session.query(tableClass).first() 

    def commit(self):
        session.commit()
