# Goco
[![Build Status](https://api.travis-ci.org/elmoiv/goco.svg?branch=master)](https://travis-ci.org/elmoiv/goco)
[![Python version](https://img.shields.io/badge/python-3.6-blue.svg)](https://pypi.org/project/goco/)

Connecting to Google apis has never been easier!

## Features
* Easy and Fast connection to google apis
* Auto-renewable access token

## Installation
`goco` requires Python 3.

Use `pip` to install the package from PyPI:

```bash
pip install goco
```

Or, install the latest version of the package from GitHub:

```bash
pip install git+https://github.com/elmoiv/goco.git
```

## Usage
Using goco to connect to blogger:

```python
# Blogger example
from goco import Goco

GoogleApi = Goco("path\\to\\client_secret.json", "path\\to\\credentials.storage")
MyBlog = GoogleApi.connect(scope='Blogger', service_name='blogger', version='v3')
Posts = MyBlog.posts().list(blogId='7599400532066909387').execute()
print(Posts)
```

## Tests
Here are a few sample tests:

* [Test1](https://github.com/elmoiv/sdelmo/tree/master/tests/test1.py)

## Contributing
Please contribute! If you want to fix a bug, suggest improvements, or add new features to the project, just [open an issue](https://github.com/elmoiv/goco/issues) or send me a pull request.
