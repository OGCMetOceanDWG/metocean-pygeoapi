# Wind speed and direction processing plugin

## Overview

This OAProc plugin demo queries the NOAA EDR API for U and V values and
calculates wind speed and direction.

## Data

No data setup is required given all inputs are from remote APIs.

## Dependencies

* [requests](https://requests.readthedocs.io)

## Installation

```bash
# install requests as per your environment (conda, pip, apt, etc.)
# for simplicity, here we will use pip
pip3 install requests

# install metocean_pygeoapi
python3 setup.py install
```

## Configuration

```yaml
wind-calculator-demo:
    type: process
    processor:
        name: metocean_pygeoapi.process.wind_calculator_demo.wind_calculator_demo.WindCalculatorDemoProcessor
```

## Integration

```bash
pygeoapi generate-openapi-document -c $PYGEOAPI_CONFIG > $PYGEOAPI_OPENAPI
```

## Running

```bash
# start pygeoapi
pygeoapi serve

# URLs to open in web browser or console

# Swagger document
http://localhost:5000/openapi

# process description
http://localhost:5000/processes/wind-calculator-demo
```

## Contact

* [Tom Kralidis](https://github.com/tomkralidis)
