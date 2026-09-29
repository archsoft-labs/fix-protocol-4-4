[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 725](https://www.onixs.biz/fix-dictionary/4.4/tagNum_725.html)

# FIX 4.4 : ResponseTransportType <725> field

**Type:** [int](https://www.onixs.biz/fix-dictionary/4.4/index.html#int)

## Description

Identifies how the response to the request should be transmitted.

Valid values:

0 = Inband: transport the request was sent over (Default)

1 = Out-of-Band: pre-arranged out of band delivery mechanism (i.e. FTP, HTTP, NDM, etc) between counterparties. Details specified via [ResponseDestination <726>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_726.html).

## Used In

- [Trade Capture Report Request <AD>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AD_6568.html)
- [Request For Positions <AN>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AN_6578.html)
- [Request for Positions Ack <AO>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AO_6579.html)
- [Trade Capture Report Request Ack <AQ>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AQ_6581.html)
- [Trade Capture Report Ack <AR>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AR_6582.html)
- [Collateral Inquiry <BB>](https://www.onixs.biz/fix-dictionary/4.4/msgType_BB_6666.html)
- [Collateral Inquiry Ack <BG>](https://www.onixs.biz/fix-dictionary/4.4/msgType_BG_6671.html)

