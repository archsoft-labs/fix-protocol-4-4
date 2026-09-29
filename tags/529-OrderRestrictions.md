[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 529](https://www.onixs.biz/fix-dictionary/4.4/tagNum_529.html)

# FIX 4.4 : OrderRestrictions <529> field

**Type:** [MultipleValueString](https://www.onixs.biz/fix-dictionary/4.4/index.html#MultipleValueString)

## Description

Restrictions associated with an order. If more than one restriction is applicable to an order, this field can contain multiple  instructions separated by space.

Valid values:

1 = Program Trade

2 = Index Arbitrage

3 = Non-Index Arbitrage

4 = Competing Market Maker

5 = Acting as Market Maker or Specialist in the security

6 = Acting as Market Maker or Specialist in the underlying security of a derivative security

7 = Foreign Entity (of foreign government or regulatory jurisdiction)

8 = External Market Participant

9 = External Inter-connected Market Linkage

A = Riskless Arbitrage

## Used In

- [Execution Report <8>](https://www.onixs.biz/fix-dictionary/4.4/msgType_8_8.html)
- [New Order Multileg <AB>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AB_6566.html)
- [Multileg Order Cancel/Replace <AC>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AC_6567.html)
- [Trade Capture Report <AE>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AE_6569.html)
- [Confirmation <AK>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AK_6575.html)
- [Trade Capture Report Ack <AR>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AR_6582.html)
- [New Order Single <D>](https://www.onixs.biz/fix-dictionary/4.4/msgType_D_68.html)
- [New Order List <E>](https://www.onixs.biz/fix-dictionary/4.4/msgType_E_69.html)
- [Order Cancel/Replace Request <G>](https://www.onixs.biz/fix-dictionary/4.4/msgType_G_71.html)
- [New Order Cross <s>](https://www.onixs.biz/fix-dictionary/4.4/msgType_s_115.html)
- [Cross Order Cancel/Replace Request <t>](https://www.onixs.biz/fix-dictionary/4.4/msgType_t_116.html)

