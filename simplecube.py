#!/usr/bin/env python

"""
Lab: 2-Simple cube
Authors: Claude-André Alves, Luc Wachter
Description: Create a cube using squares, triangles or triangle strips, write the results to disk.
Python version: 3.7.4
"""

import vtk


def cube_from_faces(points, faces, scalars):
    # Create the topology (cells)
    polys = vtk.vtkCellArray()

    for face in faces:
        polys.InsertNextCell(len(face), face)

    # Create a polydata object
    cube = vtk.vtkPolyData()
    # Set the points and polys as the geometry and topology of the polydata
    cube.SetPoints(points)
    cube.SetPolys(polys)

    # Set scalars
    cube.GetPointData().SetScalars(scalars)

    return cube


def cube_from_quads(points, scalars):
    """Get cube polydata from 6 quadrilateral sides"""
    quads = [(3, 2, 1, 0), (4, 5, 6, 7), (0, 1, 5, 4),
             (1, 2, 6, 5), (2, 3, 7, 6), (3, 0, 4, 7)]

    return cube_from_faces(points, quads, scalars)


def cube_from_triangles(points, scalars):
    """Get cube polydata from 12 triangular sides"""
    triangles = [(0, 3, 1), (1, 3, 2), (0, 1, 5), (0, 5, 4),
                 (0, 4, 3), (3, 4, 7), (1, 2, 5), (2, 6, 5),
                 (2, 3, 7), (2, 7, 6), (4, 5, 6), (4, 6, 7)]

    return cube_from_faces(points, triangles, scalars)


def cube_from_strip():
    """Get cube polydata from a triangle strip"""
    pass


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
    # cube = cube_from_quads(points, scalars)
    # write_to_file(cube, "cube_from_quads.vtk")
    cube = cube_from_triangles(points, scalars)
    # write_to_file(cube, "cube_from_triangles.vtk")
    # cube = read_from_file("cube_from_quads.vtk")

    # Visualize
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputData(cube)
    mapper.SetScalarRange(cube.GetScalarRange())

    actor = vtk.vtkActor()
    actor.SetMapper(mapper)

    # Test faces' orientation
    # actor.GetProperty().FrontfaceCullingOn()
    # actor.GetProperty().BackfaceCullingOn()

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


# Main instructions
if __name__ == "__main__":
    main()
