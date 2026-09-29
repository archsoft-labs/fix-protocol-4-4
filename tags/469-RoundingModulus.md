[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 469](https://www.onixs.biz/fix-dictionary/4.4/tagNum_469.html)

# FIX 4.4 : RoundingModulus <469> field

**Type:** [float](https://www.onixs.biz/fix-dictionary/4.4/index.html#float)

## Description

For CIV - a float value indicating the value to which rounding is required.

i.e. 10 means round to a multiple of 10 units/shares; 0.5 means round to a multiple of 0.5 units/shares.

The default, if [RoundingDirection <468>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_468.html) is specified without [RoundingModulus <469>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_469.html), is to round to a whole unit/share.

## Used In

- [<OrderQtyData>](https://www.onixs.biz/fix-dictionary/4.4/compBlock_OrderQtyData.html)

