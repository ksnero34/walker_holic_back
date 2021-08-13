'''
Application Model
'''

# from model import mysql
from config import config

def get_cursor():
    print(config.SLOW_API_TIME)


# def init_app():
#     '''Model Init Function'''

#     # Mysql Init
#     initializer = mysql.ModelInitializer()
#     initializer.init_model()

get_cursor()