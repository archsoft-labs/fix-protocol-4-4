[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 151](https://www.onixs.biz/fix-dictionary/4.4/tagNum_151.html)

# FIX 4.4 : LeavesQty <151> field

**Type:** [Qty](https://www.onixs.biz/fix-dictionary/4.4/index.html#Qty)

## Description

Quantity open for further execution. If the [OrdStatus <39>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_39.html) is 'Canceled', 'DoneForTheDay', 'Expired', 'Calculated', or' Rejected' (in which case the order is no longer active) then [LeavesQty <151>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_151.html) could be 0, otherwise [LeavesQty <151>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_151.html) = [OrderQty <38>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_38.html) - [CumQty <14>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_14.html).

(Prior to FIX 4.2 this field was of type int)

## Used In

- [Execution Report <8>](https://www.onixs.biz/fix-dictionary/4.4/msgType_8_8.html)
- [List Status <N>](https://www.onixs.biz/fix-dictionary/4.4/msgType_N_78.html)

