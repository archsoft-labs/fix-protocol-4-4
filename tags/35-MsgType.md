[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 35](https://www.onixs.biz/fix-dictionary/4.4/tagNum_35.html)

# FIX 4.4 : MsgType <35> field

**Type:** [String](https://www.onixs.biz/fix-dictionary/4.4/index.html#String)

## Description

Defines message type. ALWAYS THIRD FIELD IN MESSAGE. (Always unencrypted)

Note: A "U" as the first character in the [MsgType <35>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_35.html) field (i.e. U, U2, etc) indicates that the message format is privately defined between the sender and receiver.

Valid values: *** Note the use of lower case letters ***

0 = [Heartbeat <0>](https://www.onixs.biz/fix-dictionary/4.4/msgType_0_0.html)

1 = [Test Request <1>](https://www.onixs.biz/fix-dictionary/4.4/msgType_1_1.html)

2 = [Resend Request <2>](https://www.onixs.biz/fix-dictionary/4.4/msgType_2_2.html)

3 = [Reject <3>](https://www.onixs.biz/fix-dictionary/4.4/msgType_3_3.html)

4 = [Sequence Reset <4>](https://www.onixs.biz/fix-dictionary/4.4/msgType_4_4.html)

5 = [Logout <5>](https://www.onixs.biz/fix-dictionary/4.4/msgType_5_5.html)

6 = [Indication of Interest <6>](https://www.onixs.biz/fix-dictionary/4.4/msgType_6_6.html)

7 = [Advertisement <7>](https://www.onixs.biz/fix-dictionary/4.4/msgType_7_7.html)

8 = [Execution Report <8>](https://www.onixs.biz/fix-dictionary/4.4/msgType_8_8.html)

9 = [Order Cancel Reject <9>](https://www.onixs.biz/fix-dictionary/4.4/msgType_9_9.html)

A = [Logon <A>](https://www.onixs.biz/fix-dictionary/4.4/msgType_A_65.html)

B = [News <B>](https://www.onixs.biz/fix-dictionary/4.4/msgType_B_66.html)

C = [Email <C>](https://www.onixs.biz/fix-dictionary/4.4/msgType_C_67.html)

D = [New Order Single <D>](https://www.onixs.biz/fix-dictionary/4.4/msgType_D_68.html)

E = [New Order List <E>](https://www.onixs.biz/fix-dictionary/4.4/msgType_E_69.html)

F = [Order Cancel Request <F>](https://www.onixs.biz/fix-dictionary/4.4/msgType_F_70.html)

G = [Order Cancel/Replace Request <G>](https://www.onixs.biz/fix-dictionary/4.4/msgType_G_71.html)

H = [Order Status Request <H>](https://www.onixs.biz/fix-dictionary/4.4/msgType_H_72.html)

J = [Allocation Instruction <J>](https://www.onixs.biz/fix-dictionary/4.4/msgType_J_74.html)

K = [List Cancel Request <K>](https://www.onixs.biz/fix-dictionary/4.4/msgType_K_75.html)

L = [List Execute <L>](https://www.onixs.biz/fix-dictionary/4.4/msgType_L_76.html)

M = [List Status Request <M>](https://www.onixs.biz/fix-dictionary/4.4/msgType_M_77.html)

N = [List Status <N>](https://www.onixs.biz/fix-dictionary/4.4/msgType_N_78.html)

P = [Allocation Instruction Ack <P>](https://www.onixs.biz/fix-dictionary/4.4/msgType_P_80.html)

Q = [Don't Know Trade <Q>](https://www.onixs.biz/fix-dictionary/4.4/msgType_Q_81.html) (DK)

R = [Quote Request <R>](https://www.onixs.biz/fix-dictionary/4.4/msgType_R_82.html)

S = [Quote <S>](https://www.onixs.biz/fix-dictionary/4.4/msgType_S_83.html)

T = [Settlement Instructions <T>](https://www.onixs.biz/fix-dictionary/4.4/msgType_T_84.html)

V = [Market Data Request <V>](https://www.onixs.biz/fix-dictionary/4.4/msgType_V_86.html)

W = [Market Data-Snapshot/Full Refresh <W>](https://www.onixs.biz/fix-dictionary/4.4/msgType_W_87.html)

X = [Market Data-Incremental Refresh <X>](https://www.onixs.biz/fix-dictionary/4.4/msgType_X_88.html)

Y = [Market Data Request Reject <Y>](https://www.onixs.biz/fix-dictionary/4.4/msgType_Y_89.html)

Z = [Quote Cancel <Z>](https://www.onixs.biz/fix-dictionary/4.4/msgType_Z_90.html)

a = [Quote Status Request <a>](https://www.onixs.biz/fix-dictionary/4.4/msgType_a_97.html)

b = [Mass Quote Acknowledgement <b>](https://www.onixs.biz/fix-dictionary/4.4/msgType_b_98.html)

c = [Security Definition Request <c>](https://www.onixs.biz/fix-dictionary/4.4/msgType_c_99.html)

d = [Security Definition <d>](https://www.onixs.biz/fix-dictionary/4.4/msgType_d_100.html)

e = [Security Status Request <e>](https://www.onixs.biz/fix-dictionary/4.4/msgType_e_101.html)

f = [Security Status <f>](https://www.onixs.biz/fix-dictionary/4.4/msgType_f_102.html)

g = [Trading Session Status Request <g>](https://www.onixs.biz/fix-dictionary/4.4/msgType_g_103.html)

h = [Trading Session Status <h>](https://www.onixs.biz/fix-dictionary/4.4/msgType_h_104.html)

i = [Mass Quote <i>](https://www.onixs.biz/fix-dictionary/4.4/msgType_i_105.html)

j = [Business Message Reject <j>](https://www.onixs.biz/fix-dictionary/4.4/msgType_j_106.html)

k = [Bid Request <k>](https://www.onixs.biz/fix-dictionary/4.4/msgType_k_107.html)

l = [Bid Response <l>](https://www.onixs.biz/fix-dictionary/4.4/msgType_l_108.html) (lowercase L)

m = [List Strike Price <m>](https://www.onixs.biz/fix-dictionary/4.4/msgType_m_109.html)

n = [XML message <n>](https://www.onixs.biz/fix-dictionary/4.4/msgType_n_110.html) (e.g. non-FIX MsgType)

o = [Registration Instructions <o>](https://www.onixs.biz/fix-dictionary/4.4/msgType_o_111.html)

p = [Registration Instructions Response <p>](https://www.onixs.biz/fix-dictionary/4.4/msgType_p_112.html)

q = [Order Mass Cancel Request <q>](https://www.onixs.biz/fix-dictionary/4.4/msgType_q_113.html)

r = [Order Mass Cancel Report <r>](https://www.onixs.biz/fix-dictionary/4.4/msgType_r_114.html)

s = [New Order Cross <s>](https://www.onixs.biz/fix-dictionary/4.4/msgType_s_115.html)

t = [Cross Order Cancel/Replace Request <t>](https://www.onixs.biz/fix-dictionary/4.4/msgType_t_116.html) (a.k.a. Cross Order Modification Request)

u = [Cross Order Cancel Request <u>](https://www.onixs.biz/fix-dictionary/4.4/msgType_u_117.html)

v = [Security Type Request <v>](https://www.onixs.biz/fix-dictionary/4.4/msgType_v_118.html)

w = [Security Types <w>](https://www.onixs.biz/fix-dictionary/4.4/msgType_w_119.html)

x = [Security List Request <x>](https://www.onixs.biz/fix-dictionary/4.4/msgType_x_120.html)

y = [Security List <y>](https://www.onixs.biz/fix-dictionary/4.4/msgType_y_121.html)

z = [Derivative Security List Request <z>](https://www.onixs.biz/fix-dictionary/4.4/msgType_z_122.html)

AA = [Derivative Security List <AA>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AA_6565.html)

AB = [New Order Multileg <AB>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AB_6566.html)

AC = [Multileg Order Cancel/Replace <AC>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AC_6567.html) (a.k.a. Multileg Order Modification Request)

AD = [Trade Capture Report Request <AD>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AD_6568.html)

AE = [Trade Capture Report <AE>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AE_6569.html)

AF = [Order Mass Status Request <AF>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AF_6570.html)

AG = [Quote Request Reject <AG>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AG_6571.html)

AH = [RFQ Request <AH>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AH_6572.html)

AI = [Quote Status Report <AI>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AI_6573.html)

AJ = [Quote Response <AJ>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AJ_6574.html)

AK = [Confirmation <AK>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AK_6575.html)

AL = [Position Maintenance Request <AL>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AL_6576.html)

AM = [Position Maintenance Report <AM>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AM_6577.html)

AN = [Request For Positions <AN>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AN_6578.html)

AO = [Request For Positions Ack <AO>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AO_6579.html)

AP = [Position Report <AP>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AP_6580.html)

AQ = [Trade Capture Report Request Ack <AQ>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AQ_6581.html)

AR = [Trade Capture Report Ack <AR>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AR_6582.html)

AS = [Allocation Report <AS>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AS_6583.html) (aka Allocation Claim)

AT = [Allocation Report Ack <AT>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AT_6584.html) (aka Allocation Claim Ack)

AU = [Confirmation Ack <AU>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AU_6585.html) (aka Affirmation)

AV = [Settlement Instruction Request <AV>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AV_6586.html)

AW = [Assignment Report <AW>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AW_6587.html)

AX = [Collateral Request <AX>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AX_6588.html)

AY = [Collateral Assignment <AY>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AY_6589.html)

AZ = [Collateral Response <AZ>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AZ_6590.html)

BA = [Collateral Report <BA>](https://www.onixs.biz/fix-dictionary/4.4/msgType_BA_6665.html)

BB = [Collateral Inquiry <BB>](https://www.onixs.biz/fix-dictionary/4.4/msgType_BB_6666.html)

BC = [Network (Counterparty System) Status Request <BC>](https://www.onixs.biz/fix-dictionary/4.4/msgType_BC_6667.html)

BD = [Network (Counterparty System) Status Response <BD>](https://www.onixs.biz/fix-dictionary/4.4/msgType_BD_6668.html)

BE = [User Request <BE>](https://www.onixs.biz/fix-dictionary/4.4/msgType_BE_6669.html)

BF = [User Response <BF>](https://www.onixs.biz/fix-dictionary/4.4/msgType_BF_6670.html)

BG = [Collateral Inquiry Ack <BG>](https://www.onixs.biz/fix-dictionary/4.4/msgType_BG_6671.html)

BH = [Confirmation Request <BH>](https://www.onixs.biz/fix-dictionary/4.4/msgType_BH_6672.html)

