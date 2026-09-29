[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 102](https://www.onixs.biz/fix-dictionary/4.4/tagNum_102.html)

# FIX 4.4 : CxlRejReason <102> field

**Type:** [int](https://www.onixs.biz/fix-dictionary/4.4/index.html#int)

## Description

Code to identify reason for cancel rejection.

Valid values:

0 = Too late to cancel

1 = Unknown order

2 = Broker / Exchange Option

3 = Order already in Pending Cancel or Pending Replace status

4 = Unable to process [Order Mass Cancel Request <q>](https://www.onixs.biz/fix-dictionary/4.4/msgType_q_113.html)

5 = [OrigOrdModTime <586>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_586.html) did not match last [TransactTime <60>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_60.html) of order

6 = Duplicate [ClOrdID <11>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_11.html) received

99 = Other

## Used In

- [Order Cancel Reject <9>](https://www.onixs.biz/fix-dictionary/4.4/msgType_9_9.html)

