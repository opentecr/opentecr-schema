# OpenTECR Schema

| |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|---|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Package | [![Latest PyPI Version](https://img.shields.io/pypi/v/opentecr-schema.svg)](https://pypi.org/project/opentecr-schema/) [![Supported Python Versions](https://img.shields.io/pypi/pyversions/opentecr-schema.svg)](https://pypi.org/project/opentecr-schema/) [![Documentation](https://readthedocs.org/projects/opentecr-schema/badge/?version=latest)](https://opentecr-schema.readthedocs.io/en/latest/?badge=latest)                                                                                                                                                                         |
| Meta | [![MIT](https://img.shields.io/pypi/l/opentecr-schema.svg)](LICENSE) [![Code of Conduct](https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg)](.github/CODE_OF_CONDUCT.md) [![Code Style Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)                                                                                                                                                          |
| Automation | [![GitHub Workflow](https://github.com/rgiessman/opentecr-schema/workflows/CI-CD/badge.svg)](https://github.com/rgiessman/opentecr-schema/workflows/CI-CD) [![Code Coverage](https://codecov.io/gh/rgiessman/opentecr-schema/branch/master/graph/badge.svg)](https://codecov.io/gh/rgiessman/opentecr-schema) |

contains the code for the schema of the openTECR database

## Post Template-Instantiation Steps

1. Start working with git.

    ```shell
    git init
    ```

2. Install the git pre-commit hooks using the `pre-commit` tool.

    ```shell
    pip install pre-commit
    pre-commit install
    ```

3. Commit all the files.

    ```shell
    git add .
    git commit -m "chore: initialize project cookiecutter"
    ```

4. Create a repository on [GitHub](https://github.com) if you haven't done
   so yet.
5. Browse through the architecture decision records (`docs/adr`) if you want
   to understand details of the package design.
6. Remove this section from the readme and describe what your package is all
   about.
7. When you're ready to make a release, perform the following steps.

   1. On [GitHub](https://github.com) set the secure environment
      variables `PYPI_USERNAME` and `PYPI_PASSWORD` to `__token__` and a respective PyPI API token.
   2. Tag your latest commit with the desired version and let GitHub handle
      the release.

        ```shell
        git tag 0.1.0
        git push origin 0.1.0
        ```

## Copyright

* Copyright © 2023 OpenTECR developers.
* Free software distributed under the [MIT License](../LICENSE).

