[![Join the chat at https://gitter.im/OGCMetOceanDWG/Lobby](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/OGCMetOceeanDWG/Lobby)

# metocean-pygeoapi

[metocean-pygeoapi](https://github.com/OGCMetOceanDWG/metocean-pygeoapi) provides MetOcean
specific plugins for the [pygeoapi](https://pygeoapi.io) project.


```
+-----------------+       +--------------------------+
|                 |       |                          |
|                 |       |   metocean-pygeoapi      |
|                 |       |   -----------------      |
|    pygeoapi     | <---> |                          |
|    --------     |       |   - EDR providers        |
|                 |       |   - processes            |
|                 |       |   - providers (features, |
|                 |       |     coverages)           |
+-----------------+       |   - records/metadata     |
                          |                          |
                          +--------------------------+
```


## Installation

### Requirements

* Python 3 and above
* Python [virtualenv](https://virtualenv.pypa.io) package

### Dependencies

Dependencies are listed in [requirements.txt](requirements.txt). Dependencies
are automatically installed during metocean-pygeoapi's installation.

### Installing the Package

```bash
# install pygeoapi as per https://docs.pygeoapi.io/en/latest/installation.html
...
# install metocean-pygeoapi
python3 -m venv my-env
cd my-env
. bin/activate
git clone https://github.com/OGCMetOceanDWG/metocean-pygeoapi.git
cd metocean-pygeoapi
python3 setup.py build
python3 setup.py install
```

## Running

Plugins can be integrated via the standard pygeoapi
[plugin integration](https://docs.pygeoapi.io/en/latest/plugins.html) mechanism

## Development

### Setting up a Development Environment

Same as installing a package.  Use a virtualenv.  Also install developer
requirements:

```bash
pip3 install -r requirements-dev.txt
```

### Code Conventions

* [PEP8](https://www.python.org/dev/peps/pep-0008)

### Bugs and Issues

All bugs, enhancements and issues are managed on [GitHub](https://github.com/OGCMetOceanDWG/metocean-pygeoapi)

## Contact

* [ OGC Meteorology and Oceanography Domain Working Group](https://github.com/OGCMetOceanDWG)
