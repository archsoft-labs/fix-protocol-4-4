[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 892](https://www.onixs.biz/fix-dictionary/4.4/tagNum_892.html)

# FIX 4.4 : TotNoAllocs <892> field

**Type:** [int](https://www.onixs.biz/fix-dictionary/4.4/index.html#int)

## Description

Total number of NoAlloc entries across all messages. Should be the sum of all [NoAllocs <78>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_78.html) in each message that has repeating NoAlloc entries related to the same [AllocID <70>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_70.html) or [AllocReportID <755>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_755.html). Used to support fragmentation.

## Used In

- [Allocation Report <AS>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AS_6583.html)
- [Allocation Instruction <J>](https://www.onixs.biz/fix-dictionary/4.4/msgType_J_74.html)

