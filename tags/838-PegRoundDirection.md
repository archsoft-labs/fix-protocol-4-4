[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 838](https://www.onixs.biz/fix-dictionary/4.4/tagNum_838.html)

# FIX 4.4 : PegRoundDirection <838> field

**Type:** [int](https://www.onixs.biz/fix-dictionary/4.4/index.html#int)

## Description

If the calculated peg price is not a valid tick price, specifies whether to round the price to be more or less aggressive

Valid values:

1 = More aggressive - on a buy order round the price up round up to the nearest tick, on a sell round down to the nearest tick

2 = More passive - on a buy order round down to nearest tick on a sell order round up to nearest tick

## Used In

- [<PegInstructions>](https://www.onixs.biz/fix-dictionary/4.4/compBlock_PegInstructions.html)

