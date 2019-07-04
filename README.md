# WTSS

The Web Time Series Service (WTSS) is a lightweight web service for handling time series data from remote sensing imagery.

## Installation

### Requirements

- [`Python 3+`](https://python.org)

Install [`WTSS requirements.txt`](./requirements.txt) with the following command:

```bash
pip install -r requirements.txt
```

## Running

Run WTSS application with command:

```bash
python manager.py run
```

## Tests

In order to run tests, use the following command:

```bash
python -m pytest -v --cov-report html --cov-report annotate --cov=bdc_wtss tests/
```

It will generate folder `htmlcov` with code coverage. You can serve these files through web server. You can also
check locally with the command:

```bash
cd htmlcov
# For Python 3
python -m http.server
# Python 2
python -m SimpleHTTPServer
```

Access the web browser the url: http://127.0.0.1:8000