# NHTSA API

This is the **NHTSA-python**, a Python client for accessing the
NHTSA's API complete with objects.

## Development

This application is currently not in a stable enough state to be published, but if you are interested and would like to contribute, the code is available on the `dev` branch in the meantime.

## Installation

This application is still in development, and is not yet available on PyPI ye

## Examples

### Civil Penalties

These API endings are used for getting information about the total value of civil penalties that the NHTSA incurred upon car manufacturers for legal violations (delaying a recall/not reporting an issue in a timely manner).

```python
client = NHTSAClient()

penalties = client.penalties(2016)  # Get penalties for the 2016 fiscal year
penalty = penalties[0]

print(penalty)
# <Penalty [TQ10-007,$1500000]: 'Volvo'>

print(penalty.id)
# 'TQ10-007'

print(penalty.amount)
# 1500000

print(penalty.company)
# 'Volvo'
```

### Vehicle Crash Ratings

Looks up the vehicle crash ratings for a particular year model.

```python
client = NHTSAClient()
variants = client.get_model_variants('2009', 'Toyota', 'Prius')

variant = variants[0] # [] => nhtsa.data.ModelVariant
ratings = client.ratings(variant.id)

print(ratings[0])
# <VehicleRating[5346]: '2009 Toyota Prius 4-DR.w/SAB'>
```

## License

The MIT License (MIT)

Copyright (c) 2016 Evan Darwin

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

**THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.**