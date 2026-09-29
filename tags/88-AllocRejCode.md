[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 88](https://www.onixs.biz/fix-dictionary/4.4/tagNum_88.html)

# FIX 4.4 : AllocRejCode <88> field

**Type:** [int](https://www.onixs.biz/fix-dictionary/4.4/index.html#int)

## Description

Identifies reason for rejection.

Valid values:

0 = unknown account(s)

1 = incorrect quantity

2 = incorrect average price

3 = unknown executing broker mnemonic

4 = commission difference

5 = unknown [OrderID <37>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_37.html)

6 = unknown [ListID <66>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_66.html)

7 = other (further in [Text <58>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_58.html))

8 = incorrect allocated quantity

9 = calculation difference

10 = unknown or stale [ExecID <17>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_17.html)

11 = mismatched data value (further in [Text <58>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_58.html))

12 = unknown [ClOrdID <11>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_11.html)

13 = warehouse request rejected

## Used In

- [Allocation Report <AS>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AS_6583.html)
- [Allocation Report Ack <AT>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AT_6584.html)
- [Allocation Instruction Ack <P>](https://www.onixs.biz/fix-dictionary/4.4/msgType_P_80.html)

