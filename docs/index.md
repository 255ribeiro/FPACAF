# Fundamentos de Programação Aplicada à Criação e Análise da Forma

___


<!-- Prof. Fernando Ferraz Ribeiro \| fernando.ribeiro@ufba.br

___

[Informações](./Ficha_de_inscricao/informacoes.md)

___

Forum de comunicação do curso (Moodle UFBA):

[https://www.moodle.ufba.br/course/view.php?id=6705](https://www.moodle.ufba.br/course/view.php?id=6705) -->

___

## Plano de Curso

___
___

### Aula 01 -

[SLIDES](./topics/01_Intro_fpacaf/Aula_01-introducao_a_programacao.pdf)

1. Apresentação do curso

    * Metodologia
    * Avaliações

2. Introdução

   * Conceito de algoritmo
   * História da Programação
   * Programação Aplicada à Arquitetura e Urbanismo
   * A linguagem Python

3. [Fluxogramas](./topics/01A_fluxogramas/fluxogramas.md)

4. Instalação

    - CPython 3.X
        * Pastas importantes da distribuição CPython
          - Instalado para um único usuário (instalação mais comum)
            ```
            %USERPROFILE%/AppData/Local/Programs/Python/Python39
            %USERPROFILE%/AppData/Local/Programs/Python/Python39/Scripts
            %USERPROFILE%/AppData/Local/Programs/Python/Python39/Lib/site-packages
            ```
          - Instalado para todos os usuários do computador(instalação alternativa)
            ```
            %PROGRAMFILES%/AppData/Local/Programs/Python/Python39
            %PROGRAMFILES%/AppData/Local/Programs/Python/Python39/Scripts
            %PROGRAMFILES%/AppData/Local/Programs/Python/Python39/Lib/site-packages
            ```
    - Anaconda 3
        * Pastas importantes da distribuição Anaconda no Windows
          - Instalado para um único usuário (instalação mais comum)
            ```
            %USERPROFILE%/Anaconda3
            %USERPROFILE%/Anaconda3/Scripts
            %USERPROFILE%/Anaconda3/Lib/site-packages
            ```
          - Instalado para todos os usuários do computador (instalação alternativa)
            ```
            %PROGRAMFILES%/Anaconda3
            %PROGRAMFILES%/Anaconda3/Scripts
            %PROGRAMFILES%/Anaconda3/Lib/site-packages
            ```
    - Como encontrar o interpretador Python da sua distribuição
       - No console Python (Python shell) digite:
        ```
        import sys
        sys.exec_prefix
        ```

5. Operações matemáticas no Python Shell

   * Operadores matemáticos

   * Divisão inteira e divisão real

      * Mod e Div

   * Níveis de Parênteses

6. Exercício sugerido 01 - Use o Python Shell como uma calculadora

7. Referências e *links* úteis

   * Python

      [Python Foundaition](https://www.python.org/)

      [Python Brasil](http://python.org.br/)

   * Rhinoceros

      [Rhino3D.com](http://www.rhino3d.com/)

      [food 4 Rhino](http://www.food4rhino.com/)
      
   * Grasshopper

      [Grasshopper 3d](http://www.grasshopper3d.com/)

   * Between the Folds

      [Between the Folds](https://www.betweenthefolds.com/)

___

### Aula 02 -

[notas de aula - Python 2](https://colab.research.google.com/github/255ribeiro/LPACAF/blob/master/Aula_02/LPACAF-Aula_02_py2.ipynb)

[notas de aula - Python 3](https://colab.research.google.com/github/255ribeiro/LPACAF/blob/master/Aula_02/LPACAF-Aula_02_py3.ipynb)

1. Variáveis
    * Tipos de variáveis
        * Lógicas
        * Inteiras
        * Reais (ponto flutuante)
        * *Strings*

1. Editor de arquivos

   * abrir editor
   * salvar arquivo
   * editar
   * executar

1. Entradas e saídas
    * input() - Python 2 e 3
    * raw_input() - Python 2
    * print() - Python 3
    * print - Python 2

1. Condicionais lógicas

   * if
   * else
   * elif

1. Exercício 02 - inverter os algarismos de um número inteiro de 3 dígitos usando Mod e/ou Div

1. Arquivos dos Exemplos da Aula

    [Calcúlo do número de espelhos de uma escada](./topics/02_intro_python/escadas.md)
2. Referências e *links* úteis

    *[Tweet sobre Python The Economist](https://twitter.com/theeconomist/status/1020001623236665346?lang=pt)

    *[materia sobre Python The Economist](https://www.economist.com/science-and-technology/2018/07/19/python-has-brought-computer-programming-to-a-vast-new-audience?fsrc=scn/tw/te/bl/ed/pythonhasbroughtcomputerprogrammingtoavastnewaudienceprogramminglanguages)

Cursos de Python:

* Em português:

    - [Tutoriais para iniciantes sugeridos pela comunidade Python Brasil](http://python.org.br/introducao)

    - [curso em vídeo - python 3 em portugues](https://www.cursoemvideo.com/course/python-3-mundo-1/)

    - [Visualização de dados com Python](https://www.youtube.com/watch?v=avSiigCExoY&list=PLpVCamz0zLr9D4SQMLMVbVPAhz2BpLbp8)
  
    - [Introdução ao Python por Projetos](https://www.youtube.com/watch?v=gDDGq7Q_YFE&list=PL5TJqBvpXQv6AEfVymby32MinHdxZA-8J)

    - [Python na Prática](https://www.youtube.com/watch?v=qx2LGtKzjxk&list=PL5TJqBvpXQv6pHlMrbC-NfgeGE2CGrd1S)

    - [Python no vscode - configuração](https://www.youtube.com/watch?v=Z12w7PZWc2E)

* Em Inglês:

    - [Curso de Python no Grasshopper](https://www.youtube.com/watch?v=J84DC-cMS6A&list=PLGV167zE8gnVhurBT46afZ1RlK9RzAsLx)

    - [Introdução - Python Grasshopper](https://www.youtube.com/watch?v=AQP0FVyQ7rc)

    - [Curso de Python no Blender](https://www.youtube.com/watch?v=cyt0O7saU4Q&list=PLFtLHTf5bnym_wk4DcYIMq1DkjqB7kDb-)

___

### Aula 03 -

[notas de aula](./topics/03_intro_python/LPACAF-Aula_03.ipynb)

1. Palavras reservadas

   * [Lista de palavras reservadas do Python 2.7x](https://docs.python.org/2/reference/lexical_analysis.html#keywords)

   * [Lista de palavras reservadas do Python 3.x](https://docs.python.org/3/reference/lexical_analysis.html#keywords)

2. Funções e Métodos

   * [Funções *Built-in* Python 2](https://docs.python.org/2/library/functions.html#)

   * [Funções *Built-in* Python 3](https://docs.python.org/3.7/library/functions.html#built-in-functions)

3. Bibliotecas

   * Importando módulos
       * [Biblioteca keyword Python 2](https://docs.python.org/2/library/keyword.html)
       * [Biblioteca keyword Python 3](https://docs.python.org/3.7/library/keyword.html)

       * [Biblioteca Math Python 2](https://docs.python.org/2/library/math.html)
       * [Biblioteca Math Python 3](https://docs.python.org/3.7/library/math.html)
            * math.sin()
            * math.sqrt()

       * [Biblioteca datetime Python 2](https://docs.python.org/2/library/datetime.html)

       * [Biblioteca datetime Python 3](https://docs.python.org/3.7/library/datetime.html)
            * datetime.date()
            * datetime.timedelta()

   * 4 formas de importação

      * import *nome_do_módulo*
      * import *nome_do_módulo* as *chamada_do_módulo*
      * from *nome_do_módulo* import *função_ou_classe_do_módulo*
      * from *nome_do_módulo* import *função_ou_classe_do_módulo* as *chamada_da_classe_ou_função_do_módulo*
   * Instalando bibliotecas adicionais
    ```shell
        pip install matplotlib
    ```

    * [tutorial sobre o pip](https://www.w3schools.com/python/python_pip.asp)
    * [tutorial sobre o numpy](https://www.w3schools.com/python/numpy_intro.asp)
    * [tutorial sobre o matplotlib](https://www.tutorialspoint.com/matplotlib/index.htm)

4. Funções definidas pelo usuário

   * def
   * parâmetros de entrada
   * retorno

5. Exercício 03 - [Bhaskara](./topics/03_intro_python/if_else.md)

6. Referências e *links* úteis

   * IDE [Pycharm](https://www.jetbrains.com/pycharm/download/#section=windows)

   * Distribuição [Anaconda](https://www.anaconda.com/download/)

   * Ambiente de desenvolvimento Python Online [IBM Developer Skills Network - Labs](https://labs.cognitiveclass.ai/)

   * Ambiente de desenvolvimento Python Online [Google colab](https://colab.research.google.com)

   * O software [Processing](https://processing.org/download/) possui um modo de programação em Python

___

### Aula 04 -

[Arquivo da Aula](./topics/04_intro_loops/AULA_04.gh)  Clique com o botão direito para baixar

1. iteráveis

    * [listas Python 2](https://docs.python.org/2/tutorial/datastructures.html#)
    * [listas Python 3](https://docs.python.org/3.7/tutorial/datastructures.html#)
      * fila
      * pilha
      * lista
      * operações em listas
         * função range()
         * função len()
         * função list()

    * tuples

    * strings

2. Repetições

   * while

   * for

3. Exercício 04 - Sequência de Fibonacci

4. Arquivos dos Exemplos da Aula

    [Arquivo .gh da Aula - Final](./topics/04_intro_loops/AULA_04_FINAL.gh)

    [Exemplos Loops While e For](topics/04_intro_loops/exemplos_for_e_while.py)

    [Exemplo Loop For](./topics/04_intro_loops/exemploFor.py)

5. Referências e *links* úteis

___

### Aula 05 -

1. Alguns comandos do Rhinoceros

    * Curvas
        * Point
        * Line
        * Circle
        * Arc
        * Polyline
        * Curve
        * InterpCrv

    * Superfícies
        * PlanarSrf
        * ExtrudeCrv
        * ExtrudeSrf
        * Pipe
        * Loft

    * Sólidos
        * Cap
        * Box
        * Sphere
        * BooleanUnion
        * BooleanDifference
        * BooleanIntersection

1. Editor de Python do Rhinoceros

    * Abrindo o Editor
    * importando Bibliotecas
    * Criando geometria (rs.Add...)
    * Utilizando variáveis
    * Entrada de dados (rs.Get...)
    * Loops
    * Armazenando Geometria em listas.

1. Exercício 05 - Inverter os algarismos de um número inteiro de qualquer tamanho usando listas.

1. Arquivos dos Exemplos da Aula
    * [Pilar Tubular - Extrude](./topics/05_intro_rhino_py/exemplo_rhino_pilar_tubular_extrude.py)
    * [Pilar Tubular - Pipe](./topics/05_intro_rhino_py/exemplo_rhino_pilar_tubular_pipe.py)

2. Referências e *links* úteis

    * [Tutorial Rhino Modelagem 3D](https://www.youtube.com/watch?v=NKkXMKKA_Cs&list=PL68tctImfhCR2zFIxzEs95v5ETSXe9r14)

    * [Rhino Python](http://developer.rhino3d.com/5/guides/rhinopython/)

    * [Tutorial Rhino Python em vídeo (eng)](https://www.youtube.com/watch?v=wdY1T0XLzkE&list=PL594EB4471E93F2DA)

    * [Rhino -material de aula](https://255ribeiro.github.io/cad_intro/)

___

### Aula 06 -

1. Interface do Grasshopper

   * Parâmetros de entrada
   * Sequência de comandos
   * Bake
   * Exemplos
   * Listas
   * Exemplos

2. Sequência de colunas no Grasshopper

3. Grasshopper Python Component (GhPython)

4. Exercício 06 - Criar sequência de colunas do GhPython.

5. Arquivos dos Exemplos da Aula
    [Rhino Python](topics/05_intro_rhino_py/rhino_python.md)
    [Rhino Grasshopper](./topics/06_intro_grasshopper/intro_grasshopper.md)

6. Referências e *links* úteis

___

### Aula 07 -


1. Treliças

[Treliças](./topics/07_trelicas/trelicas.md)
___

### Aula 08 -


Malha de Pilares

[Malha de Pilares regulares](./topics/08_malha_reg/malha_reg.md)

___

### Aula 09 -

[Malha de pilares irregulares](topics/09_malha_irreg/malha_irreg.md)

___

### Aula 10 -

[Edf. Múltiplos pavimentos](./topics/10_multi_pav/multipav.md)

### Aula 11 -

[Funções definidas pelo usuário - Python](./topics/04a_func_python/functionsPyton3.md)

[Funções definidas pelo usuário - Grasshopper](topics/04a_func_python/functionsRhinoGrass.md)

___

### Aula 12 -

[Listas e data tree](./topics/12_lists_data_tree/lists_and_data_trees.md)

___

### Aula 13 -

1. Biblioteca ghpythonlib.components

1. Exercício 13 - ????

1. Referências e *links* úteis

    [referência da biblioteca ghpythonlib](https://developer.rhino3d.com/guides/rhinopython/ghpython-component/)

    [EliFront](https://www.food4rhino.com/app/elefront)

___

### Aula 14 -

[Fractais](topics/13_fractals/fractais.md)

___

### Aula 15 -

1. Orientação de trabalhos

___

### Aula 16 -

1. Orientação de trabalhos

___

### Aula 17 -

1. Encerramento do Curso

2. Referências e *links* úteis

    [Tutoriais de C# para Grasshopper](http://designalyze.com/course/intro-c-scripting-grasshopper)

    [Tutoriais de C# para Grasshopper](https://www.youtube.com/watch?v=pFCrIzENDn8&list=PLapoQ_9M-ujfYGOsZProIXPGx-HRfjJ9C)

    [Compilando um componente Python no Rhino 6](https://discourse.mcneel.com/t/tutorial-creating-a-grasshopper-component-with-the-python-ghpy-compiler/38552)

___
___
