import numpy as np
from copy import deepcopy
from math import sqrt


class Segmentation:

    def __init__(self):
        self.data = [["Consummate customers", 652, 718, 43, 87, 1.95, 52, 55],
                ["Risky Revenue", 643, 570, 34,	55,	2.11, 45, 49],
                ["Business Builders", 49, 739, 48, 78, 1.97, 52, 50],
                ["Balance Bombs", 59, 570, 32, 40, 2.13, 41, 46]]
        self.transpose_data = np.transpose(self.data)
        self.data_norm = self.normalization()

    def normalization(self):
        data = deepcopy(self.data)
        minmax = [(0, 0)]
        # finding min and max for each component
        for i in range(1, 8):
            minmax.append((float(min(self.transpose_data[i])), float(max(self.transpose_data[i]))))

        for j in range(len(data)):
            for i in range(1, 8):
                data[j][i] = (data[j][i] - minmax[i][0])/(minmax[i][1] - minmax[i][0])

        return data

    def euclid_distances_all(self):
        distances = dict()
        for i in range(len(self.data)):
            for j in range(i + 1, len(self.data)):
                euclid = 0
                for k in range(1, 8):
                    euclid += (self.data_norm[i][k] - self.data_norm[j][k]) ** 2
                distances[(i, j)] = sqrt(euclid)
        return distances

    def add_data(self, row):
        if len(row) != 8:
            raise SyntaxError
        index = len(self.data)
        self.data.append(row)
        self.transpose_data = np.transpose(self.data)
        self.data_norm = self.normalization()

        distance = float('inf')
        similar = None
        for i in range(len(self.data) - 1):
            euclid = 0
            for k in range(1, 8):
                euclid += (self.data_norm[i][k] - self.data_norm[index][k]) ** 2
            euclid = sqrt(euclid)
            if distance > euclid:
                distance = euclid
                similar = self.data_norm[i][0]
        return similar


if __name__ == '__main__':
    s = Segmentation()
    print(s.add_data(["s", 644, 560, 33, 55, 2.12, 40, 40]))
    print(s.data_norm)
