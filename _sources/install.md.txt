# Install

## Prerequisites

For installing `femder` you'll need:

- Python >= 3.9, < 3.12

```{note}
If you're a beginner at programming we strongly recommend you to
use [`Anaconda Distribution`](https://www.anaconda.com/download) - it includes
Python, [`NumPy`](https://github.com/numpy/numpy),
and many other commonly used packages for scientific computing and data science.
It also includes [`conda`](https://docs.conda.io/en/latest/),
a [package manager](https://en.wikipedia.org/wiki/Package_manager)
that makes it easier to install and manage other packages you may need.
```

## Conda

[`conda`](https://docs.conda.io) is a package manager that comes with [`Anaconda Distribution`](https://www.anaconda.com/download),
[`Miniconda`](https://docs.anaconda.com/free/miniconda/) and [`Miniforge`](https://github.com/conda-forge/miniforge).

For installing `femder` using `conda` follow the steps below:

- You'll need a [shell](<https://en.wikipedia.org/wiki/Shell_(computing)>) with `conda` in its [PATH](<https://en.wikipedia.org/wiki/PATH_(variable)>):

  ```{admonition} Note for Windows users
  :class: note

  If you're using Windows and have installed Anaconda Distribution, Miniconda, or Miniforge,
  you'll have access to the **Anaconda Prompt**,
  **Anaconda Prompt (miniconda3)**, or **Miniforge Prompt**, respectively.
  Search for them under Windows start menu.
  ```

- Create and activate your `conda` environment:

  You **MUST** use Python >= 3.9, < 3.12.

  ```
  $ conda create -n myenv python=3.9
  $ conda activate myenv
  ```

  ```{note}
  Creating a new `conda` environment for each project you work on
  is considered a best practice, ensuring better management of dependencies
  and promoting a cleaner development workflow.
  ```

- Install `femder` using `pip`:

  `$ pip install femder`

## Pip

[`Pip`](https://pip.pypa.io/en/stable/getting-started/) is a package manager that comes with Python.

For installing `femder` using `pip` follow the steps below:

- Optional step (**recommended**) - consider using a [`virtual environment`](https://docs.python.org/3/library/venv.html):

  ```{note}
  Utilizing a virtual environment with `pip` is recommended as it allows
  for the isolation of project dependencies, enhancing dependency management
  and facilitating working across diverse projects.
  ```

  - Create your virtual environment as usual:

    `$ python -m venv venv`

  - Activate the virtual environment:

    - If you use Windows:

      `> .\venv\Scripts\activate`

    - If you use macOS or a Linux distribution:

      `$ source venv/bin/activate`

- Install `femder` using `pip`:

  `$ pip install femder`
