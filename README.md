# Withings API

Python version of the Withings API.

## Usage

Example usage to get body measurements:

```python
from withings_api import withings
from withings_api.api.measure.measure_getmeas import sync as measure_getmeas
import datetime

today = datetime.datetime.now().date()
start = datetime.datetime(today.year, today.month, today.day)
end = start + datetime.timedelta(days=1)

w = withings.create_local_api_wrapper()
m = w(measure_getmeas)(
    action="getmeas",
    meastype=1,
    meastypes="1,5,8,76,77,88",
    category=1,
    startdate=int(start.timestamp()),
    enddate=int(end.timestamp()),
)
print(m)


```

## Docs

See [Withings API](https://developer.withings.com/).
