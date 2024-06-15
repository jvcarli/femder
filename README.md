![Static Badge](https://img.shields.io/badge/python-3.9%20%7C%203.10%20%7C%203.11-blue)
![Static Badge](https://img.shields.io/badge/version-v0.2.0-orange?logo=github)

_Read in other languages: [en-US](https://github.com/jvcarli/femder/blob/main/README.md),
[pt-BR](https://github.com/jvcarli/femder/blob/main/README.pt-BR.md)_

# femder

A Finite Element Method (FEM) code for acoustics written for the undergraduate course
"Métodos Numéricos em Acústica e Vibrações", ministered by Dr. Paulo Mareze.

## Acknowledgement

**Original author**: Luiz Augusto T. Ferraz Alvim <br/>
**Original co-author**: Dr. Paulo Mareze

This repository was initially a fork from
[gutoalvim/femder](https://github.com/gutoalvim/femder/), but it was detached.
It shares its codebase from the parent first commit until
[gutoalvim/femder@`16a7231`](https://github.com/gutoalvim/femder/commit/16a7231).
From [jvcarli/femder@`a447e21`](https://github.com/jvcarli/femder/commit/a447e21)
onwards they diverge.

## Installation

Prerequisites:

- Python >= 3.9, < 3.12

**NOTE**: If you're a beginner at programming we strongly recommend that
you follow the conda installation guide below and download
[Anaconda Distribution](https://www.anaconda.com/download) - it includes
Python, [NumPy](https://github.com/numpy/numpy), many other commonly used packages
for scientific computing and
[conda](https://docs.conda.io/en/latest/) - a
[package manager](https://en.wikipedia.org/wiki/Package_manager)
that makes it easier to install and manage other packages you may need.

**Follow the instructions bellow**:

<details>

<summary>For <a href="https://docs.conda.io"><code>conda</code></a> - a package manager that comes with <a href="https://www.anaconda.com/download">Anaconda Distribution</a>, <a href="https://docs.anaconda.com/free/miniconda/">Miniconda</a> and <a href="https://github.com/conda-forge/miniforge">Miniforge</a> (<em>click to expand</em>):</summary>

- You'll need a [shell](https://en.wikipedia.org/wiki/Shell_(computing))
with `conda` in its [`PATH`](https://en.wikipedia.org/wiki/PATH_(variable)).

  If you're using Windows and have installed Anaconda Distribution, Miniconda, or Miniforge,
  you'll have access to the **`Anaconda Prompt`**,
  **`Anaconda Prompt (miniconda3)`**, or **`Miniforge Prompt`**, respectively.
  Search for them under Windows start menu.

- Create and activate your `conda` environment:

  Creating a new `conda` environment for each project you work on
  is considered a best practice, ensuring better management and isolation of dependencies
  and promoting a cleaner development workflow.

  You **MUST** use Python >= 3.9, < 3.12.

  ```
  conda create -n myenv python=3.9
  conda activate myenv
  ```

- Install `femder` using `pip`:

  ```
  pip install femder
  ```

</details>

<details>

<summary>For <a href="https://pip.pypa.io/en/stable/getting-started/"><code>pip</code></a> - a package manager that comes with Python (<em>click to expand</em>):</summary>

- Optional step (**recommended**) - consider using a [virtual environment](https://docs.python.org/3/library/venv.html):

  Creating a new virtual environment for each project you work on
  is considered a best practice, ensuring better management and isolation of dependencies
  and promoting a cleaner development workflow.

  - Create your virtual environment as usual:

    ```
    python -m venv venv
    ```

  - Activate the virtual environment:

    - If you use Windows:

      ```
      .\venv\Scripts\activate
      ```

    - If you use macOS or a Linux distribution:

      ```
      source venv/bin/activate
      ```

- Install `femder` using `pip`:

  ```
  pip install femder
  ```

</details>

## Examples

For instructions on running the examples,
please refer to the [README](https://github.com/jvcarli/femder/tree/main/examples)
file in the `examples` directory.

## Contributing

Thank you for considering contributing to `femder`!
You can contribute as a user or as developer,
please read our [contribution guide](https://github.com/jvcarli/femder/blob/main/CONTRIBUTING.md).

Remember, no contribution is too small! Every line of code, every documentation update,
and every bug report helps making the library better for everyone.

---

Have fun doing acoustics! If you experience any bugs or problems, have any suggestions or ideas,
please [open an issue](https://github.com/jvcarli/femder/issues/new).

Special thanks to Luiz Augusto Alvim, Dr. Paulo Mareze, Dr. Eric Brandão, Alexandre Piccini and Rinaldi Petrolli.
