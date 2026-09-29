[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 388](https://www.onixs.biz/fix-dictionary/4.4/tagNum_388.html)

# FIX 4.4 : DiscretionInst <388> field

**Type:** [char](https://www.onixs.biz/fix-dictionary/4.4/index.html#char)

## Description

Code to identify the price a [DiscretionOffsetValue <389>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_389.html) is related to and should be mathematically added to.

Valid values:

0 = Related to displayed price

1 = Related to market price

2 = Related to primary price

3 = Related to local primary price

4 = Related to midpoint price

5 = Related to last trade price

6 = Related to VWAP

## Used In

- [<DiscretionInstructions>](https://www.onixs.biz/fix-dictionary/4.4/compBlock_DiscretionInstructions.html)

