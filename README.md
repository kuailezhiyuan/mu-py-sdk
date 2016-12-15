# mu-py-sdk
ss-panel mu api py sdk

# Install

```
pip install musdk
```

# Example

```
from musdk import client


def init_mu_client():
    mu_url = "http://example.com/mu"
    mu_token = "ThisNotToken"
    mu_client = client.Client(mu_url, mu_token)

``
