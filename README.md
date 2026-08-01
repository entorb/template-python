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

see [run_update.sh](scripts/run_update.sh)

## Pytest Unit Tests

```sh
# for console output
uv run pytest --cov
# for html output in htmlcov/ dir
uv run pytest --cov --cov-report=html
# for sonarqube compatible report
uv run pytest tests/ --cov --cov-report=xml:coverage.xml
```

see [chk_py_test.sh](scripts/chk_py_test.sh) and [run_pytest_cov.sh](scripts/run_pytest_cov.sh)

## Ruff formatter and linter

- config in [ruff.toml](ruff.toml)
- [chk_py_lint.sh](scripts/chk_py_lint.sh)
- or `uv run ruff format` and `uv run ruff check --fix` or even `uv run ruff check --fix --unsafe-fixes`

To disable a certain rule

- **for a file** add `# ruff: noqa: D103` at the top
- **for a specific line** append `# noqa: D103`

see [chk_py_lint.sh](scripts/chk_py_lint.sh)

## GitHub Actions

- [dependabot.yml](.github/dependabot.yml)
- [check.yml](.github/workflows/check.yml) check commits and PRs
- [update.yml](.github/workflows/update.yml) auto-update some packages

## SonarQube Code Analysis

- Report at [sonarcloud.io](https://sonarcloud.io/summary/overall?id=entorb_template-python&branch=main)
- Or per API as [json](https://sonarcloud.io/api/issues/search?componentKeys=entorb_template-python&ps=500)

### Using GitHub Action to scan and provide unit test coverage report

- disable the "Automatic Analysis" at <https://sonarcloud.io/project/analysis_method?id=entorb_template-python>
- setup SonarSource/sonarqube-scan-action@v5 in [check.yml](.github/workflows/check.yml)
- rename [.sonarcloud.properties](.sonarcloud.properties) to [sonar-project.properties](sonar-project.properties)
- generate a token at <https://sonarcloud.io/account/security>
- add this token as secret SONAR_TOKEN in GitHub

see [check.yml](.github/workflows/check.yml)

## Code Checks

[run_checks.sh](scripts/run_checks.sh) runs all `chk_*.sh` scripts in sequence and reports failures.

### Pre-commit via prek

see <https://prek.j178.dev/> and <https://pre-commit.com>

```sh
# run
prek run --all-files

# auto-update all hooks
prek autoupdate

# to trigger prek automatically at each `git commit` command
prek install
```

### CSpell Code Checker

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

see [chk_spelling.sh](scripts/chk_spelling.sh) and

### Markdownlint

- config in [.markdownlint-cli2.yaml](.markdownlint-cli2.yaml)

```sh
npm exec markdownlint-cli2 --fix "**/*.md"
```

see [chk_md_lint.sh](scripts/chk_md_lint.sh)
