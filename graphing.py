import os
import json

def cal_oobs(path = ""):
    for root, dirs, files in os.walk(path):
        total_oobs = 0
        if root != path:
            if files.__len__() != 0:
                for i in range(0, files.__len__()):
                    path = os.path.join(root, files[i])
                    with open(path) as json_file:
                        data = json.load(json_file)
                        total_oobs += data["execution"]["oobs"]
                        if i == files.__len__() - 1:
                            f = open(os.path.join(root,"total_oobs.txt"), "w+")
                            f.write("total_oobs = " + str(total_oobs))
                            f.close()
                            total_oobs = 0


if __name__ == "__main__":
    path1 = "C:/Users/apsara.murali-simha/Tests_Final/Novelty/Novelty_pop/"
    path2 = "C:/Users/apsara.murali-simha/Tests_Final/Random_1/"
    cal_oobs(path1)
    cal_oobs(path2)
