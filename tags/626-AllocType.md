[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 626](https://www.onixs.biz/fix-dictionary/4.4/tagNum_626.html)

# FIX 4.4 : AllocType <626> field

**Type:** [int](https://www.onixs.biz/fix-dictionary/4.4/index.html#int)

## Description

Describes the specific type or purpose of an Allocation message (i.e. "Buyside Calculated")

Valid values:

1 = Calculated (includes MiscFees and [NetMoney <118>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_118.html))

2 = Preliminary (without MiscFees and [NetMoney <118>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_118.html))

~~3 = Sellside Calculated Using Preliminary (includes MiscFees and NetMoney)~~ (Replaced)

~~4 = Sellside Calculated Without Preliminary (sent unsolicited by sellside, includes MiscFees and NetMoney)~~ (Replaced)

5 = Ready-To-Book ~~- Single Order~~

~~6 = Buyside Ready-To-Book - Combined Set of Orders~~ (Replaced)

7 = Warehouse instruction

8 = [Request to Intermediary](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#RequestToIntermediary)

*** SOME VALUES HAVE BEEN REPLACED - See: 

 [Appendix 6-F: 8.Replaced values: AllocTransType (tag 71) with values in AllocType (tag 626) [Replaced in FIX 4.3]](https://www.onixs.biz/fix-dictionary/4.4/app_6_f.html#8) and 

 [Appendix 6-F: 22.Removed several values from AllocType (tag 626) field [Replaced in FIX 4.4]](https://www.onixs.biz/fix-dictionary/4.4/app_6_f.html#22) ***

## Used In

- [Allocation Instruction <J>](https://www.onixs.biz/fix-dictionary/4.4/msgType_J_74.html)
- [Allocation Instruction Ack <P>](https://www.onixs.biz/fix-dictionary/4.4/msgType_P_80.html)

