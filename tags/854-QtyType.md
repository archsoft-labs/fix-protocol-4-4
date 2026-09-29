[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 854](https://www.onixs.biz/fix-dictionary/4.4/tagNum_854.html)

# FIX 4.4 : QtyType <854> field

**Type:** [int](https://www.onixs.biz/fix-dictionary/4.4/index.html#int)

## Description

Type of quantity specified in a [Quantity <53>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_53.html) field:

Valid values:

0 = Units (shares,[par](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#Par), currency)

1 = Contracts (if used - should specify [ContractMultiplier <231>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_231.html))

## Used In

- [IOI <6>](https://www.onixs.biz/fix-dictionary/4.4/msgType_6_6.html)
- [Advertisement <7>](https://www.onixs.biz/fix-dictionary/4.4/msgType_7_7.html)
- [Execution Report <8>](https://www.onixs.biz/fix-dictionary/4.4/msgType_8_8.html)
- [New Order Multileg <AB>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AB_6566.html)
- [Multileg Order Cancel/Replace <AC>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AC_6567.html)
- [Trade Capture Report <AE>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AE_6569.html)
- [Quote Request Reject <AG>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AG_6571.html)
- [Confirmation <AK>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AK_6575.html)
- [Allocation Report <AS>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AS_6583.html)
- [Collateral Request <AX>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AX_6588.html)
- [Collateral Assignment <AY>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AY_6589.html)
- [Collateral Response <AZ>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AZ_6590.html)
- [Collateral Report <BA>](https://www.onixs.biz/fix-dictionary/4.4/msgType_BA_6665.html)
- [Collateral Inquiry <BB>](https://www.onixs.biz/fix-dictionary/4.4/msgType_BB_6666.html)
- [Collateral Inquiry Ack <BG>](https://www.onixs.biz/fix-dictionary/4.4/msgType_BG_6671.html)
- [New Order Single <D>](https://www.onixs.biz/fix-dictionary/4.4/msgType_D_68.html)
- [New Order List <E>](https://www.onixs.biz/fix-dictionary/4.4/msgType_E_69.html)
- [Order Cancel/Replace Request <G>](https://www.onixs.biz/fix-dictionary/4.4/msgType_G_71.html)
- [Allocation Instruction <J>](https://www.onixs.biz/fix-dictionary/4.4/msgType_J_74.html)
- [Quote Request <R>](https://www.onixs.biz/fix-dictionary/4.4/msgType_R_82.html)
- [New Order Cross <s>](https://www.onixs.biz/fix-dictionary/4.4/msgType_s_115.html)
- [Cross Order Cancel/Replace Request <t>](https://www.onixs.biz/fix-dictionary/4.4/msgType_t_116.html)

