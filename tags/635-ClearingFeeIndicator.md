[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 635](https://www.onixs.biz/fix-dictionary/4.4/tagNum_635.html)

# FIX 4.4 : ClearingFeeIndicator <635> field

**Type:** [String](https://www.onixs.biz/fix-dictionary/4.4/index.html#String)

## Description

Indicates type of fee being assessed of the customer for trade executions at an exchange. Applicable for futures markets only at this time.

Valid values (source CBOT, CME, NYBOT, and NYMEX):

B = CBOE Member

C = Non-member and Customer

E = Equity Member and Clearing Member

F = Full and Associate Member trading for own account and as floor Brokers

H = 106.H and 106.J Firms

I = GIM, IDEM and COM Membership Interest Holders

L = Lessee and 106.F Employees

M = All other ownership types

1 = 1st year delegate trading for his own account

2 = 2nd year delegate trading for his own account

3 = 3rd year delegate trading for his own account

4 = 4th year delegate trading for his own account

5 = 5th year delegate trading for his own account

9 = 6th year and beyond delegate trading for his own account

## Used In

- [Execution Report <8>](https://www.onixs.biz/fix-dictionary/4.4/msgType_8_8.html)
- [New Order Multileg <AB>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AB_6566.html)
- [Multileg Order Cancel/Replace <AC>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AC_6567.html)
- [Trade Capture Report <AE>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AE_6569.html)
- [Trade Capture Report Ack <AR>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AR_6582.html)
- [Allocation Report <AS>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AS_6583.html)
- [New Order Single <D>](https://www.onixs.biz/fix-dictionary/4.4/msgType_D_68.html)
- [New Order List <E>](https://www.onixs.biz/fix-dictionary/4.4/msgType_E_69.html)
- [Order Cancel/Replace Request <G>](https://www.onixs.biz/fix-dictionary/4.4/msgType_G_71.html)
- [Allocation Instruction <J>](https://www.onixs.biz/fix-dictionary/4.4/msgType_J_74.html)
- [New Order Cross <s>](https://www.onixs.biz/fix-dictionary/4.4/msgType_s_115.html)
- [Cross Order Cancel/Replace Request <t>](https://www.onixs.biz/fix-dictionary/4.4/msgType_t_116.html)

