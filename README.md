## climetlab-mltc-surface-observation-postprocessing

A dataset plugin for climetlab for the dataset mltc-surface-observation-postprocessing-main.


Features
--------

In this README is a description of how to get the dataset provided by the python package climetlab_mltc_surface_observation_postprocessing.

## Datasets description

The dataset is designed for learning forecast errors of 2m-temperature from a weather forecasting model, using station observations as the truth. Currently there are 3 variables in the dataset. For each variable the dataset contains over 5 million datapoints covering a range of different locations (not specified).

### 1 : `field = forecast_error`
The predictand for the problem, the difference between the forecasted value of 2m-temperature and the observed value, units degrees C (or equally Kelvin).

### 2 : `field = time_of_day`
Local time of day, in decimal hours. Useful for diagnosing the diurnal cycle model bias.

### 3: `field = soil_temperature`
Model soil temperature, units degrees C.


## Using climetlab to access the data

See the [demo notebooks](https://github.com/mchantry/climetlab-mltc-surface-observation-postprocessing/tree/main/notebooks)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/mchantry/climetlab-mltc-surface-observation-postprocessing/main?urlpath=lab)


- [demo_main.ipynb](https://github.com/mchantry/climetlab-mltc-surface-observation-postprocessing/tree/main/notebooks/demo_main.ipynb)
[![nbviewer](https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg)](https://nbviewer.jupyter.org/github/mchantry/climetlab-mltc-surface-observation-postprocessing/blob/main/notebooks/demo_main.ipynb) 
[![Open in colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mchantry/climetlab-mltc-surface-observation-postprocessing/blob/main/notebooks/demo_main.ipynb) 
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/mchantry/climetlab-mltc-surface-observation-postprocessing/main?filepath=notebooks/demo_main.ipynb)
[<img src="https://deepnote.com/buttons/launch-in-deepnote-small.svg">](https://deepnote.com/launch?name=MyProject&url=https://github.com/mchantry/climetlab-mltc-surface-observation-postprocessing/tree/main/notebooks/demo_main.ipynb)


- TODO.


The climetlab python package allows easy access to the data with a few lines of code such as:
``` python

!pip install climetlab climetlab-mltc-surface-observation-postprocessing
import climetlab as cml
ds = cml.load_dataset("mltc-surface-observation-postprocessing", field="forecast_error")
ds.to_pandas()
```


Support and contributing
------------------------

Either open a issue on github if this is a github repository, or send an email to email@example.com.

LICENSE
-------

See the LICENSE file.
(C) Copyright 2022 European Centre for Medium-Range Weather Forecasts.
This software is licensed under the terms of the Apache Licence Version 2.0
which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
In applying this licence, ECMWF does not waive the privileges and immunities
granted to it by virtue of its status as an intergovernmental organisation
nor does it submit to any jurisdiction.

Authors
-------

Matthew Chantry, Fenwick Cooper, Zied Ben Bouallegue, Peter Dueben

See also the CONTRIBUTORS.md file.
