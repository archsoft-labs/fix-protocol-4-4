[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 749](https://www.onixs.biz/fix-dictionary/4.4/tagNum_749.html)

# FIX 4.4 : TradeRequestResult <749> field

**Type:** [int](https://www.onixs.biz/fix-dictionary/4.4/index.html#int)

## Description

Result of Trade Request

Valid values:

0 = Successful (Default)

1 = Invalid or unknown instrument

2 = Invalid type of trade requested

3 = Invalid parties

4 = Invalid Transport Type requested

5 = Invalid Destination requested

8 = [TradeRequestType <569>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_569.html) not supported

9 = Unauthorized for [Trade Capture Report Request <AD>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AD_6568.html)

99 = Other

4000+ Reserved and available for bi-laterally agreed upon user-defined values

## Used In

- [Trade Capture Report Request Ack <AQ>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AQ_6581.html)

