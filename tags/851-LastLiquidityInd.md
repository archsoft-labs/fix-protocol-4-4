[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 851](https://www.onixs.biz/fix-dictionary/4.4/tagNum_851.html)

# FIX 4.4 : LastLiquidityInd <851> field

**Type:** [int](https://www.onixs.biz/fix-dictionary/4.4/index.html#int)

## Description

Indicator to identify whether this fill was a result of a liquidity provider providing or liquidity taker taking the liquidity. Applicable only for [OrdStatus <39>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_39.html) of 'Partial' or 'Filled'.

Valid values:

1 = Added Liquidity

2 = Removed Liquidity

3 = Liquidity Routed Out

## Used In

- [Execution Report <8>](https://www.onixs.biz/fix-dictionary/4.4/msgType_8_8.html)

