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
python manage.py run
```

## Tests

In order to run tests, use the following command:

```bash
python manage.py test
```

or

```bash
python -m pytest -v --cov-report html --cov-report annotate --cov=bdc_wtss tests/
```

It will generate folder `htmlcov` with code coverage. You can serve these files through web server. You can also
check locally with the command:

```bash
cd htmlcov
# For Python 3
python -m http.server
```

Access the web browser the url: http://127.0.0.1:8000


## Documentation

In order to generate WTSS documentation, go to directory `docs` and run `Makefile`:

```bash
python manage.py docs
```

or

```bash
cd docs
make html
```

After that, you can serve these HTML files with command:

```bash
cd build/html
# Python 3
python -m http.server 5001
```

You can also pass `--serve` flag to run local HTTP Server listening on 0.0.0.0:5001. The port can be changed with `--port=NewPort`

```bash
python manage.py docs --serve
```

Open web browser http://127.0.0.1:5001

## Docker

You can configure the environment to run through Docker containers. In order to do that, build the image `brazildatacube/wtss:0.1`:

```bash
docker build --tag brazildatacube/wtss:0.1 -f docker/Dockerfile .
```

After that, you can run the application with command:

```bash
docker run --interactive \
           --tty \
           --detach \
           --name wtss_app \
           --publish 5000:5000 \
           brazildatacube/wtss:0.1
```

You can also generate the documentation on `http://localhost:5001`:

```bash
docker run --rm \
           --interactive \
           --name wtss_docs \
           --publish 5001:5001 \
           brazildatacube/wtss:0.1 \
           python3 manage.py docs --serve
```

And run the tests:

```bash
docker run --rm \
           --interactive \
           --name wtss_docs \
           brazildatacube/wtss:0.1 \
           python3 manage.py test
```