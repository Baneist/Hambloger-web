import json

class Pictures:
    pics = {}
    def __init__(self):
        with open('pictures.db', 'r') as file:
            self.pics = json.load(file)

    def save(self):
        with open('pictures.db', 'w') as file:
            json.dump(self.pics, file)

    def getCnt(self):
        return self.pics['count']

    def getPictureById(self, id):
        return self.pics['pic'][id - 1]

    def addStar(self, id, starer):
        stid = self.pics['pic'][id - 1]['star']
        self.pics['pic'][id - 1]['star'] += 1
        self.pics['pic'][id - 1]['starer'][stid] = starer
        self.save()

    def setDescribe(self, id, str):
        self.pics['pic'][id - 1]['describe'] = str
        self.save()

    def addPicture(self, owner):
        self.pics['count'] += 1
        id = self.pics['count']
        inform = {
            "owner": owner,
            "star": 0,
            "describe": "测试",
            "starer": []
        }
        while(self.pics['user'].size() <= owner - 100):
            self.pics['user'].append([])
        self.pics['user'][owner - 100].append(id)
        self.pics['pic'].append(inform)
        self.save()
        return id

picData = Pictures()