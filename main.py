# This is a sample Python script.
import numpy as np
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import open3d as o3d


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    bunny = o3d.data.BunnyMesh()
    mesh = o3d.io.read_triangle_mesh(bunny.path)

    mesh.compute_vertex_normals()

    pcd = mesh.sample_points_poisson_disk(5000)

    # o3d.visualization.draw_geometries([mesh, pcd])
    o3d.visualization.draw([mesh, pcd])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
