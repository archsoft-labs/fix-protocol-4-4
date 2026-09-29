[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 160](https://www.onixs.biz/fix-dictionary/4.4/tagNum_160.html)

# FIX 4.4 : SettlInstMode <160> field

**Type:** [char](https://www.onixs.biz/fix-dictionary/4.4/index.html#char)

## Description

Indicates mode used for [Settlement Instructions <T>](https://www.onixs.biz/fix-dictionary/4.4/msgType_T_84.html) message.

Valid values:

~~0 = Default~~ (Replaced)

1 = Standing Instructions Provided

~~2 = Specific Allocation Account Overriding~~ (Replaced)

~~3 = Specific Allocation Account Standing~~ (Replaced)

4 = Specific Order for a single account (for CIV)

5 = Request reject

*** SOME VALUES HAVE BEEN REPLACED - See [Appendix 6-F: 21.Removed values from SettlInstMode (tag 160) field [Replaced in FIX 4.4]](https://www.onixs.biz/fix-dictionary/4.4/app_6_f.html#21) ***

## Used In

- [New Order List <E>](https://www.onixs.biz/fix-dictionary/4.4/msgType_E_69.html)
- [Settlement Instructions <T>](https://www.onixs.biz/fix-dictionary/4.4/msgType_T_84.html)

