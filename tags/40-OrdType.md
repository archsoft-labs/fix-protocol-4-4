[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 40](https://www.onixs.biz/fix-dictionary/4.4/tagNum_40.html)

# FIX 4.4 : OrdType <40> field

**Type:** [char](https://www.onixs.biz/fix-dictionary/4.4/index.html#char)

## Description

Order type.

Valid values:

1 = [Market](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#Market)

2 = [Limit](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#Limit)

3 = [Stop](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#Stop)

4 = [Stop limit](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#StopLimit)

~~5 = Market on close~~ (No longer used)

6 = [With or without](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#WithOrWithout)

7 = [Limit or better](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#LimitOrBetter) (Deprecated)

8 = [Limit with or without](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#LimitWithOrWithout)

9 = [On basis](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#OnBasis)

~~A = On close~~ (No longer used)

~~B = Limit on close~~ (No longer used)

~~C = Forex - Market~~ (No longer used)

D = [Previously quoted](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#PreviouslyQuoted)

E = [Previously indicated](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#PreviouslyIndicated)

~~F = Forex - Limit~~ (No longer used)

G = [Forex - Swap](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#ForexSwap)

~~H = Forex - Previously Quoted~~ (No longer used)

I = [Funari](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#Funari) (Limit Day Order with unexecuted portion handled as Market On Close. E.g. Japan)

J = [Market If Touched (MIT)](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#MarketIfTouched)

K = [Market with Leftover as Limit](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#MarketWithLeftoverAsLimit) (market order then unexecuted quantity becomes limit order at last price)

L = [Previous Fund Valuation Point](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#PreviousFundValuationPoint) (Historic pricing) (for CIV)

M = [Next Fund Valuation Point](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#NextFundValuationPoint) (Forward pricing) (for CIV)

P = Pegged

*** SOME VALUES ARE NO LONGER USED - See: 

 "[Appendix 6-F: 11.Removed Deprecated "On Close"-related Values for OrdType Field [Deprecated in FIX 4.3, Removed in FIX 4.4]](https://www.onixs.biz/fix-dictionary/4.4/app_6_f.html#11)" and 

 "[Appendix 6-F: 14.Removed three Deprecated "Forex - "-related Values for OrdType Field [Deprecated and Replaced in FIX 4.3, Removed in FIX 4.4]](https://www.onixs.biz/fix-dictionary/4.4/app_6_f.html#14)" ***

## Used In

- [Execution Report <8>](https://www.onixs.biz/fix-dictionary/4.4/msgType_8_8.html)
- [New Order Multileg <AB>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AB_6566.html)
- [Multileg Order Cancel/Replace <AC>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AC_6567.html)
- [Trade Capture Report <AE>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AE_6569.html)
- [Quote Request Reject <AG>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AG_6571.html)
- [Quote Status Report <AI>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AI_6573.html)
- [Quote Response <AJ>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AJ_6574.html)
- [Mass Quote Acknowledgement <b>](https://www.onixs.biz/fix-dictionary/4.4/msgType_b_98.html)
- [New Order Single <D>](https://www.onixs.biz/fix-dictionary/4.4/msgType_D_68.html)
- [New Order List <E>](https://www.onixs.biz/fix-dictionary/4.4/msgType_E_69.html)
- [Order Cancel/Replace Request <G>](https://www.onixs.biz/fix-dictionary/4.4/msgType_G_71.html)
- [Mass Quote <i>](https://www.onixs.biz/fix-dictionary/4.4/msgType_i_105.html)
- [Quote Request <R>](https://www.onixs.biz/fix-dictionary/4.4/msgType_R_82.html)
- [New Order Cross <s>](https://www.onixs.biz/fix-dictionary/4.4/msgType_s_115.html)
- [Quote <S>](https://www.onixs.biz/fix-dictionary/4.4/msgType_S_83.html)
- [Cross Order Cancel/Replace Request <t>](https://www.onixs.biz/fix-dictionary/4.4/msgType_t_116.html)

