import json
import cv2
import os
from cv2 import calcHist
from cv2 import solve

from sqlalchemy import false

def judge(img1, img2):
    p1 = cv2.imread(os.path.dirname(__file__)[0:-4] + 'static\\save\\' + str(img1) + '.png')
    p2 = cv2.imread(os.path.dirname(__file__)[0:-4] + 'static\\save\\' + str(img2) + '.png')
    h1 = cv2.calcHist([p1], [2], None, [256], [0,256])
    h2 = cv2.calcHist([p2], [2], None, [256], [0,256])
    return cv2.compareHist(h1, h2, method=cv2.HISTCMP_CORREL)
class Pictures:
    pics = {}
    def __init__(self):
        with open('pictures.db', 'r', encoding='utf-8') as file:
            self.pics = json.load(file)

    def getOwner(self, id):
        return self.pics['pic'][id-1]['owner']

    def getOwnPictureNum(self, user):
        return len(self.pics['user'][user - 100])

    def getOwnPicture(self, user):
        return self.pics['user'][user - 100]

    def getStarPictureNum(self, user):
        return len(self.pics['stared'][user - 100])

    def getStarPicture(self, user):
        return self.pics['stared'][user - 100]

    def save(self):
        with open('pictures.db', 'w', encoding='utf-8') as file:
            json.dump(self.pics, file, ensure_ascii=False)

    def getCnt(self):
        return self.pics['count']

    def getPictureById(self, id):
        return self.pics['pic'][id - 1]

    def addStar(self, id, starer):
        self.pics['pic'][id - 1]['star'] += 1
        self.pics['pic'][id - 1]['starer'].append(starer)
        self.pics['stared'][starer - 100].append(id)
        self.save()

    def delStar(self, id, starer):
        self.pics['pic'][id - 1]['starer'].remove(starer)
        self.pics['pic'][id - 1]['star'] -= 1
        self.pics['stared'][starer - 100].remove(id)
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
        self.pics['user'][owner - 100].append(id)
        self.pics['pic'].append(inform)
        self.save()
        return id

    def calcSimilar(self, id):
        ans = []
        for i in range(0, self.pics['count']):
            if i != id - 1 and judge(id, i + 1) > 0.1:
                ans.append(i + 1)
        return ans

    def isStared(self, user, picid):
        return user in self.pics['pic'][picid - 1]['starer']

    def isOwner(self, user, picid):
        return picid in self.pics['user'][user-100]

picData = Pictures()