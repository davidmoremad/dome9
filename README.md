# Dome9 (Python SDK)

![GitHub License](https://img.shields.io/github/license/davidmoremad/dome9?style=flat-square)
[![Documentation Status](https://readthedocs.org/projects/dome9/badge/?version=latest&style=flat-square)](http://dome9.readthedocs.io/?badge=latest)
[![Build, Lint & Test](https://github.com/davidmoremad/dome9/actions/workflows/main.yaml/badge.svg)](https://github.com/davidmoremad/dome9/actions/workflows/main.yaml)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/dome9?label=python%20version&style=flat-square)
![PyPI](https://img.shields.io/pypi/v/dome9?label=pypi%20package&style=flat-square)


Dome9, also known as Checkpoint CloudGuard, is a cloud native security solutions for securing
assets and workloads. At the core of this solution, CloudGuard Posture Management visualizes and
assesses security posture, detects misconfigurations, automates and actively enforces standard
policies (GDPR, HIPAA, ISO27001...), and protects against attacks and insider threats. 

This repository contains a Python SDK of this tool. Initially its SDK did not have much functionality
and that is why I developed this one to be able to work and include it within my Continuous Integration processes.

If you want to integrate Dome9 as part of your CI, check my other modules: [Dome9 CLI and Agile](https://github.com/davidmoremad/dome9cli).

## 🚀 Installation

```bash
pip install dome9  # Install last stable version
```
**📚 Documentation**: https://dome9.readthedocs.io/


## ⚙️ Usage

There are two ways to authenticate:
* **As Arguments**: Passing variables on init -> `Dome9(key='xxxxxx', secret='yyyyyyy')`
* **As Environment variables**: Setting your credentials as environment variables -> `DOME9_ACCESS_KEY` and `DOME9_SECRET_KEY`


```python
from dome9 import Dome9

dome9 = Dome9(key='xxxxxx', secret='yyyyyyy')

rulesets = dome9.list_rulesets()
```

```bash
export DOME9_ACCESS_KEY='xxxxxxxxxxxxxxxxxxxx'
export DOME9_SECRET_KEY='yyyyyyyyyyyyyyyyyyyy'
python -c "from dome9 import Dome9; print(Dome9().list_rulesets())"
```


## 🔥 What can I do?

* 🌵 List all cloud accounts -> `dome9.list_cloud_accounts()`
* 🌻 List AWS accounts -> `dome9.list_aws_accounts()`
* 🌷 List KUBERNETES accounts -> `dome9.list_kubernetes_accounts()`
* 🌼 Create ruleset -> `dome9.create_ruleset()`
* 🌴 Create remediation -> `dome9.create_remediation()`
* 🌲 Connect new AWS account -> `dome9.create_aws_account()`
* 🌹 Run assessment -> `dome9.run_assessment()`
* 🍀 List all your cloud assets -> `dome9.list_protected_assets()`

