[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 87](https://www.onixs.biz/fix-dictionary/4.4/tagNum_87.html)

# FIX 4.4 : AllocStatus <87> field

**Type:** [int](https://www.onixs.biz/fix-dictionary/4.4/index.html#int)

## Description

Identifies status of allocation.

Valid values:

0 = accepted (successfully processed)

1 = block level reject

2 = account level reject

3 = received (received, not yet processed)

4 = incomplete

5 = rejected by intermediary

## Used In

- [Allocation Report <AS>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AS_6583.html)
- [Allocation Report Ack <AT>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AT_6584.html)
- [Allocation Instruction Ack <P>](https://www.onixs.biz/fix-dictionary/4.4/msgType_P_80.html)

