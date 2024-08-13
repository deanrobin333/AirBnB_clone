#!/usr/bin/python3
# main_1.py
# for task 4. Create BaseModel from dictionary

from models.base_model import BaseModel

bm1 = BaseModel()
bm2 = BaseModel(**bm1.to_dict())
print(bm1)
print(bm2)
print(bm1.id == bm2.id)
