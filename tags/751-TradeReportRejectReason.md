[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 751](https://www.onixs.biz/fix-dictionary/4.4/tagNum_751.html)

# FIX 4.4 : TradeReportRejectReason <751> field

**Type:** [int](https://www.onixs.biz/fix-dictionary/4.4/index.html#int)

## Description

Reason Trade Capture Request was rejected.

Valid values:

0 = Successful (Default)

1 = Invalid party information

2 = Unknown instrument

3 = Unauthorized to report trades

4 = Invalid trade type

99 = Other

4000+ Reserved and available for bi-laterally agreed upon user-defined values

## Used In

- [Trade Capture Report Ack <AR>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AR_6582.html)

