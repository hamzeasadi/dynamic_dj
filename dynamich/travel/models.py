from django.db import models

# Create your models here.

class Destinations(object):
    """docstring for ."""

    def __init__(self, image, name, price, desc):
        # super(self).__init__()
        self.img = image
        self.name = name
        self.price = price
        self.desc = desc

# class Destinations(object):
#     """docstring for ."""
#     name: str
#     iamge: str
#     desc: str
#     price: int

# class Destinations(object):
#     """docstring for ."""
#
#     # def __init__(self):
#         # super(, self).__init__()
#         # self.arg = arg
#     def __call__(self, name, price, description, image):
#         self.name = name
#         self.img = image
#         self.desc = description
#         self.price = price
