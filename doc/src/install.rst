Install
=======

Prerequisites
-------------

For installing ``femder`` you'll need:

- Git
- Python >= 3.9, < 3.12

.. note::

  If you're a beginner at programming we strongly recommend you to
  use `Anaconda Distribution <https://www.anaconda.com/download>`_ - it includes
  Python, `NumPy <https://github.com/numpy/numpy>`_,
  and many other commonly used packages for scientific computing and data science.
  It also includes `conda <https://docs.conda.io/en/latest/>`_,
  a `package manager <https://en.wikipedia.org/wiki/Package_manager>`_
  that makes it easier to install and manage other packages you may need, like ``git``.


Conda
=====

`conda <https://docs.conda.io>`_ is a package manager that comes with `Anaconda Distribution <https://www.anaconda.com/download>`_,
`Miniconda <https://docs.anaconda.com/free/miniconda/>`_ and `Miniforge <https://github.com/conda-forge/miniforge>`_.

For installing ``femder`` using ``conda`` follow the steps below:

- You'll need a `shell <https://en.wikipedia.org/wiki/Shell_(computing)>`_ with ``conda`` in its `PATH <https://en.wikipedia.org/wiki/PATH_(variable)>`_:

  .. admonition:: Note for Windows users
     :class: note

     If you're using Windows and have installed Anaconda Distribution, Miniconda, or Miniforge,
     you'll have access to the **Anaconda Prompt**,
     **Anaconda Prompt (miniconda3)**, or **Miniforge Prompt**, respectively.
     Search for them under Windows start menu.

- Create and activate your ``conda`` environment:

  You **MUST** use Python >= 3.9, < 3.12.

  .. code-block::

     conda create -n myenv python=3.9
     conda activate myenv

  .. note::

     Creating a new ``conda`` environment for each project you work on
     is considered a best practice, ensuring better management of dependencies
     and promoting a cleaner development workflow.

- Optional step (only if you haven't ``git`` installed yet and want ``conda`` to manage it):

  ``conda install git``

- Install ``femder`` using ``pip``:

  ``pip install git+https://github.com/jvcarli/femder.git``

Pip
===

.. TODO: add tabs for windows / macos / linux venv instructions

`Pip <https://pip.pypa.io/en/stable/getting-started/>`_ is a package manager that comes with Python.

For installing ``femder`` using ``pip`` follow the steps below:

- Install ``git`` using your preferred way.

- Optional step (**recommended**) - consider using a `virtual environment <https://docs.python.org/3/library/venv.html>`_:

  .. note::

    Utilizing a virtual environment with ``pip`` is recommended as it allows
    for the isolation of project dependencies, enhancing dependency management
    and facilitating working across diverse projects.

  - Create your virtual environment as usual:

    ``python -m venv venv``

  - Activate the virtual environment:

    - If you use Windows:

      ``source venv\Scripts\activate``

    - If you use macOS or a Linux distribution:

      ``source venv/bin/activate``

- Install ``femder`` using ``pip``:

  ``pip install git+https://github.com/jvcarli/femder.git``
