# WTSS

The Web Time Series Service (WTSS) is a lightweight web service for handling time series data from remote sensing imagery.

## Documentation

In order to generate WTSS documentation, go to directory `docs` and run `Makefile`:

```bash
cd docs
make html
```

After that, you can serve these HTML files with command:

```bash
cd build/html
# Python 3
python -m http.server
```

Open web browser http://127.0.0.1:8000