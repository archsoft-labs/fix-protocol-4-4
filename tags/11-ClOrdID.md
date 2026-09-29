[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 11](https://www.onixs.biz/fix-dictionary/4.4/tagNum_11.html)

# FIX 4.4 : ClOrdID <11> field

**Type:** [String](https://www.onixs.biz/fix-dictionary/4.4/index.html#String)

## Description

Unique identifier for Order as assigned by the buy-side (institution, broker, intermediary etc.) (identified by [SenderCompID <49>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_49.html) or [OnBehalfOfCompID <115>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_115.html) as appropriate). Uniqueness must be guaranteed within a single trading day. Firms, particularly those which electronically submit multi-day orders, trade globally or throughout market close periods, should ensure uniqueness across days, for example by embedding a date within the [ClOrdID <11>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_11.html) field.

## Used In

- [Execution Report <8>](https://www.onixs.biz/fix-dictionary/4.4/msgType_8_8.html)
- [Order Cancel Reject <9>](https://www.onixs.biz/fix-dictionary/4.4/msgType_9_9.html)
- [New Order Multileg <AB>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AB_6566.html)
- [Multileg Order Cancel/Replace <AC>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AC_6567.html)
- [Trade Capture Report Request <AD>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AD_6568.html)
- [Trade Capture Report <AE>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AE_6569.html)
- [Quote Response <AJ>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AJ_6574.html)
- [Confirmation <AK>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AK_6575.html)
- [Allocation Report <AS>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AS_6583.html)
- [Collateral Request <AX>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AX_6588.html)
- [Collateral Assignment <AY>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AY_6589.html)
- [Collateral Response <AZ>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AZ_6590.html)
- [Collateral Report <BA>](https://www.onixs.biz/fix-dictionary/4.4/msgType_BA_6665.html)
- [Collateral Inquiry <BB>](https://www.onixs.biz/fix-dictionary/4.4/msgType_BB_6666.html)
- [Collateral Inquiry Ack <BG>](https://www.onixs.biz/fix-dictionary/4.4/msgType_BG_6671.html)
- [Confirmation Request <BH>](https://www.onixs.biz/fix-dictionary/4.4/msgType_BH_6672.html)
- [Email <C>](https://www.onixs.biz/fix-dictionary/4.4/msgType_C_67.html)
- [New Order Single <D>](https://www.onixs.biz/fix-dictionary/4.4/msgType_D_68.html)
- [New Order List <E>](https://www.onixs.biz/fix-dictionary/4.4/msgType_E_69.html)
- [Order Cancel Request <F>](https://www.onixs.biz/fix-dictionary/4.4/msgType_F_70.html)
- [Order Cancel/Replace Request <G>](https://www.onixs.biz/fix-dictionary/4.4/msgType_G_71.html)
- [Order Status Request <H>](https://www.onixs.biz/fix-dictionary/4.4/msgType_H_72.html)
- [Allocation Instruction <J>](https://www.onixs.biz/fix-dictionary/4.4/msgType_J_74.html)
- [List Strike Price <m>](https://www.onixs.biz/fix-dictionary/4.4/msgType_m_109.html)
- [List Status <N>](https://www.onixs.biz/fix-dictionary/4.4/msgType_N_78.html)
- [Registration Instructions <o>](https://www.onixs.biz/fix-dictionary/4.4/msgType_o_111.html)
- [Registration Instructions Response <p>](https://www.onixs.biz/fix-dictionary/4.4/msgType_p_112.html)
- [Order Mass Cancel Request <q>](https://www.onixs.biz/fix-dictionary/4.4/msgType_q_113.html)
- [Order Mass Cancel Report <r>](https://www.onixs.biz/fix-dictionary/4.4/msgType_r_114.html)
- [Quote Request <R>](https://www.onixs.biz/fix-dictionary/4.4/msgType_R_82.html)
- [New Order Cross <s>](https://www.onixs.biz/fix-dictionary/4.4/msgType_s_115.html)
- [Cross Order Cancel/Replace Request <t>](https://www.onixs.biz/fix-dictionary/4.4/msgType_t_116.html)
- [Settlement Instructions <T>](https://www.onixs.biz/fix-dictionary/4.4/msgType_T_84.html)
- [Cross Order Cancel Request <u>](https://www.onixs.biz/fix-dictionary/4.4/msgType_u_117.html)

