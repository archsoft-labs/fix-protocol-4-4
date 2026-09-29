[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 468](https://www.onixs.biz/fix-dictionary/4.4/tagNum_468.html)

# FIX 4.4 : RoundingDirection <468> field

**Type:** [char](https://www.onixs.biz/fix-dictionary/4.4/index.html#char)

## Description

Specifies which direction to round For CIV - indicates whether or not the quantity of shares/units is to be rounded and in which direction where [CashOrderQty <152>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_152.html) or (for CIV only) [OrderPercent <516>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_516.html) are specified on an order.

Valid values are:

0 = Round to nearest

1 = Round down

2 = Round up

The default is for rounding to be at the discretion of the executing broker or fund manager.

E.g. for an order specifying [CashOrderQty <152>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_152.html) or [OrderPercent <516>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_516.html) if the calculated number of shares/units was 325.76 and [RoundingModulus <469>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_469.html) was 10 - "round down" would give 320 units, "round up" would give 330 units and "round to nearest" would give 320 units.

## Used In

- [<OrderQtyData>](https://www.onixs.biz/fix-dictionary/4.4/compBlock_OrderQtyData.html)

