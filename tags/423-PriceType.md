[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 423](https://www.onixs.biz/fix-dictionary/4.4/tagNum_423.html)

# FIX 4.4 : PriceType <423> field

**Type:** [int](https://www.onixs.biz/fix-dictionary/4.4/index.html#int)

## Description

Code to represent the price type.

Valid values:

1 = Percentage (e.g. [percent of par](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#PercentOfPar)) (often called ["dollar price"](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#DollarPrice) for fixed income)

2 = [Per unit](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#PerUnit) (i.e. per share or contract)

3 = Fixed Amount (absolute value)

4 = [Discount](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#Discount) - percentage points below par

5 = [Premium](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#Premium) - percentage points over par

6 = [Spread](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#Spread)

7 = [TED price](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#TEDPrice)

8 = [TED yield](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#TEDYield)

9 = Yield

10 = [Fixed cabinet trade price](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#FixedPriceCabinetTrade) (primarily for listed futures and options)

11 = [Variable cabinet trade price](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#FloatingPriceCabinetTrade) (primarily for listed futures and options)

(For Financing transactions [PriceType <423>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_423.html) implies the "repo type" - Fixed or Floating - 9 (Yield) or 6 (Spread) respectively - and [Price<44>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_44.html) gives the corresponding "repo rate".

## Used In

- [IOI <6>](https://www.onixs.biz/fix-dictionary/4.4/msgType_6_6.html)
- [Execution Report <8>](https://www.onixs.biz/fix-dictionary/4.4/msgType_8_8.html)
- [New Order Multileg <AB>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AB_6566.html)
- [Multileg Order Cancel/Replace <AC>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AC_6567.html)
- [Trade Capture Report <AE>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AE_6569.html)
- [Quote Request Reject <AG>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AG_6571.html)
- [Quote Status Report <AI>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AI_6573.html)
- [Quote Response <AJ>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AJ_6574.html)
- [Confirmation <AK>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AK_6575.html)
- [Allocation Report <AS>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AS_6583.html)
- [Collateral Request <AX>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AX_6588.html)
- [Collateral Assignment <AY>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AY_6589.html)
- [Collateral Response <AZ>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AZ_6590.html)
- [Collateral Report <BA>](https://www.onixs.biz/fix-dictionary/4.4/msgType_BA_6665.html)
- [Collateral Inquiry <BB>](https://www.onixs.biz/fix-dictionary/4.4/msgType_BB_6666.html)
- [New Order Single <D>](https://www.onixs.biz/fix-dictionary/4.4/msgType_D_68.html)
- [New Order List <E>](https://www.onixs.biz/fix-dictionary/4.4/msgType_E_69.html)
- [Order Cancel/Replace Request <G>](https://www.onixs.biz/fix-dictionary/4.4/msgType_G_71.html)
- [Allocation Instruction <J>](https://www.onixs.biz/fix-dictionary/4.4/msgType_J_74.html)
- [Bid Response <l>](https://www.onixs.biz/fix-dictionary/4.4/msgType_l_108.html)
- [Quote Request <R>](https://www.onixs.biz/fix-dictionary/4.4/msgType_R_82.html)
- [New Order Cross <s>](https://www.onixs.biz/fix-dictionary/4.4/msgType_s_115.html)
- [Quote <S>](https://www.onixs.biz/fix-dictionary/4.4/msgType_S_83.html)
- [Cross Order Cancel/Replace Request <t>](https://www.onixs.biz/fix-dictionary/4.4/msgType_t_116.html)

