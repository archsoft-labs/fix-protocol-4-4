[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 844](https://www.onixs.biz/fix-dictionary/4.4/tagNum_844.html)

# FIX 4.4 : DiscretionRoundDirection <844> field

**Type:** [int](https://www.onixs.biz/fix-dictionary/4.4/index.html#int)

## Description

If the calculated discretionary price is not a valid tick price, specifies whether to round the price to be more or less aggressive

Valid values:

1 = More aggressive - on a buy order round the price up round up to the nearest tick, on a sell round down to the nearest tick

2 = More passive - on a buy order round down to nearest tick on a sell order round up to nearest tick

## Used In

- [<DiscretionInstructions>](https://www.onixs.biz/fix-dictionary/4.4/compBlock_DiscretionInstructions.html)

