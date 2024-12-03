import pygame as pg
import dq_object as obj


class inventory:
    item_list = []

    def __init__(self, size):
        self.size = size

    def pop_item(item_name):
        for index, item in item_list:
            if item.name == item_name:
                return item_list.pop(index)

    def read_item(item_name):
        for item in item_list:
            if item.name == item_name:
                return item

    def add_item(item):
        if item is obj and len(item_list) < size:
            item_list.append(item)

    def check_item(item_name):
        for item in item_list:
            if item.name == item_name:
                return True
        return False

    def remove_item(item_name):
        for index, item in item_list:
            if item.name == item_name:
                del item_list[index]

    def get_item_list():
        return item_list
