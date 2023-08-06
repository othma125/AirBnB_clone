from models.base_model import BaseModel

from models import storage

if __name__ == "__main__":
    # print storage.__objects
    print("storage.__objects: ", storage.all())

    model = BaseModel()
    model.name: str = "first name"
    model.my_number = 98
    print(model)

    model.save()


# model = BaseModel()
# model.name: str = 'first name'
# model.my_number = 98
# # print(model)
# import time
# time.sleep(2)
# model.save()
# tojson = model.to_dict()
# print(tojson)
# # for key in tojson.keys():
# #     print(f'{key} {type(tojson[key])}')
# model = BaseModel(**tojson)
# print(model.to_dict())
