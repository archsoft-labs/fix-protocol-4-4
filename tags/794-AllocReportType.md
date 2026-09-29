[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 794](https://www.onixs.biz/fix-dictionary/4.4/tagNum_794.html)

# FIX 4.4 : AllocReportType <794> field

**Type:** [int](https://www.onixs.biz/fix-dictionary/4.4/index.html#int)

## Description

Describes the specific type or purpose of an [Allocation Report <AS>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AS_6583.html) message

Valid values:

3 = Sellside Calculated Using Preliminary (includes MiscFees and [NetMoney <118>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_118.html))

4 = Sellside Calculated Without Preliminary (sent unsolicited by sellside, includes MiscFees and [NetMoney <118>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_118.html))

5 = Warehouse recap

8 = Request to Intermediary

## Used In

- [Allocation Report <AS>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AS_6583.html)
- [Allocation Report Ack <AT>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AT_6584.html)

