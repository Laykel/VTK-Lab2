# Labo 2 - simple cube

Le but de ce laboratoire est de créer manuellement des vtkPolyData . Pour cela nous allons modifier le code de cone5.py du laboratoire précédent.

- Créer un cube de coté 1 et centré en (0,0,0) en créant explicitement le vtkPoints et le vtkCellArray. Utiliser des cellules quadrilatérales.
- Sauvez le résultat au moyen d'un vtkPolyDataWriter.
- Lisez le fichier sauvé au moyen d'un vtkPolyDataReader
- Idem mais en utilisant des 12 triangles au lieu de 6 carrés.
- Idem mais en utilisant 1 triangle strip
- Ajoutez des valeurs scalaires à chaque sommet et visualiser le résultat. Pensez à spécifier le ScalarRange à votre Mapper.

Dans chacun des cas, vérifiez que vos faces sont bien orientées en la visualisant sans les faces avant ou arrière. Pour cela, il faut appeler la méthode FrontfaceCullingOn() ou BackfaceCullinOn() de la Property de votre Actor. Essayer aussi d'en changer l'opacité.

Rendez un fichier .zip contenant votre code en python et les fichier .vtk de vos données.
