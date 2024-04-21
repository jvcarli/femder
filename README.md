![Static Badge](https://img.shields.io/badge/python-3.9%20%7C%203.10%20%7C%203.11-blue)
![Static Badge](https://img.shields.io/badge/version-v0.1.0-orange?logo=github)

# femder

A Finite Element Method (FEM) code for acoustics written for the undergraduate course
"Métodos Numéricos em Acústica e Vibrações", ministered by Dr. Paulo Mareze.

**Author**: Luiz Augusto T. Ferraz Alvim <br/>
**Co-Author**: Dr. Paulo Mareze

## Installation

Prerequisites:

- Git
- Python >= 3.9, < 3.12

**NOTE**: If you're a beginner at programming we strongly recommend you to
use [Anaconda Distribution](https://www.anaconda.com/download) - it includes
Python, [NumPy](https://github.com/numpy/numpy),
and many other commonly used packages for scientific computing and data science.
It also includes [conda](https://docs.conda.io/en/latest/),
a [package manager](https://en.wikipedia.org/wiki/Package_manager)
that makes it easier to install and manage other packages you may need, like `git`.

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

  You **MUST** use Python >= 3.9, < 3.12.

  ```
  conda create -n myenv python=3.9
  conda activate myenv
  ```

  **NOTE**: Creating a new `conda` environment for each project you work on
  is considered a best practice, ensuring better management of dependencies
  and promoting a cleaner development workflow.

- Optional step (only if you haven't `git` installed yet and want `conda` to manage it):

  ```
  conda install git
  ```

- Install `femder` using `pip`:

  ```
  pip install git+https://github.com/jvcarli/femder.git
  ```

</details>

<details>

<summary>For <a href="https://pip.pypa.io/en/stable/getting-started/"><code>pip</code></a> - a package manager that comes with Python (<em>click to expand</em>):</summary>

- Install `git` using your preferred way.

- Optional step (**recommended**) - consider using a [virtual environment](https://docs.python.org/3/library/venv.html):

  Utilizing a virtual environment with `pip` is recommended as it allows
  for the isolation of project dependencies, enhancing dependency management
  and facilitating working across diverse projects.

  - Create your virtual environment as usual:

    ```
    python -m venv venv
    ```

  - Activate the virtual environment:

    - If you use Windows:

      ```
      source venv\Scripts\activate
      ```

    - If you use macOS or a Linux distribution:

      ```
      source venv/bin/activate
      ```

- Install `femder` using `pip`:

  ```
  pip install git+https://github.com/jvcarli/femder.git
  ```

</details>

## Examples

For instructions on running the examples,
please refer to the [README](./examples)
file in the `examples` directory.

## Contributing

Thank you for considering contributing to `femder`!
You can contribute as a user or as developer,
please read our [contribution guide](./CONTRIBUTING.md).

Remember, no contribution is too small! Every line of code, every documentation update,
and every bug report helps making the library better for everyone.

---

Have fun doing acoustics! If you experience any bugs or problems, have any suggestions or ideas,
please [open an issue](https://github.com/jvcarli/femder/issues/new).

Special thanks to Luiz Augusto Alvim, Dr. Paulo Mareze, Dr. Eric Brandão, Alexandre Piccini and Rinaldi Petrolli.
