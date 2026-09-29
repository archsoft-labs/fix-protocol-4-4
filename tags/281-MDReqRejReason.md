[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 281](https://www.onixs.biz/fix-dictionary/4.4/tagNum_281.html)

# FIX 4.4 : MDReqRejReason <281> field

**Type:** [char](https://www.onixs.biz/fix-dictionary/4.4/index.html#char)

## Description

Reason for the rejection of a [MarketDataRequest <V>](https://www.onixs.biz/fix-dictionary/4.4/msgType_V_86.html).

Valid values:

0 = Unknown symbol

1 = Duplicate [MDReqID <262>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_262.html)

2 = Insufficient Bandwidth

3 = Insufficient Permissions

4 = Unsupported [SubscriptionRequestType <263>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_263.html)

5 = Unsupported [MarketDepth <264>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_264.html)

6 = Unsupported [MDUpdateType <265>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_265.html)

7 = Unsupported [AggregatedBook <266>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_266.html)

8 = Unsupported [MDEntryType <269>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_269.html)

9 = Unsupported [TradingSessionID <336>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_336.html)

A = Unsupported [Scope <546>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_546.html)

B = Unsupported [OpenCloseSettlFlag <286>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_286.html)

C = Unsupported [MDImplicitDelete <547>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_547.html)

## Used In

- [Market Data Request Reject <Y>](https://www.onixs.biz/fix-dictionary/4.4/msgType_Y_89.html)

