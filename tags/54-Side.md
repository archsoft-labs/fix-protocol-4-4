[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 54](https://www.onixs.biz/fix-dictionary/4.4/tagNum_54.html)

# FIX 4.4 : Side <54> field

**Type:** [char](https://www.onixs.biz/fix-dictionary/4.4/index.html#char)

## Description

Side of order.

Valid values:

1 = Buy

2 = Sell

3 = [Buy minus](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#BuyMinus)

4 = [Sell plus](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#SellPlus)

5 = [Sell short](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#SellShort)

6 = [Sell short exempt](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#SellShortExempt)

7 = Undisclosed (valid for IOI and List Order messages only)

8 = [Cross](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#Cross) (orders where counterparty is an exchange, valid for all messages except IOIs)

9 = [Cross short](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#CrossShort)

A = [Cross short exempt](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#CrossShortExempt)

B = ["As Defined"](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#AsDefined) (for use with multileg instruments)

C = ["Opposite"](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#Opposite) (for use with multileg instruments)

D = [Subscribe](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#Subscribe) (e.g. CIV)

E = [Redeem](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#Redeem) (e.g. CIV)

F = Lend (FINANCING - identifies direction of collateral)

G = Borrow (FINANCING - identifies direction of collateral)

## Used In

- [IOI <6>](https://www.onixs.biz/fix-dictionary/4.4/msgType_6_6.html)
- [Execution Report <8>](https://www.onixs.biz/fix-dictionary/4.4/msgType_8_8.html)
- [New Order Multileg <AB>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AB_6566.html)
- [Multileg Order Cancel/Replace <AC>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AC_6567.html)
- [Trade Capture Report Request <AD>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AD_6568.html)
- [Trade Capture Report <AE>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AE_6569.html)
- [Order Mass Status Request <AF>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AF_6570.html)
- [Quote Request Reject <AG>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AG_6571.html)
- [Quote Status Report <AI>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AI_6573.html)
- [Quote Response <AJ>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AJ_6574.html)
- [Confirmation <AK>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AK_6575.html)
- [Allocation Report <AS>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AS_6583.html)
- [Settlement Instruction Request <AV>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AV_6586.html)
- [Collateral Request <AX>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AX_6588.html)
- [Collateral Assignment <AY>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AY_6589.html)
- [Collateral Response <AZ>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AZ_6590.html)
- [Collateral Report <BA>](https://www.onixs.biz/fix-dictionary/4.4/msgType_BA_6665.html)
- [Collateral Inquiry <BB>](https://www.onixs.biz/fix-dictionary/4.4/msgType_BB_6666.html)
- [New Order Single <D>](https://www.onixs.biz/fix-dictionary/4.4/msgType_D_68.html)
- [New Order List <E>](https://www.onixs.biz/fix-dictionary/4.4/msgType_E_69.html)
- [Order Cancel Request <F>](https://www.onixs.biz/fix-dictionary/4.4/msgType_F_70.html)
- [Order Cancel/Replace Request <G>](https://www.onixs.biz/fix-dictionary/4.4/msgType_G_71.html)
- [Order Status Request <H>](https://www.onixs.biz/fix-dictionary/4.4/msgType_H_72.html)
- [Allocation Instruction <J>](https://www.onixs.biz/fix-dictionary/4.4/msgType_J_74.html)
- [Bid Request <k>](https://www.onixs.biz/fix-dictionary/4.4/msgType_k_107.html)
- [Bid Response <l>](https://www.onixs.biz/fix-dictionary/4.4/msgType_l_108.html)
- [List Strike Price <m>](https://www.onixs.biz/fix-dictionary/4.4/msgType_m_109.html)
- [Order Mass Cancel Request <q>](https://www.onixs.biz/fix-dictionary/4.4/msgType_q_113.html)
- [Don't Know Trade <Q>](https://www.onixs.biz/fix-dictionary/4.4/msgType_Q_81.html)
- [Order Mass Cancel Report <r>](https://www.onixs.biz/fix-dictionary/4.4/msgType_r_114.html)
- [Quote Request <R>](https://www.onixs.biz/fix-dictionary/4.4/msgType_R_82.html)
- [New Order Cross <s>](https://www.onixs.biz/fix-dictionary/4.4/msgType_s_115.html)
- [Quote <S>](https://www.onixs.biz/fix-dictionary/4.4/msgType_S_83.html)
- [Cross Order Cancel/Replace Request <t>](https://www.onixs.biz/fix-dictionary/4.4/msgType_t_116.html)
- [Settlement Instructions <T>](https://www.onixs.biz/fix-dictionary/4.4/msgType_T_84.html)
- [Cross Order Cancel Request <u>](https://www.onixs.biz/fix-dictionary/4.4/msgType_u_117.html)

