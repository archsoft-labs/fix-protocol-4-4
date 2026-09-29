[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 64](https://www.onixs.biz/fix-dictionary/4.4/tagNum_64.html)

# FIX 4.4 : SettlDate <64> field

**Type:** [LocalMktDate](https://www.onixs.biz/fix-dictionary/4.4/index.html#LocalMktDate)

## Description

Specific date of trade settlement (SettlementDate) in YYYYMMDD format.

If present, this field overrides [SettlType <63>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_63.html). This field is required if the value of [SettlType <63>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_63.html) is '6' (Future) or '8' (Sellers Option). This field must be omitted if the value of [SettlType <63>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_63.html) is '7' (When and If Issued)

(expressed in local time at place of settlement)

(Prior to FIX 4.4 this field was named "FutSettDate")

## Used In

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
- [Mass Quote Acknowledgement <b>](https://www.onixs.biz/fix-dictionary/4.4/msgType_b_98.html)
- [Collateral Report <BA>](https://www.onixs.biz/fix-dictionary/4.4/msgType_BA_6665.html)
- [Collateral Inquiry <BB>](https://www.onixs.biz/fix-dictionary/4.4/msgType_BB_6666.html)
- [Collateral Inquiry Ack <BG>](https://www.onixs.biz/fix-dictionary/4.4/msgType_BG_6671.html)
- [New Order Single <D>](https://www.onixs.biz/fix-dictionary/4.4/msgType_D_68.html)
- [New Order List <E>](https://www.onixs.biz/fix-dictionary/4.4/msgType_E_69.html)
- [Order Cancel/Replace Request <G>](https://www.onixs.biz/fix-dictionary/4.4/msgType_G_71.html)
- [Mass Quote <i>](https://www.onixs.biz/fix-dictionary/4.4/msgType_i_105.html)
- [Allocation Instruction <J>](https://www.onixs.biz/fix-dictionary/4.4/msgType_J_74.html)
- [Bid Request <k>](https://www.onixs.biz/fix-dictionary/4.4/msgType_k_107.html)
- [Bid Response <l>](https://www.onixs.biz/fix-dictionary/4.4/msgType_l_108.html)
- [Quote Request <R>](https://www.onixs.biz/fix-dictionary/4.4/msgType_R_82.html)
- [New Order Cross <s>](https://www.onixs.biz/fix-dictionary/4.4/msgType_s_115.html)
- [Quote <S>](https://www.onixs.biz/fix-dictionary/4.4/msgType_S_83.html)
- [Cross Order Cancel/Replace Request <t>](https://www.onixs.biz/fix-dictionary/4.4/msgType_t_116.html)

