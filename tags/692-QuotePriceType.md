[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 692](https://www.onixs.biz/fix-dictionary/4.4/tagNum_692.html)

# FIX 4.4 : QuotePriceType <692> field

**Type:** [int](https://www.onixs.biz/fix-dictionary/4.4/index.html#int)

## Description

Code to represent price type requested in Quote.

If the [Quote Request <R>](https://www.onixs.biz/fix-dictionary/4.4/msgType_R_82.html) is for a Swap values 1-8 apply to all legs.

Valid values:

1 = percent (percent of par)

2 = per share (e.g. cents per share)

3 = fixed amount (absolute value)

4 = discount - percentage points below par

5 = premium - percentage points over par

6 = basis points relative to benchmark

7 = TED price

8 = TED yield

9 = Yield spread (swaps)

10 = Yield

## Used In

- [Quote Request Reject <AG>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AG_6571.html)
- [Quote Request <R>](https://www.onixs.biz/fix-dictionary/4.4/msgType_R_82.html)

