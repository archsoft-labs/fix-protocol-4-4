[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 63](https://www.onixs.biz/fix-dictionary/4.4/tagNum_63.html)

# FIX 4.4 : SettlType <63> field

**Type:** [char](https://www.onixs.biz/fix-dictionary/4.4/index.html#char)

## Description

Indicates order settlement period. If present, [SettlDate <64>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_64.html) overrides this field. If both [SettlType <63>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_63.html) and [SettlDate <64>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_64.html) are omitted, the default for [SettlType <63>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_63.html) is '0' (Regular)

Regular is defined as the default settlement period for the particular security on the exchange of execution.

In Fixed Income the contents of this field may influence the instrument definition if the [SecurityID <48>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_48.html) is ambiguous. In the US an active Treasury offering may be re-opened, and for a time one CUSIP will apply to both the current and "when-issued" securities. Supplying a value of "7" clarifies the instrument description; any other value or the absence of this field should cause the respondent to default to the active issue.

(Prior to FIX 4.4 this field was named "SettlmntTyp")

Valid values:

0 = Regular

1 = Cash

2 = Next Day (T+)

3 = T+2

4 = T+3

5 = T+4

6 = Future

7 = When And If Issued

8 = Sellers Option

9 = T+5

~~A = T+1~~(Removed in FIX 4.4, use "2 = Next Day (T+)" value)

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
- [New Order Single <D>](https://www.onixs.biz/fix-dictionary/4.4/msgType_D_68.html)
- [New Order List <E>](https://www.onixs.biz/fix-dictionary/4.4/msgType_E_69.html)
- [Order Cancel/Replace Request <G>](https://www.onixs.biz/fix-dictionary/4.4/msgType_G_71.html)
- [Allocation Instruction <J>](https://www.onixs.biz/fix-dictionary/4.4/msgType_J_74.html)
- [Bid Request <k>](https://www.onixs.biz/fix-dictionary/4.4/msgType_k_107.html)
- [Bid Response <l>](https://www.onixs.biz/fix-dictionary/4.4/msgType_l_108.html)
- [Quote Request <R>](https://www.onixs.biz/fix-dictionary/4.4/msgType_R_82.html)
- [New Order Cross <s>](https://www.onixs.biz/fix-dictionary/4.4/msgType_s_115.html)
- [Quote <S>](https://www.onixs.biz/fix-dictionary/4.4/msgType_S_83.html)
- [Cross Order Cancel/Replace Request <t>](https://www.onixs.biz/fix-dictionary/4.4/msgType_t_116.html)

