# Listas e Data Trees


1. Manipulação de listas e slicing

    [Arquivo base da Aula](./AULA_12_base.gh)

    [Arquivo final da Aula](./AULA_12_final.gh)


2. Data trees

    [Artigo Mcnell data trees](https://developer.rhino3d.com/guides/rhinopython/grasshopper-datatrees-and-python/)

    [exemplos de data tree R8 - py3](./datatree_examples_py3.gh)

    -----------------

    ```Python

    import ghpythonlib.treehelpers as th
    import Rhino

    layerTree = []

    for i in range(len(layernames)):
        objs = Rhino.RhinoDoc.ActiveDoc.Objects.FindByLayer(layernames[i])

        if objs:
            geoms = [obj.Geometry for obj in objs]
            layerTree.append(geoms)


    layerTreeA = th.list_to_tree(layerTree, source=[0, 0])
    a = layerTreeA


    layerTreeB = th.list_to_tree(layerTree, source=[1])
    b = layerTreeB

    ```

--------------------

3. Referências e *links* úteis