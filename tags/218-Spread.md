[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 218](https://www.onixs.biz/fix-dictionary/4.4/tagNum_218.html)

# FIX 4.4 : Spread <218> field

**Type:** [PriceOffset](https://www.onixs.biz/fix-dictionary/4.4/index.html#PriceOffset)

## Description

For Fixed Income. Either Swap Spread or Spread to Benchmark depending upon the order type.

Spread to Benchmark: Basis points relative to a benchmark. To be expressed as "count of basis points" (vs. an absolute value). E.g. High Grade Corporate Bonds may express price as basis points relative to benchmark (the [BenchmarkCurveName <221>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_221.html) field). Note: Basis points can be negative.

Swap Spread: Target spread for a swap.

## Used In

- [<SpreadOrBenchmarkCurveData>](https://www.onixs.biz/fix-dictionary/4.4/compBlock_SpreadOrBenchmarkCurveData.html)

