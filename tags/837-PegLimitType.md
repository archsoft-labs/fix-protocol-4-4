[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 837](https://www.onixs.biz/fix-dictionary/4.4/tagNum_837.html)

# FIX 4.4 : PegLimitType <837> field

**Type:** [int](https://www.onixs.biz/fix-dictionary/4.4/index.html#int)

## Description

Type of Peg Limit

Valid values:

0 = Or better (default) - price improvement allowed

1 = Strict - limit is a strict limit

2 = Or worse - for a buy the peg limit is a minimum and for a sell the peg limit is a maximum (for use for orders which have a price range)

## Used In

- [<PegInstructions>](https://www.onixs.biz/fix-dictionary/4.4/compBlock_PegInstructions.html)

