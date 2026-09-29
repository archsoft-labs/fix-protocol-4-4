[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 660](https://www.onixs.biz/fix-dictionary/4.4/tagNum_660.html)

# FIX 4.4 : AcctIDSource <660> field

**Type:** [int](https://www.onixs.biz/fix-dictionary/4.4/index.html#int)

## Description

Used to identify the source of the [Account <1>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_1.html) code. This is especially useful if the account is a new account that the Respondent may not have setup yet in their system.

Valid values:

1 = BIC

2 = SID code

3 = TFM (GSPTA)

4 = OMGEO (AlertID)

5 = DTCC code

99 = Other (custom or proprietary)

## Used In

- [Execution Report <8>](https://www.onixs.biz/fix-dictionary/4.4/msgType_8_8.html)
- [Order Cancel Reject <9>](https://www.onixs.biz/fix-dictionary/4.4/msgType_9_9.html)
- [Quote Status Request <a>](https://www.onixs.biz/fix-dictionary/4.4/msgType_a_97.html)
- [New Order Multileg <AB>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AB_6566.html)
- [Multileg Order Cancel/Replace <AC>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AC_6567.html)
- [Trade Capture Report <AE>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AE_6569.html)
- [Order Mass Status Request <AF>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AF_6570.html)
- [Quote Request Reject <AG>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AG_6571.html)
- [Quote Status Report <AI>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AI_6573.html)
- [Quote Response <AJ>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AJ_6574.html)
- [Position Maintenance Request <AL>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AL_6576.html)
- [Position Maintenance Report <AM>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AM_6577.html)
- [Request For Positions <AN>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AN_6578.html)
- [Request for Positions Ack <AO>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AO_6579.html)
- [Position Report <AP>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AP_6580.html)
- [Trade Capture Report Ack <AR>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AR_6582.html)
- [Mass Quote Acknowledgement <b>](https://www.onixs.biz/fix-dictionary/4.4/msgType_b_98.html)
- [New Order Single <D>](https://www.onixs.biz/fix-dictionary/4.4/msgType_D_68.html)
- [New Order List <E>](https://www.onixs.biz/fix-dictionary/4.4/msgType_E_69.html)
- [Order Cancel Request <F>](https://www.onixs.biz/fix-dictionary/4.4/msgType_F_70.html)
- [Order Cancel/Replace Request <G>](https://www.onixs.biz/fix-dictionary/4.4/msgType_G_71.html)
- [Order Status Request <H>](https://www.onixs.biz/fix-dictionary/4.4/msgType_H_72.html)
- [Mass Quote <i>](https://www.onixs.biz/fix-dictionary/4.4/msgType_i_105.html)
- [Bid Request <k>](https://www.onixs.biz/fix-dictionary/4.4/msgType_k_107.html)
- [Registration Instructions <o>](https://www.onixs.biz/fix-dictionary/4.4/msgType_o_111.html)
- [Registration Instructions Response <p>](https://www.onixs.biz/fix-dictionary/4.4/msgType_p_112.html)
- [Quote Request <R>](https://www.onixs.biz/fix-dictionary/4.4/msgType_R_82.html)
- [New Order Cross <s>](https://www.onixs.biz/fix-dictionary/4.4/msgType_s_115.html)
- [Quote <S>](https://www.onixs.biz/fix-dictionary/4.4/msgType_S_83.html)
- [Cross Order Cancel/Replace Request <t>](https://www.onixs.biz/fix-dictionary/4.4/msgType_t_116.html)
- [Quote Cancel <Z>](https://www.onixs.biz/fix-dictionary/4.4/msgType_Z_90.html)

