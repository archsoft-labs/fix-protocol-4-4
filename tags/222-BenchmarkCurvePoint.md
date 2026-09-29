[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 222](https://www.onixs.biz/fix-dictionary/4.4/tagNum_222.html)

# FIX 4.4 : BenchmarkCurvePoint <222> field

**Type:** [String](https://www.onixs.biz/fix-dictionary/4.4/index.html#String)

## Description

Point on benchmark curve. Free form values: e.g. "1Y", "7Y", "INTERPOLATED".

Sample values:

1M = combination of a number between 1-12 and a "M" for month

1Y = combination of number between 1-100 and a "Y" for year

10Y-OLD = see above, then add "-OLD" when appropriate

INTERPOLATED = the point is mathematically derived

2/2031 5 3/8 = the point is stated via a combination of maturity month / year and coupon

See Fixed Income-specific documentation at [www.fixtrading.org](https://www.fixtrading.org/) for additional values.

(Note tag # was reserved in FIX 4.1, added in FIX 4.3)

## Used In

- [<SpreadOrBenchmarkCurveData>](https://www.onixs.biz/fix-dictionary/4.4/compBlock_SpreadOrBenchmarkCurveData.html)

