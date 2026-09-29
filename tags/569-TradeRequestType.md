[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 569](https://www.onixs.biz/fix-dictionary/4.4/tagNum_569.html)

# FIX 4.4 : TradeRequestType <569> field

**Type:** [int](https://www.onixs.biz/fix-dictionary/4.4/index.html#int)

## Description

Type of [Trade Capture Report <AE>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AE_6569.html).

Valid values:

0 = All trades

1 = Matched trades matching Criteria provided on request (parties, exec id, trade id, order id, instrument, input source, etc.)

2 = Unmatched trades that match criteria

3 = Unreported trades that match criteria

4 = Advisories that match criteria

## Used In

- [Trade Capture Report Request <AD>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AD_6568.html)
- [Trade Capture Report Request Ack <AQ>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AQ_6581.html)

