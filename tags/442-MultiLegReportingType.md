[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 442](https://www.onixs.biz/fix-dictionary/4.4/tagNum_442.html)

# FIX 4.4 : MultiLegReportingType <442> field

**Type:** [char](https://www.onixs.biz/fix-dictionary/4.4/index.html#char)

## Description

Used to indicate what an [Execution Report <8>](https://www.onixs.biz/fix-dictionary/4.4/msgType_8_8.html) represents (e.g. used with multi-leg securities, such as option strategies, spreads, etc.).

Valid values:

1 = Single Security (default if not specified)

2 = Individual leg of a multi-leg security

3 = Multi-leg security

## Used In

- [Execution Report <8>](https://www.onixs.biz/fix-dictionary/4.4/msgType_8_8.html)
- [Trade Capture Report Request <AD>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AD_6568.html)
- [Trade Capture Report <AE>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AE_6569.html)
- [Trade Capture Report Request Ack <AQ>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AQ_6581.html)

