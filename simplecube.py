#!/usr/bin/env python

"""
Lab: 2-Simple cube
Authors: Claude-André Alves, Luc Wachter
Description: Create a cube using squares, triangles or triangle strips, write the results to disk.
Python version: 3.7.4
"""

import vtk


def cube_from_faces(points, cells, scalars, strip=False):
    """Create cube polydata from the geometry and topology given in parameters"""
    # Create the topology (cells)
    polys = vtk.vtkCellArray()

    for cell in cells:
        polys.InsertNextCell(len(cell), cell)

    # Create a polydata object
    cube = vtk.vtkPolyData()
    # Set the geometry of the polydata
    cube.SetPoints(points)

    # Set the topology of the polydata
    if not strip:
        cube.SetPolys(polys)
    else:
        cube.SetStrips(polys)

    # Set scalars
    cube.GetPointData().SetScalars(scalars)

    return cube


def cube_from_quads(points, scalars):
    """Create cube polydata from 6 quadrilateral sides"""
    # Define cells using points indices
    quads = [(3, 2, 1, 0), (4, 5, 6, 7), (0, 1, 5, 4),
             (1, 2, 6, 5), (2, 3, 7, 6), (3, 0, 4, 7)]

    return cube_from_faces(points, quads, scalars)


def cube_from_triangles(points, scalars):
    """Create cube polydata from 12 triangular sides"""
    # Define cells using points indices
    triangles = [(0, 3, 1), (1, 3, 2), (0, 1, 5), (0, 5, 4),
                 (0, 4, 3), (3, 4, 7), (1, 2, 5), (2, 6, 5),
                 (2, 3, 7), (2, 7, 6), (4, 5, 6), (4, 6, 7)]

    return cube_from_faces(points, triangles, scalars)


def cube_from_strip(points, scalars):
    """Create cube polydata from a triangle strip"""
    # Define strip using a series of points
    # Each series of three points represents a triangle
    # https://stackoverflow.com/questions/28375338/cube-using-single-gl-triangle-strip
    series = [(0, 1, 4, 5, 6, 1, 2, 0, 3, 4, 7, 6, 3, 2)]

    return cube_from_faces(points, series, scalars, strip=True)


def write_to_file(cube, filename):
    """Write polydata geometry, topology and attributes to file"""
    writer = vtk.vtkPolyDataWriter()
    writer.SetInputData(cube)
    writer.SetFileName(filename)
    writer.Write()


def read_from_file(filename):
    """Read polydata geometry, topology and attributes from file"""
    reader = vtk.vtkPolyDataReader()
    reader.SetFileName(filename)
    reader.Update()
    return reader.GetOutput()


# Main instructions
def main():
    colors = vtk.vtkNamedColors()

    # Points for a cube centered on (0, 0, 0)
    pts = [(-0.5, -0.5, -0.5), (0.5, -0.5, -0.5), (0.5, 0.5, -0.5), (-0.5, 0.5, -0.5),
           (-0.5, -0.5, 0.5), (0.5, -0.5, 0.5), (0.5, 0.5, 0.5), (-0.5, 0.5, 0.5)]

    # Create the geometry (coordinates)
    points = vtk.vtkPoints()
    # Store attributes
    scalars = vtk.vtkFloatArray()

    for i, pt in enumerate(pts):
        points.InsertPoint(i, pt)
        scalars.InsertTuple1(i, i)

    # Create cube from cells
    cube = cube_from_quads(points, scalars)
    # write_to_file(cube, "cube_from_quads.vtk")
    # cube = read_from_file("cube_from_quads.vtk")
    # cube = cube_from_triangles(points, scalars)
    # write_to_file(cube, "cube_from_triangles.vtk")
    # cube = read_from_file("cube_from_triangles.vtk")
    # cube = cube_from_strip(points, scalars)
    # write_to_file(cube, "cube_from_strip.vtk")
    # cube = read_from_file("cube_from_strip.vtk")

    # Map data and create actors
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputData(cube)
    mapper.SetScalarRange(cube.GetScalarRange())

    actor = vtk.vtkActor()
    actor.SetMapper(mapper)

    # Test the cells' orientation
    # actor.GetProperty().FrontfaceCullingOn()
    actor.GetProperty().BackfaceCullingOn()

    renderer = vtk.vtkRenderer()
    renderer.AddActor(actor)
    renderer.SetBackground(colors.GetColor3d("Cornsilk"))

    # Window properties
    ren_win = vtk.vtkRenderWindow()
    ren_win.SetWindowName("The good cube")
    ren_win.SetSize(600, 600)
    ren_win.AddRenderer(renderer)

    # Watch for events
    interactor = vtk.vtkRenderWindowInteractor()
    interactor.SetRenderWindow(ren_win)

    # Set the interactor style
    style = vtk.vtkInteractorStyleTrackballCamera()
    interactor.SetInteractorStyle(style)

    # Initialize and start the event loop
    interactor.Initialize()
    interactor.Start()


if __name__ == "__main__":
    main()
