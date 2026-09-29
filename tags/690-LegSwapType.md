[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 690](https://www.onixs.biz/fix-dictionary/4.4/tagNum_690.html)

# FIX 4.4 : LegSwapType <690> field

**Type:** [int](https://www.onixs.biz/fix-dictionary/4.4/index.html#int)

## Description

For Fixed Income, used instead of [LegQty <687>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_687.html) or [LegOrderQty <685>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_685.html) to requests the respondent to calculate the quantity based on the quantity on the opposite side of the swap.

Valid values:

1 = Par For Par

2 = Modified Duration

4 = Risk

5 = Proceeds

## Used In

- [Execution Report <8>](https://www.onixs.biz/fix-dictionary/4.4/msgType_8_8.html)
- [New Order Multileg <AB>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AB_6566.html)
- [Multileg Order Cancel/Replace <AC>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AC_6567.html)
- [Trade Capture Report <AE>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AE_6569.html)
- [Quote Request Reject <AG>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AG_6571.html)
- [Quote Status Report <AI>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AI_6573.html)
- [Quote Response <AJ>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AJ_6574.html)
- [Trade Capture Report Ack <AR>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AR_6582.html)
- [Quote Request <R>](https://www.onixs.biz/fix-dictionary/4.4/msgType_R_82.html)
- [Quote <S>](https://www.onixs.biz/fix-dictionary/4.4/msgType_S_83.html)
- [Security List <y>](https://www.onixs.biz/fix-dictionary/4.4/msgType_y_121.html)

