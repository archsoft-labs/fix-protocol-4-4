[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 528](https://www.onixs.biz/fix-dictionary/4.4/tagNum_528.html)

# FIX 4.4 : OrderCapacity <528> field

**Type:** [char](https://www.onixs.biz/fix-dictionary/4.4/index.html#char)

## Description

Designates the capacity of the firm placing the order.

Valid values:

A = Agency

G = Proprietary

I = Individual

P = Principal (Note for CMS purposes, Principal includes Proprietary)

R = [Riskless Principal](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#RisklessPrincipal)

W = Agent for Other Member

(as of FIX 4.3, this field replaced [Rule80A <47>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_47.html) used in conjunction with [OrderRestrictions <529>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_529.html) field)

See [Appendix 6-F: 12.Removed Deprecated Field: Rule80A (tag 47) [Deprecated and Replaced in FIX 4.3, Removed in FIX 4.4]](https://www.onixs.biz/fix-dictionary/4.4/app_6_f.html#12)

## Used In

- [Execution Report <8>](https://www.onixs.biz/fix-dictionary/4.4/msgType_8_8.html)
- [New Order Multileg <AB>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AB_6566.html)
- [Multileg Order Cancel/Replace <AC>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AC_6567.html)
- [Trade Capture Report <AE>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AE_6569.html)
- [Quote Response <AJ>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AJ_6574.html)
- [Confirmation <AK>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AK_6575.html)
- [Trade Capture Report Ack <AR>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AR_6582.html)
- [New Order Single <D>](https://www.onixs.biz/fix-dictionary/4.4/msgType_D_68.html)
- [New Order List <E>](https://www.onixs.biz/fix-dictionary/4.4/msgType_E_69.html)
- [Order Cancel/Replace Request <G>](https://www.onixs.biz/fix-dictionary/4.4/msgType_G_71.html)
- [Quote Request <R>](https://www.onixs.biz/fix-dictionary/4.4/msgType_R_82.html)
- [New Order Cross <s>](https://www.onixs.biz/fix-dictionary/4.4/msgType_s_115.html)
- [Quote <S>](https://www.onixs.biz/fix-dictionary/4.4/msgType_S_83.html)
- [Cross Order Cancel/Replace Request <t>](https://www.onixs.biz/fix-dictionary/4.4/msgType_t_116.html)

