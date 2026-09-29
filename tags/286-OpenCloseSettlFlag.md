[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 286](https://www.onixs.biz/fix-dictionary/4.4/tagNum_286.html)

# FIX 4.4 : OpenCloseSettlFlag <286> field

**Type:** [MultipleValueString](https://www.onixs.biz/fix-dictionary/4.4/index.html#MultipleValueString)

## Description

Flag that identifies a market data entry.

Valid values:

0 = Daily Open / Close / Settlement entry

1 = Session Open / Close / Settlement entry

2 = Delivery Settlement entry

3 = Expected entry

4 = Entry from previous business day

5 = Theoretical Price value

(Prior to FIX 4.3 this field was of type [char](https://www.onixs.biz/fix-dictionary/4.4/index.html#char))

## Used In

- [Market Data Request <V>](https://www.onixs.biz/fix-dictionary/4.4/msgType_V_86.html)
- [Market Data - Snapshot/Full Refresh <W>](https://www.onixs.biz/fix-dictionary/4.4/msgType_W_87.html)
- [Market Data - Incremental Refresh <X>](https://www.onixs.biz/fix-dictionary/4.4/msgType_X_88.html)

