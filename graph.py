import numpy as np


class Mesh2D:

    def __init__(self, file_name: str):
        file = open(file_name, 'r')
        vertices = []
        triangles = []
        while line := file.readline():
            if "#" in line:
                continue
            if "v" in line:
                _, x, y, _ = line.split()
                x, y = float(x), float(y)
                vertices.append([x, y])
            if "f" in line:
                triangles.append([int(i) - 1 for i in line.replace("f", '').split()])
        self.vertices = np.array(vertices, np.double)
        self.triangles = np.array(triangles, np.int8)

    @property
    def triangle_centers(self):
        return np.mean(self.vertices[self.triangles], axis=1)

    @property
    def triangle_components(self):
        return self.vertices[self.triangles]
