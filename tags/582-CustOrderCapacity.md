[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 582](https://www.onixs.biz/fix-dictionary/4.4/tagNum_582.html)

# FIX 4.4 : CustOrderCapacity <582> field

**Type:** [int](https://www.onixs.biz/fix-dictionary/4.4/index.html#int)

## Description

Capacity of customer placing the order

1 = Member trading for their own account

2 = Clearing Firm trading for its proprietary account

3 = Member trading for another member

4 = All other

Primarily used by futures exchanges to indicate the CTICode (customer type indicator) as required by the US CFTC (Commodity Futures Trading Commission).

## Used In

- [Execution Report <8>](https://www.onixs.biz/fix-dictionary/4.4/msgType_8_8.html)
- [New Order Multileg <AB>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AB_6566.html)
- [Multileg Order Cancel/Replace <AC>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AC_6567.html)
- [Trade Capture Report <AE>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AE_6569.html)
- [Quote Status Report <AI>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AI_6573.html)
- [Quote Response <AJ>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AJ_6574.html)
- [Trade Capture Report Ack <AR>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AR_6582.html)
- [New Order Single <D>](https://www.onixs.biz/fix-dictionary/4.4/msgType_D_68.html)
- [New Order List <E>](https://www.onixs.biz/fix-dictionary/4.4/msgType_E_69.html)
- [Order Cancel/Replace Request <G>](https://www.onixs.biz/fix-dictionary/4.4/msgType_G_71.html)
- [New Order Cross <s>](https://www.onixs.biz/fix-dictionary/4.4/msgType_s_115.html)
- [Quote <S>](https://www.onixs.biz/fix-dictionary/4.4/msgType_S_83.html)
- [Cross Order Cancel/Replace Request <t>](https://www.onixs.biz/fix-dictionary/4.4/msgType_t_116.html)

