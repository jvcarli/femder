# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and starting from **v0.1.0** this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).
From [`79aeeb1`](https://github.com/jvcarli/femder/commit/79aeeb1) commit onwards it uses [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)
specification for its commit messages.

## [v0.1.0] - 2024-04-14

This release is concerned with housekeeping. No functionality from the library itself was changed,
however some breaking changes were introduced in the process.

**BREAKING CHANGES**:

Due to the use of [`sphinx`](https://github.com/sphinx-doc/sphinx)
to document the library, the minimum required python version was bumped from 3.8.x to 3.9.x.

When [`numba`](https://github.com/numba/numba) >= 0.59 is used the library breaks.
Because of this, `numba` version was fixed on < 0.59.

`numba` < 0.59 only works with Python < 3.12
so the maximum python version was restricted to 3.11.x.

`femder` now uses [`kaleido`](https://github.com/plotly/Kaleido) instead of
[`orca`](https://github.com/plotly/orca) for static image generation of interactive plotly charts.
Due to this [`plotly`](https://github.com/plotly/plotly.py) minimum version now is 4.9.

### Added

- **documentation dependency**: [`sphinx`](https://github.com/sphinx-doc/sphinx) documentation generator to document the project.
- **documentation dependency**: [`pydata-sphinx-theme`](https://github.com/pydata/pydata-sphinx-theme) as a `sphinx` html theme.
- **documentation development dependency**: [`sphinx-autobuild`](https://github.com/sphinx-doc/sphinx-autobuild)
to help rebuild the documentation while it is being written.
- **development dependency**: [`ruff`](https://github.com/astral-sh/ruff) for linting and formatting the library.
- Documentation scaffold (initial work for providing user friendly documentation).
- internal files for helping the developers of the project
(`.gitattributes`, `.git-blame-ignore-revs` and `.editorconfig`).

### Changed

- **BREAKING CHANGE**: required python version now is >= 3.9,< 3.12.
- **BREAKING CHANGE**: `numba` required version was restricted to < 0.59.
- **BREAKING CHANGE**: `plotly` required version was restricted to >= 4.9.
- `setup.py` was replaced with [`pyproject.toml`](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/)
for enhanced packaging and dependency management.
- `femder` package was moved to `src/femder` directory.
- `femder` dependencies were reorganized into `requirements` directory.
`pyproject.toml` is configured to read the dependencies from these files.
- [`kaleido`](https://github.com/plotly/Kaleido) is now used instead of [`orca`](https://github.com/plotly/orca)
for generating static images of interactive plotly charts.
- All `femder` *.py modules were formatted with [`ruff`](https://github.com/astral-sh/ruff)
formatter for consistent formatting.
- `examples` instructions were moved from top-level `README.md` to `examples/README.md`.
- `Mshs` directory was moved to `examples/mshs` directory.

### Removed

- unnecessary `__pycache__` directory.
- unused modules (`points.py` and `BEM_3D_copy.py`).
- unused *.msh files.
- code from `FEM_3D.py` that was dependent on a non-existent file.
- [`conda`](https://docs.conda.io/en/latest/) `environment.yml` file was removed for now.
It will be reintroduced later.

<details>

<summary>Relevant commits:</summary>

* [`66806c3`](https://github.com/jvcarli/femder/commit/66806c3) chore: update top-level README (Joao Vitor Carli Pereira)
* [`ca1af36`](https://github.com/jvcarli/femder/commit/ca1af36) chore: use .md extension for README files (Joao Vitor Carli Pereira)
* [`9fdaa86`](https://github.com/jvcarli/femder/commit/9fdaa86) build!: restrict python versions to >= 3.9,<3.12 (Joao Vitor Carli Pereira)
* [`1cfac01`](https://github.com/jvcarli/femder/commit/1cfac01) fix: remove code that was dependent on a non-existent file (Joao Vitor Carli Pereira)
* [`fb3ed10`](https://github.com/jvcarli/femder/commit/fb3ed10) chore: update top-level README (Joao Vitor Carli Pereira)
* [`2f2c9ea`](https://github.com/jvcarli/femder/commit/2f2c9ea) style: add .editorconfig (Joao Vitor Carli Pereira)
* [`74cca8a`](https://github.com/jvcarli/femder/commit/74cca8a) docs: clean documentation index (Joao Vitor Carli Pereira)
* [`7fc45a9`](https://github.com/jvcarli/femder/commit/7fc45a9) docs: move examples instructions to examples directory (Joao Vitor Carli Pereira)
* [`9dc85df`](https://github.com/jvcarli/femder/commit/9dc85df) docs: replace default sphinx theme with pydata-sphinx-theme (Joao Vitor Carli Pereira)
* [`2c95d57`](https://github.com/jvcarli/femder/commit/2c95d57) docs: add sphinx-autobuild dependency for developing the documentation (Joao Vitor Carli Pereira)
* [`2244454`](https://github.com/jvcarli/femder/commit/2244454) build: remove plotly-orca dependency in favor of kaleido (Joao Vitor Carli Pereira)
* [`947e106`](https://github.com/jvcarli/femder/commit/947e106) refactor: move Mshs directory to examples/mshs (Joao Vitor Carli Pereira)
* [`7b15a0a`](https://github.com/jvcarli/femder/commit/7b15a0a) fix: delete unused module points.py (Joao Vitor Carli Pereira)
* [`33cc8c6`](https://github.com/jvcarli/femder/commit/33cc8c6) chore: add .gitattributes (Joao Vitor Carli Pereira)
* [`f3dd83f`](https://github.com/jvcarli/femder/commit/f3dd83f) build: remove conda environment.yml (Joao Vitor Carli Pereira)
* [`07ecab0`](https://github.com/jvcarli/femder/commit/07ecab0) chore: add .git-blame-ignore-revs file (Joao Vitor Carli Pereira)
* [`32179f0`](https://github.com/jvcarli/femder/commit/32179f0) style: run ruff formatter for the first time (Joao Vitor Carli Pereira)
* [`79aeeb1`](https://github.com/jvcarli/femder/commit/79aeeb1) refactor: reorganize femder dependencies (Joao Vitor Carli Pereira)
* [`d72522f`](https://github.com/jvcarli/femder/commit/d72522f) move docs directory to doc (nitpick) (Joao Vitor Carli Pereira)
* [`1373b37`](https://github.com/jvcarli/femder/commit/1373b37) remove unused *.msh files (Joao Vitor Carli Pereira)
* [`58cd037`](https://github.com/jvcarli/femder/commit/58cd037) remove unused python module (Joao Vitor Carli Pereira)
* [`e01a462`](https://github.com/jvcarli/femder/commit/e01a462) fix pip install url (Joao Vitor Carli Pereira)
* [`a10e608`](https://github.com/jvcarli/femder/commit/a10e608) rewrite README.md in rst (Joao Vitor Carli Pereira)
* [`e05e2e6`](https://github.com/jvcarli/femder/commit/e05e2e6) add documentation scaffold (Joao Vitor Carli Pereira)
* [`44a01c3`](https://github.com/jvcarli/femder/commit/44a01c3) move femder package to src directory (Joao Vitor Carli Pereira)
* [`54e7fef`](https://github.com/jvcarli/femder/commit/54e7fef) delete unnecessary __pycache__ directory (Joao Vitor Carli Pereira)
* [`d30a13f`](https://github.com/jvcarli/femder/commit/d30a13f) add pyproject.toml (Joao Vitor Carli Pereira)
* [`a447e21`](https://github.com/jvcarli/femder/commit/a447e21) remove setup.py in favor of pyproject.toml (Joao Vitor Carli Pereira)

</details>

## [v0.0.1] - 2023-11-08

Until v0.1.0 `femder` didn't follow any version policy practices
and the library was assumed to be `v0.0.1` from the [`first commit`](https://github.com/jvcarli/femder/commit/961a9fc)
until [`16a7231`](https://github.com/jvcarli/femder/commit/16a7231).

For practical purposes we'll call [`16a7231 commit`](https://github.com/jvcarli/femder/commit/16a7231) **v0.0.1**.

This release can be found at: <https://github.com/jvcarli/femder/releases/tag/v0.0.1>

[v0.1.0]: https://github.com/jvcarli/femder/compare/v0.0.1...v0.1.0
[v0.0.1]: https://github.com/jvcarli/femder/compare/961a9fc...v0.0.1
