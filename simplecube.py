#!/usr/bin/env python

"""
Lab: 2-Simple cube
Authors: Claude-André Alves, Luc Wachter
Description: Create a cube using squares, triangles or triangle strips, write the results to disk.
Python version: 3.7.4
"""

# vtkCellArray using quadrilateral cells
# vtkPolyDataWriter
# vtkPolyDataReader
# Same but with 12 triangles instead of 6 squares
# Same but with a triangle strip
# Add scalar values to each vertex

import vtk


def cube_from_quads(pts, quads):
    # Create the geometry (coordinates)
    points = vtk.vtkPoints()
    # Store attributes
    scalars = vtk.vtkFloatArray()

    for i, pt in enumerate(pts):
        points.InsertPoint(i, pt)
        scalars.InsertTuple1(i, i)

    # Create the topology (cells)
    polys = vtk.vtkCellArray()

    for quad in quads:
        polys.InsertNextCell(4, quad)

    # Create a polydata object
    cube = vtk.vtkPolyData()
    # Set the points and polys as the geometry and topology of the polydata
    cube.SetPoints(points)
    cube.SetPolys(polys)

    # Set scalars
    cube.GetPointData().SetScalars(scalars)

    return cube


def cube_from_triangles():
    pass


def cube_from_strip():
    pass


def main():
    colors = vtk.vtkNamedColors()

    # Points for a cube centered on (0, 0, 0)
    pts = [(-0.5, -0.5, -0.5), (0.5, -0.5, -0.5), (0.5, -0.5, 0.5), (-0.5, -0.5, 0.5),
           (-0.5, 0.5, 0.5), (0.5, 0.5, 0.5), (0.5, 0.5, -0.5), (-0.5, 0.5, -0.5)]
    quads = [(0, 1, 2, 3), (0, 3, 4, 7), (0, 1, 6, 7),
             (1, 2, 5, 6), (2, 3, 4, 5), (4, 5, 6, 7)]

    cube = cube_from_quads(pts, quads)

    # Visualize
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputData(cube)
    mapper.SetScalarRange(cube.GetScalarRange())

    actor = vtk.vtkActor()
    actor.SetMapper(mapper)

    renderer = vtk.vtkRenderer()
    renderer.AddActor(actor)
    # renderer.SetBackground(colors.GetColor3d("DarkGreen"))
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
