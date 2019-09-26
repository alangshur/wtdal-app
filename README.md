# mind-engine

## Dependencies

The following dependencies are required for developing this project:

- Python 3.7.*: `$ brew install python3`
- Falcon: `$ pip3 install falcon`
- Cython: `$ pip3 install cython`
- Cython-Falcon integration: `pip3 install --no-binary :all: falcon`
- Gunicorn: `$ pip3 install gunicorn`

## Building

To launch the application locally, run the following commnand: `$ gunicorn wtdal.app`
