[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 336](https://www.onixs.biz/fix-dictionary/4.4/tagNum_336.html)

# FIX 4.4 : TradingSessionID <336> field

**Type:** [String](https://www.onixs.biz/fix-dictionary/4.4/index.html#String)

## Description

Identifier for Trading Session

Can be used to represent a specific market trading session (e.g. "PRE-OPEN", "CROSS_2", "AFTER-HOURS", "TOSTNET", "TOSTNET2", etc).

To specify good for session where session spans more than one calendar day, use [TimeInForce <59>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_59.html) = 'Day' in conjunction with [TradingSessionID <336>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_336.html).

Values should be bi-laterally agreed to between counterparties.

Firms may register Trading Session values on the FIX website (presently a document maintained within "ECN and Exchanges" working group section).

## Used In

- [Advertisement <7>](https://www.onixs.biz/fix-dictionary/4.4/msgType_7_7.html)
- [Execution Report <8>](https://www.onixs.biz/fix-dictionary/4.4/msgType_8_8.html)
- [Quote Status Request <a>](https://www.onixs.biz/fix-dictionary/4.4/msgType_a_97.html)
- [Derivative Security List <AA>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AA_6565.html)
- [New Order Multileg <AB>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AB_6566.html)
- [Multileg Order Cancel/Replace <AC>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AC_6567.html)
- [Trade Capture Report Request <AD>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AD_6568.html)
- [Trade Capture Report <AE>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AE_6569.html)
- [Order Mass Status Request <AF>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AF_6570.html)
- [Quote Request Reject <AG>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AG_6571.html)
- [RFQ Request <AH>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AH_6572.html)
- [Quote Status Report <AI>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AI_6573.html)
- [Quote Response <AJ>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AJ_6574.html)
- [Position Maintenance Request <AL>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AL_6576.html)
- [Position Maintenance Report <AM>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AM_6577.html)
- [Request For Positions <AN>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AN_6578.html)
- [Allocation Report <AS>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AS_6583.html)
- [Collateral Request <AX>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AX_6588.html)
- [Collateral Assignment <AY>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AY_6589.html)
- [Mass Quote Acknowledgement <b>](https://www.onixs.biz/fix-dictionary/4.4/msgType_b_98.html)
- [Collateral Report <BA>](https://www.onixs.biz/fix-dictionary/4.4/msgType_BA_6665.html)
- [Collateral Inquiry <BB>](https://www.onixs.biz/fix-dictionary/4.4/msgType_BB_6666.html)
- [Collateral Inquiry Ack <BG>](https://www.onixs.biz/fix-dictionary/4.4/msgType_BG_6671.html)
- [Security Definition Request <c>](https://www.onixs.biz/fix-dictionary/4.4/msgType_c_99.html)
- [Security Definition <d>](https://www.onixs.biz/fix-dictionary/4.4/msgType_d_100.html)
- [New Order Single <D>](https://www.onixs.biz/fix-dictionary/4.4/msgType_D_68.html)
- [Security Status Request <e>](https://www.onixs.biz/fix-dictionary/4.4/msgType_e_101.html)
- [New Order List <E>](https://www.onixs.biz/fix-dictionary/4.4/msgType_E_69.html)
- [Security Status <f>](https://www.onixs.biz/fix-dictionary/4.4/msgType_f_102.html)
- [Trading Session Status Request <g>](https://www.onixs.biz/fix-dictionary/4.4/msgType_g_103.html)
- [Order Cancel/Replace Request <G>](https://www.onixs.biz/fix-dictionary/4.4/msgType_G_71.html)
- [Trading Session Status <h>](https://www.onixs.biz/fix-dictionary/4.4/msgType_h_104.html)
- [Mass Quote <i>](https://www.onixs.biz/fix-dictionary/4.4/msgType_i_105.html)
- [Allocation Instruction <J>](https://www.onixs.biz/fix-dictionary/4.4/msgType_J_74.html)
- [Bid Request <k>](https://www.onixs.biz/fix-dictionary/4.4/msgType_k_107.html)
- [Bid Response <l>](https://www.onixs.biz/fix-dictionary/4.4/msgType_l_108.html)
- [Order Mass Cancel Request <q>](https://www.onixs.biz/fix-dictionary/4.4/msgType_q_113.html)
- [Order Mass Cancel Report <r>](https://www.onixs.biz/fix-dictionary/4.4/msgType_r_114.html)
- [Quote Request <R>](https://www.onixs.biz/fix-dictionary/4.4/msgType_R_82.html)
- [New Order Cross <s>](https://www.onixs.biz/fix-dictionary/4.4/msgType_s_115.html)
- [Quote <S>](https://www.onixs.biz/fix-dictionary/4.4/msgType_S_83.html)
- [Cross Order Cancel/Replace Request <t>](https://www.onixs.biz/fix-dictionary/4.4/msgType_t_116.html)
- [Security Type Request <v>](https://www.onixs.biz/fix-dictionary/4.4/msgType_v_118.html)
- [Market Data Request <V>](https://www.onixs.biz/fix-dictionary/4.4/msgType_V_86.html)
- [Security Types <w>](https://www.onixs.biz/fix-dictionary/4.4/msgType_w_119.html)
- [Market Data - Snapshot/Full Refresh <W>](https://www.onixs.biz/fix-dictionary/4.4/msgType_W_87.html)
- [Security List Request <x>](https://www.onixs.biz/fix-dictionary/4.4/msgType_x_120.html)
- [Market Data - Incremental Refresh <X>](https://www.onixs.biz/fix-dictionary/4.4/msgType_X_88.html)
- [Security List <y>](https://www.onixs.biz/fix-dictionary/4.4/msgType_y_121.html)
- [Derivative Security List Request <z>](https://www.onixs.biz/fix-dictionary/4.4/msgType_z_122.html)
- [Quote Cancel <Z>](https://www.onixs.biz/fix-dictionary/4.4/msgType_Z_90.html)

