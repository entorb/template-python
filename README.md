# Torben's Python Template

My Python template repo, using the following tools:

## UV package manager

[UV](https://docs.astral.sh/uv/) manages Python and package versions, as well as venv.

```sh
# run
uv run src/main.py

# update a package
uv lock --upgrade-package pytest
# uv lock --upgrade
uv sync
```

see [update.sh](scripts/update.sh)

## Pytest Unit Tests

```sh
# for console output
uv run pytest --cov
# for html output in htmlcov/ dir
uv run pytest --cov --cov-report=html
# for sonarqube compatible report
uv run pytest tests/ --cov --cov-report=xml:coverage.xml
```

## Ruff formatter and linter

- config in [ruff.toml](ruff.toml)
- [run_ruff.sh](scripts/run_ruff.sh)
- or `uv run ruff format` and `uv run ruff check --fix` or even `uv run ruff check --fix --unsafe-fixes`

To disable a certain rule

- **for a file** add `# ruff: noqa: D103` at the top
- **for a specific line** append `# noqa: D103`

## GitHub Actions

- [dependabot.yml](.github/dependabot.yml)
- [check.yml](.github/workflows/check.yml)
- [update.yml](.github/workflows/update.yml)

## SonarQube Code Analysis

See report at [sonarcloud.io](https://sonarcloud.io/summary/overall?id=entorb_template-python&branch=main)

### Using GitHub Action to scan and provide unit test coverage report

- disable the "Automatic Analysis" at <https://sonarcloud.io/project/analysis_method?id=entorb_template-python>
- setup SonarSource/sonarqube-scan-action@v5 in [check.yml](.github/workflows/check.yml)
- rename [.sonarcloud.properties](.sonarcloud.properties) to [sonar-project.properties](sonar-project.properties)
- generate a token at <https://sonarcloud.io/account/security>
- add this token as secret SONAR_TOKEN in GitHub

see [check.yml](.github/workflows/check.yml)

## Pre-commit

see <https://pre-commit.com>

```sh
# run
uv run pre-commit run --all-files
# or ./scripts/run_pre-commit.sh

# auto-update all hooks
uv run pre-commit autoupdate

# to trigger pre-commit automatically at each `git commit` command
uv run pre-commit install
```

## CSpell Code Checker

(run by pre-commit and VSCode)

see <https://cspell.org> and [cspell.org/configuration/document-settings/](https://cspell.org/configuration/document-settings/)

- [cspell.config.yaml](cspell.config.yaml) config
- [cspell-words.txt](cspell-words.txt) custom dictionary, add unknown words here

To disable cspell checking of a file or path, you can use

- add a `# cspell: disable` comment inside that file
- exclude via [cspell.config.yaml](cspell.config.yaml) -> ignorePaths

To disable the spellchecking for a section of the file

```sh
# cspell: disable
# ...
# cspell: enable
```

To disable for a single line `# cspell:disable-next-line`

Ignore words per file

- `# cspell:ignore myword myyword` add to file-specifiv ignore list
- `# cspell:words myword myyword` add to file-specifiv dictionary
- `# cspell:ignoreRegExp g{5}|h{5}`
