[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 71](https://www.onixs.biz/fix-dictionary/4.4/tagNum_71.html)

# FIX 4.4 : AllocTransType <71> field

**Type:** [char](https://www.onixs.biz/fix-dictionary/4.4/index.html#char)

## Description

Identifies allocation transaction type

Valid values:

0 = New

1 = Replace

2 = Cancel

~~3 = Preliminary (without MiscFees and NetMoney)~~ (Removed/Replaced)

~~4 = Calculated (includes MiscFees and NetMoney)~~ (Removed/Replaced)

~~5 = Calculated without Preliminary (sent unsolicited by broker, includes MiscFees and NetMoney)~~ (Removed/Replaced)

*** SOME VALUES HAVE BEEN REPLACED - See: 

 [Appendix 6-F: 8.Replaced values: AllocTransType (tag 71) with values in AllocType (tag 626) [Replaced in FIX 4.3]](https://www.onixs.biz/fix-dictionary/4.4/app_6_f.html#8) ***

## Used In

- [Allocation Report <AS>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AS_6583.html)
- [Allocation Instruction <J>](https://www.onixs.biz/fix-dictionary/4.4/msgType_J_74.html)

