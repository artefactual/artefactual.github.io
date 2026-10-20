# Contributors portal

Hi! Welcome to our contributors portal.

The first version of this site was built in July 2024. Visit us at
artefactual.github.io

- The Community Team.

## Building the website locally

To build the website locally, you will need to install:

```shell
pip install Sphinx
pip install furo
```

You will then be able to use `make html` to build the HTML version of the
website, which will be in `build/html`.

## Contributing

At the moment speaking and for the foreseeable future, we expect that
contributions will be made by Artefactual staff from time to time.
We do not expect any external contributor to make a PR, but you are welcome to
[file an issue](https://github.com/artefactual/artefactual.github.io/issues) if
you have general questions about contributing.

### pre-commit

We use pre-commit hooks to check for formatting with `doc8` and `sphinx-lint`.

You should be able to use `pre-commit install` to install the hooks.
