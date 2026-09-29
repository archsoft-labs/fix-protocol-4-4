[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 481](https://www.onixs.biz/fix-dictionary/4.4/tagNum_481.html)

# FIX 4.4 : MoneyLaunderingStatus <481> field

**Type:** [char](https://www.onixs.biz/fix-dictionary/4.4/index.html#char)

## Description

A one character code identifying Money laundering status.

Valid values:

Y = Passed

N = Not checked

1 = Exempt - Below The Limit

2 = Exempt - Client Money Type Exemption

3 = Exempt - Authorised Credit or Financial Institution.

## Used In

- [Execution Report <8>](https://www.onixs.biz/fix-dictionary/4.4/msgType_8_8.html)
- [New Order Multileg <AB>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AB_6566.html)
- [Multileg Order Cancel/Replace <AC>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AC_6567.html)
- [New Order Single <D>](https://www.onixs.biz/fix-dictionary/4.4/msgType_D_68.html)
- [New Order List <E>](https://www.onixs.biz/fix-dictionary/4.4/msgType_E_69.html)
- [Order Cancel/Replace Request <G>](https://www.onixs.biz/fix-dictionary/4.4/msgType_G_71.html)
- [New Order Cross <s>](https://www.onixs.biz/fix-dictionary/4.4/msgType_s_115.html)
- [Cross Order Cancel/Replace Request <t>](https://www.onixs.biz/fix-dictionary/4.4/msgType_t_116.html)

