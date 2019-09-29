# Dome9 SDK



## Usage

```python
from dome9sdk import Dome9SDK

dome9 = Dome9SDK(key='xxxxxx', secret='yyyyyyy')

rulesets = dome9.list_rulesets()
```



## Authentication

There are two ways to authenticate Dome9SDK:
* **SDK Arguments**: Passing variables to Dome9SDK `Dome9SDK(key='xxxxxx', secret='yyyyyyy')`
* **Environment variables**: Setting your credentials to `DOME9_ACCESS_KEY` and `DOME9_SECRET_KEY` environment variables

Example: 
```bash
export DOME9_ACCESS_KEY='xxxxxxxxxxxxxxxxxxxx'
export DOME9_SECRET_KEY='yyyyyyyyyyyyyyyyyyyy'
echo -e "import dome9sdk \nprint(dome9sdk.Dome9SDK().list_cloud_accounts())" | python
```



## Agile

```python
import json
from dome9sdk import Dome9SDK

cloudAccount = '00000-00000-00000-00000'

dome9 = Dome9SDK()

rulesetTemplate = {}
with open('ruleset','r') as f:
    rulesetTemplate = json.loads(f.read())

# Step 1. Create ruleset
ruleset = dome9.create_ruleset(rulesetTemplate)

# Step 2. Run Assessment
results = dome9.run_assessment(rulesetId=ruleset['id'], cloudAccountId=cloudAccount)

# Step 3. Delete ruleset
ruleset = dome9.delete_ruleset(ruleset['id'])

```