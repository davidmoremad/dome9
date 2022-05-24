.. Dome9 documentation master file, created by
   sphinx-quickstart on Sun Sep 29 14:56:54 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Dome9's documentation!
=================================

.. toctree::
  :hidden:
  :maxdepth: 2
  :caption: Contents:

  Accounts.rst
  Rulesets.rst
  Remediations.rst
  Exclusions.rst
  Assessments.rst
 

.. toctree::
  :hidden:
  :maxdepth: 2
  :caption: Sitemap:

  dome9.rst

|Version| |Docs| 


.. |Docs| image:: https://readthedocs.org/projects/dome9/badge/?version=latest
   :target: http://dome9.readthedocs.io/en/latest/?badge=latest
   :alt: Read the Docs
.. |Version| image:: http://img.shields.io/pypi/v/dome9.svg?style=flat
   :target: https://pypi.python.org/pypi/dome9/
   :alt: Version


Dome9 is a web service that allows you to improve the security of your cloud technologies 
(AWS, Azure, GCP, Kubernetes, etc...). Through its service you can centralize all the information
and perform security controls (GDPR, HIPAA, ISO27001...) individually or globally.

This repository contains a Python SDK of this tool. Initially its SDK did not have much functionality
and that is why I developed this one to be able to work and include it within my continuous integration processes.


Installation
------------

.. code-block:: bash

   pip install dome9



Usage
-----

.. code-block:: python

   from dome9 import Dome9

   dome9 = Dome9(key='xxxxxx', secret='yyyyyyy')

   rulesets = dome9.list_rulesets()


Authentication
--------------

There are two ways to authenticate:

* **As Arguments**: Passing variables on init -> **Dome9(key='xxxxxx', secret='yyyyyyy')**
* **As Environment variables**: Setting your credentials as environment variables -> **DOME9_ACCESS_KEY** and **DOME9_SECRET_KEY**

Example:


.. code-block:: python
   
   from dome9 import Dome9

   dome9 = Dome9(key='xxxxxx', secret='yyyyyyy')

   rulesets = dome9.list_rulesets()


.. code-block:: bash

   export DOME9_ACCESS_KEY='xxxxxxxxxxxxxxxxxxxx'
   export DOME9_SECRET_KEY='yyyyyyyyyyyyyyyyyyyy'
   python -c "from dome9 import Dome9; print(Dome9().list_rulesets())"


Agile
-----

.. code-block:: python

    import json
    from dome9 import Dome9

    cloudAccount = '00000-00000-00000-00000'

    d9 = Dome9()

    rulesetTemplate = {}
    with open('ruleset','r') as f:
        rulesetTemplate = json.loads(f.read())

    # Step 1. Create ruleset
    ruleset = d9.create_ruleset(rulesetTemplate)

    # Step 2. Run Assessment
    results = d9.run_assessment(rulesetId=ruleset['id'], cloudAccountId=cloudAccount)

    # Step 3. Delete ruleset
    ruleset = d9.delete_ruleset(ruleset['id'])


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
