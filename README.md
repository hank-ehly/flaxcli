# flaxcli

Programmatically search a body of text for recurrent, semi-fixed combinations of words (aka "collocations"). Uses [FLAX](http://flax.nzdl.org/greenstone3/flax?a=fp&sa=collAbout&c=collocations&if=flax) library.

```python
from flaxcli import FlaxCli

client = FlaxCli()
collocations = client.query_text('He is a highly individualistic actor who speaks with a southern dialect.')

# output: ['southern dialect', 'highly individualistic']
```

### License

The MIT License (MIT)

Copyright (c) 2018 Hank Ehly

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.