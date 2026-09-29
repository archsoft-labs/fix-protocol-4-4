[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 81](https://www.onixs.biz/fix-dictionary/4.4/tagNum_81.html)

# FIX 4.4 : ProcessCode <81> field

**Type:** [char](https://www.onixs.biz/fix-dictionary/4.4/index.html#char)

## Description

Processing code for sub-account. Absence of this field in [AllocAccount <79>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_79.html) / [AllocPrice <366>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_366.html) /[AllocQty <80>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_80.html) / [ProcessCode <81>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_81.html) instance indicates regular trade.

Valid values:

0 = regular

1 = soft dollar

2 = step-in

3 = step-out

4 = soft-dollar step-in

5 = soft-dollar step-out

6 = plan sponsor

## Used In

- [New Order Multileg <AB>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AB_6566.html)
- [Multileg Order Cancel/Replace <AC>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AC_6567.html)
- [Trade Capture Report <AE>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AE_6569.html)
- [Confirmation <AK>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AK_6575.html)
- [Allocation Report <AS>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AS_6583.html)
- [New Order Single <D>](https://www.onixs.biz/fix-dictionary/4.4/msgType_D_68.html)
- [New Order List <E>](https://www.onixs.biz/fix-dictionary/4.4/msgType_E_69.html)
- [Allocation Instruction <J>](https://www.onixs.biz/fix-dictionary/4.4/msgType_J_74.html)
- [New Order Cross <s>](https://www.onixs.biz/fix-dictionary/4.4/msgType_s_115.html)
- [Cross Order Cancel/Replace Request <t>](https://www.onixs.biz/fix-dictionary/4.4/msgType_t_116.html)

