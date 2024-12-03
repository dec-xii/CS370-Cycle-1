import pygame as pg 
import dq_object as obj
from dq_object import dq_item

class inventory:
    def __init__(self, size):
        self.size=size
        self.item_list=[]

    def pop_item(self, item_name):
        for index,item in self.item_list:
            if item.name==item_name:
                return self.item_list.pop(index)
            
    def read_item(self, item_name):
        for item in self.item_list:
            if item.name==item_name:
                return item
            
    def add_item(self, item):
        myObj = item.myObject
        if len(self.item_list) < self.size:
            self.item_list.append(myObj)
            print("adding item ", myObj.name)

    def check_item(self, item_name):
        for item in self.item_list:
            if item.name==item_name:
                return True
        return False
    
    def remove_item(self, item_name):
        for index,item in self.item_list:
            if item.name==item_name:
                del self.item_list[index]

    def get_item_list(self):
        return self.item_list