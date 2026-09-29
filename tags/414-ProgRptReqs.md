[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 414](https://www.onixs.biz/fix-dictionary/4.4/tagNum_414.html)

# FIX 4.4 : ProgRptReqs <414> field

**Type:** [int](https://www.onixs.biz/fix-dictionary/4.4/index.html#int)

## Description

Code to identify the desired frequency of progress reports.

Valid values:

1 = BuySide explicitly requests status using StatusRequest (Default) The sell-side firm can however, send a DONE status [List Status <N>](https://www.onixs.biz/fix-dictionary/4.4/msgType_N_78.html) Response in an unsolicited fashion

2 = SellSide periodically sends status using ListStatus. Period optionally specified in ProgressPeriod

3 = Real-time execution reports (to be discouraged)

## Used In

- [New Order List <E>](https://www.onixs.biz/fix-dictionary/4.4/msgType_E_69.html)
- [Bid Request <k>](https://www.onixs.biz/fix-dictionary/4.4/msgType_k_107.html)

