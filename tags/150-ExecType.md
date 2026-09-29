[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 150](https://www.onixs.biz/fix-dictionary/4.4/tagNum_150.html)

# FIX 4.4 : ExecType <150> field

**Type:** [char](https://www.onixs.biz/fix-dictionary/4.4/index.html#char)

## Description

Describes the specific Execution Report (i.e. Pending Cancel) while [OrdStatus <39>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_39.html) will always identify the current order status (i.e. Partially Filled)

Valid values:

0 = New

~~1 = Partial fill~~ ([Replaced](https://www.onixs.biz/fix-dictionary/4.4/app_6_f.html#1))

~~2 = Fill~~ ([Replaced](https://www.onixs.biz/fix-dictionary/4.4/app_6_f.html#1))

3 = Done for day

4 = Canceled

5 = Replaced

6 = Pending Cancel (e.g. result of [Order Cancel Request <F>](https://www.onixs.biz/fix-dictionary/4.4/msgType_F_70.html))

7 = Stopped

8 = Rejected

9 = Suspended

A = Pending New

B = Calculated

C = Expired

D = Restated ([Execution Report <8>](https://www.onixs.biz/fix-dictionary/4.4/msgType_8_8.html) sent unsolicited by sellside, with [ExecRestatementReason <378>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_378.html) set)

E = Pending Replace (e.g. result of [Order Cancel/Replace Request <G>](https://www.onixs.biz/fix-dictionary/4.4/msgType_G_71.html))

F = Trade (partial fill or fill)

G = Trade Correct (formerly an [ExecTransType <20>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_20.html))

H = Trade Cancel (formerly an [ExecTransType <20>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_20.html))

I = Order Status (formerly an [ExecTransType <20>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_20.html))

*** SOME VALUES HAVE BEEN REPLACED - See: 

 [Appendix 6-F: 1.Replaced Field: ExecTransType (tag 20) and values in ExecType and OrdStatus fields [replaced in FIX 4.3]](https://www.onixs.biz/fix-dictionary/4.4/app_6_f.html#1) ***

## Used In

- [Execution Report <8>](https://www.onixs.biz/fix-dictionary/4.4/msgType_8_8.html)
- [Trade Capture Report Request <AD>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AD_6568.html)
- [Trade Capture Report <AE>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AE_6569.html)
- [Trade Capture Report Ack <AR>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AR_6582.html)

