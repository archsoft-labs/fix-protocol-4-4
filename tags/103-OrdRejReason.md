[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 103](https://www.onixs.biz/fix-dictionary/4.4/tagNum_103.html)

# FIX 4.4 : OrdRejReason <103> field

**Type:** [int](https://www.onixs.biz/fix-dictionary/4.4/index.html#int)

## Description

Code to identify reason for order rejection.

Valid values:

0 = Broker / Exchange option

1 = Unknown symbol

2 = Exchange closed

3 = Order exceeds limit

4 = Too late to enter

5 = Unknown Order

6 = Duplicate Order (e.g. dupe [ClOrdID <11>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_11.html))

7 = Duplicate of a verbally communicated order

8 = Stale Order

9 = Trade Along required

10 = Invalid Investor ID

11 = Unsupported order characteristic

12 = Surveillence Option

13 = Incorrect quantity

14 = Incorrect allocated quantity

15 = Unknown account(s)

99 = Other

Note: Values 3, 4, and 5 will be used when rejecting an order due to pre-allocation information errors.

## Used In

- [Execution Report <8>](https://www.onixs.biz/fix-dictionary/4.4/msgType_8_8.html)
- [List Status <N>](https://www.onixs.biz/fix-dictionary/4.4/msgType_N_78.html)

