#!/usr/bin/env python3

import climetlab as cml
import pandas as pd

from climetlab_maelstrom_yr.yr import Yr

def test_read():
    ds = cml.load_dataset(
        "maelstrom-yr",
        size="5GB",
        dates=["2020-03-01", "2020-03-03"],
        location="files/",
        probabilistic_target=False,
        verbose=True,
    )
    q = ds.to_xarray()


def test_parse_dates():
    expected = ["20210101", "20210102", "20210103"]
    pd_dates = pd.date_range(start="2021-01-01", end="2021-01-03", freq="1D")
    assert Yr.parse_dates(pd_dates) == expected
    assert Yr.parse_dates(["2021-01-01", "2021-01-02", "2021-01-03"]) == expected


if __name__ == "__main__":
    from climetlab.testing import main

    test_read()
    test_parse_dates()
