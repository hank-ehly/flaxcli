# flaxcli

Programmatically search a body of text for frequently used phrases (or "collocations"). Uses [FLAX](http://flax.nzdl.org/greenstone3/flax?a=fp&sa=collAbout&c=collocations&if=flax) library.

```python
from flaxcli import FlaxCli

client = FlaxCli()
collocations = client.query_text('He is a highly individualistic actor who speaks with a southern dialect.')

# output: ['southern dialect', 'highly individualistic']
```