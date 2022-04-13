#!/usr/bin/env python3
# (C) Copyright 2022 European Centre for Medium-Range Weather Forecasts.
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.

import climetlab as cml


def test_read():
    ds = cml.load_dataset(
        "mltc-surface-observation-postprocessing",
        field="soil_temperature",
    )
    xds = ds.to_pandas()
    print(xds)


if __name__ == "__main__":
    test_read()
