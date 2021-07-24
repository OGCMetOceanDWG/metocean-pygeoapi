# =================================================================
#
# Authors: Tom Kralidis <tomkralidis@gmail.com>
#
# Copyright (c) 2021 Tom Kralidis
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
# =================================================================

from datetime import datetime, timedelta
import logging
import math
from urllib.parse import unquote

import requests

from pygeoapi.process.base import BaseProcessor

LOGGER = logging.getLogger(__name__)

TODAY = datetime.today().strftime('%Y-%m-%d')
TOMORROW = (datetime.now() + timedelta(1)).strftime('%Y-%m-%d')

EDR_API_URL = 'https://data-api.mdl.nws.noaa.gov/EDR-API/collections/automated_gfs_100_forecast_time0_lat_0_lon_0_lv_ISBL5_Isobaric_surface_Pa/instance/00z/cube'  # noqa

#: Process metadata and description
PROCESS_METADATA = {
    'version': '0.1.0',
    'id': 'edr-wind-calculator-demo',
    'title': 'Wind speed and direction calculator demo',
    'description': 'Wind speed and direction calculator demo',
    'keywords': ['edr', 'wind speed', 'wind direction', 'calculator'],
    'links': [{
        'type': 'text/html',
        'rel': 'canonical',
        'title': 'information',
        'href': 'https://disc.gsfc.nasa.gov/information/data-in-action?title=Derive%20Wind%20Speed%20and%20Direction%20With%20MERRA-2%20Wind%20Components',  # noqa
        'hreflang': 'en-US'
    }],
    'inputs': {
        'wkt': {
            'title': 'OGC Well-known text',
            'schema': {
                'type': 'string'
            },
            'minOccurs': 1,
            'maxOccurs': 1
        },
        'datetime': {
            'title': 'datetime (RFC3339)',
            'schema': {
                'type': 'string',
                'format': 'date-time'
            },
            'minOccurs': 1,
            'maxOccurs': 1
        },
        'z': {
            'title': 'z',
            'schema': {
                'type': 'number',
            },
            'minOccurs': 1,
            'maxOccurs': 1
        }
    },
    'outputs': {
        'edr-wind-calculator-demo-response': {
            'title': 'EDR wind calculator demo output',
            'schema': {
                'type': 'object',
                'contentEncodingType': 'application/json'
            }
        }
    },
    'example': {
        'inputs': {
            'wkt': 'POLYGON((-120.504906 36.031332,-120.504906 46.980252,-83.692291 46.980252,-83.692291 36.031332,-120.504906 36.031332))',  # noqa
            'datetime': f'{TODAY}T00:00:00/{TOMORROW}T21:00:00',
            'z': '50000.0'
        }
    }
}


class WindCalculatorDemoProcessor(BaseProcessor):
    """Wind calculator demo processor"""

    def __init__(self, provider_def):
        """
        Initialize object

        :param provider_def: provider definition

        :returns: pygeoapi.process.wind_calculator_demo.wind_calculator_demo.WindCalculatorDemoProcessor  # noqa
        """

        BaseProcessor.__init__(self, provider_def, PROCESS_METADATA)

    def execute(self, data):
        params = {
            'coords': unquote(data['wkt']),
            'datetime': data['datetime'],
            'z': data['z'],
            'parametername': 'UGRD_P0_L100_GLL0,VGRD_P0_L100_GLL0',
            'f': 'CoverageJSON'
        }

        LOGGER.debug('Accessing U/V data from NOAA EDR API')
        response = requests.get(EDR_API_URL, params=params)
        LOGGER.debug('request URL: {}'.format(response.url))

        d = response.json()

        parameter_wind_speed = {
            'description': {
                'en': 'derived wind speed'
            },
            'observedProperty': {
                'label': {
                    'en': 'derived wind speed'
                }
            },
            'unit': {
                'label': {
                    'en': 'derived wind speed'
                },
                'symbol': {
                    'value': 'mph'
                }
            }
        }
        parameter_wind_direction = {
            'description': {
                'en': 'derived wind direction'
            },
            'observedProperty': {
                'label': {
                    'en': 'derived wind direction'
                }
            },
            'unit': {
                'label': {
                    'en': 'derived wind direction'
                },
                'symbol': {
                    'value': 'degrees'
                }
            }
        }

        output = []

        LOGGER.debug('Calculating wind speed and direction for all values')
        for u, v in zip(d['ranges']['UGRD_P0_L100_GLL0']['values'], d['ranges']['VGRD_P0_L100_GLL0']['values']):  # noqa
            wind_speed = math.sqrt(u*u + v*v)
            wind_direction = math.atan(u/v)
            output.append(((wind_speed, wind_direction)))

        return output

    def __repr__(self):
        return '<WindCalculatorDemoProcessor> {}'.format(self.name)
