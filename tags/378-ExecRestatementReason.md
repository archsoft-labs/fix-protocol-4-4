[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 378](https://www.onixs.biz/fix-dictionary/4.4/tagNum_378.html)

# FIX 4.4 : ExecRestatementReason <378> field

**Type:** [int](https://www.onixs.biz/fix-dictionary/4.4/index.html#int)

## Description

Code to identify reason for an [ExecutionRpt <8>](https://www.onixs.biz/fix-dictionary/4.4/msgType_8_8.html) message sent with [ExecType <150>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_150.html)='Restated' or used when communicating an unsolicited cancel.

Valid values:

0 = GT Corporate action

1 = GT renewal / restatement (no corporate action)

2 = Verbal change

3 = Repricing of order

4 = Broker option

5 = Partial decline of [OrderQty <38>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_38.html) (e.g. exchange-initiated partial cancel)

6 = Cancel on Trading Halt

7 = Cancel on System Failure

8 = Market (Exchange) Option

9 = Canceled, Not Best

10 = Warehouse recap

99 = Other

## Used In

- [Execution Report <8>](https://www.onixs.biz/fix-dictionary/4.4/msgType_8_8.html)
- [Trade Capture Report <AE>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AE_6569.html)

