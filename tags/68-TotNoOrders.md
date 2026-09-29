[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 68](https://www.onixs.biz/fix-dictionary/4.4/tagNum_68.html)

# FIX 4.4 : TotNoOrders <68> field

**Type:** [int](https://www.onixs.biz/fix-dictionary/4.4/index.html#int)

## Description

Total number of list order entries across all messages. Should be the sum of all [NoOrders <73>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_73.html) in each message that has repeating list order entries related to the same [ListID <66>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_66.html). Used to support fragmentation.

(Prior to FIX 4.2 this field was named "ListNoOrds")

## Used In

- [New Order List <E>](https://www.onixs.biz/fix-dictionary/4.4/msgType_E_69.html)
- [List Status <N>](https://www.onixs.biz/fix-dictionary/4.4/msgType_N_78.html)

