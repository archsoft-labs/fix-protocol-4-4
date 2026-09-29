[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 857](https://www.onixs.biz/fix-dictionary/4.4/tagNum_857.html)

# FIX 4.4 : AllocNoOrdersType <857> field

**Type:** [int](https://www.onixs.biz/fix-dictionary/4.4/index.html#int)

## Description

Indicates how the orders being booked and allocated by an [Allocation Instruction <J>](https://www.onixs.biz/fix-dictionary/4.4/msgType_J_74.html) or [Allocation Report <AS>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AS_6583.html) message are identified, i.e. by explicit definition in the [NoOrders <73>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_73.html) group or not.

Valid values:

0 = Not specified

1 = Explicit list provided

## Used In

- [Allocation Report <AS>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AS_6583.html)
- [Allocation Instruction <J>](https://www.onixs.biz/fix-dictionary/4.4/msgType_J_74.html)

