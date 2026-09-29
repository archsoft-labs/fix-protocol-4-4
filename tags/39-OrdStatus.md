[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 39](https://www.onixs.biz/fix-dictionary/4.4/tagNum_39.html)

# FIX 4.4 : OrdStatus <39> field

**Type:** [char](https://www.onixs.biz/fix-dictionary/4.4/index.html#char)

## Description

Identifies current status of order.

Valid values:

0 = New

1 = Partially filled

2 = Filled

3 = Done for day

4 = Canceled

5 = ~~Replaced~~ ([Removed/Replaced](https://www.onixs.biz/fix-dictionary/4.4/app_6_f.html#1))

6 = Pending Cancel (e.g. result of [Order Cancel Request <F>](https://www.onixs.biz/fix-dictionary/4.4/msgType_F_70.html))

7 = [Stopped](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#Stopped)

8 = Rejected

9 = [Suspended](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#Suspended)

A = Pending New

B = Calculated

C = Expired

D = Accepted for bidding

E = Pending Replace (e.g. result of [Order Cancel/Replace Request <G>](https://www.onixs.biz/fix-dictionary/4.4/msgType_G_71.html))

*** SOME VALUES HAVE BEEN REPLACED - See: 

 [Appendix 6-F: 1.Replaced Field: ExecTransType (tag 20) and values in ExecType and OrdStatus fields [Replaced in FIX 4.3]](https://www.onixs.biz/fix-dictionary/4.4/app_6_f.html#1) ***

## Used In

- [Execution Report <8>](https://www.onixs.biz/fix-dictionary/4.4/msgType_8_8.html)
- [Order Cancel Reject <9>](https://www.onixs.biz/fix-dictionary/4.4/msgType_9_9.html)
- [Trade Capture Report <AE>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AE_6569.html)
- [List Status <N>](https://www.onixs.biz/fix-dictionary/4.4/msgType_N_78.html)

