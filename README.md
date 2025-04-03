# Torben's Python Template

Based on <https://github.com/entorb/pre-commit-config>

## SonarQube

Report is here: <https://sonarcloud.io/project/overview?id=entorb_template-python>

### Using GitHub Action to scan and provide unit test coverage report

* disable the "Automatic Analysis" at <https://sonarcloud.io/project/analysis_method?id=entorb_template-python>
* setup SonarSource/sonarqube-scan-action@v4 in [check.yml](.github/workflows/check.yml)
* rename [.sonarcloud.properties](.sonarcloud.properties) to [sonar-project.properties](sonar-project.properties)
* generate a token at <https://sonarcloud.io/account/security>
* add this token as secret SONAR_TOKEN in GitHub
