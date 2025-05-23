# Torben's Python Template

Based on <https://github.com/entorb/pre-commit-config>

## UV package manager

TODO: how to update all packages

```sh
uv lock --upgrade-package pytest
# uv lock --upgrade
uv sync
```

## Unit Tests

```sh
# for console output
pytest --cov
# for html output in htmlcov/ dir
pytest --cov --cov-report=html
```

## SonarQube Code Analysis

At [sonarcloud.io](https://sonarcloud.io/summary/overall?id=entorb_template-python&branch=main)

### Using GitHub Action to scan and provide unit test coverage report

* disable the "Automatic Analysis" at <https://sonarcloud.io/project/analysis_method?id=entorb_template-python>
* setup SonarSource/sonarqube-scan-action@v5 in [check.yml](.github/workflows/check.yml)
* rename [.sonarcloud.properties](.sonarcloud.properties) to [sonar-project.properties](sonar-project.properties)
* generate a token at <https://sonarcloud.io/account/security>
* add this token as secret SONAR_TOKEN in GitHub
