[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 424](https://www.onixs.biz/fix-dictionary/4.4/tagNum_424.html)

# FIX 4.4 : DayOrderQty <424> field

**Type:** [Qty](https://www.onixs.biz/fix-dictionary/4.4/index.html#Qty)

## Description

For GT orders, the [OrderQty <38>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_38.html) less all quantity (adjusted for stock splits) that traded on previous days. [DayOrderQty <424>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_424.html) = [OrderQty <38>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_38.html) - ([CumQty <14>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_14.html) - [DayCumQty <425>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_425.html))

## Used In

- [Execution Report <8>](https://www.onixs.biz/fix-dictionary/4.4/msgType_8_8.html)

