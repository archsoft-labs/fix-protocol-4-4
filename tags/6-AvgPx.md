[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 6](https://www.onixs.biz/fix-dictionary/4.4/tagNum_6.html)

# FIX 4.4 : AvgPx <6> field

**Type:** [Price](https://www.onixs.biz/fix-dictionary/4.4/index.html#Price)

## Description

Calculated average price of all fills on this order.

For Fixed Income trades [AvgPx <6>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_6.html) is always expressed as [percent-of-par](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#PercentOfPar), regardless of the [PriceType <423>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_423.html) of [LastPx <31>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_31.html). I.e., [AvgPx <6>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_6.html) will contain an average of percent-of-par values (see [LastParPx <669>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_669.html)) for issues traded in Yield, Spread or Discount.

## Used In

- [Execution Report <8>](https://www.onixs.biz/fix-dictionary/4.4/msgType_8_8.html)
- [Trade Capture Report <AE>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AE_6569.html)
- [Confirmation <AK>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AK_6575.html)
- [Allocation Report <AS>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AS_6583.html)
- [Allocation Instruction <J>](https://www.onixs.biz/fix-dictionary/4.4/msgType_J_74.html)
- [List Status <N>](https://www.onixs.biz/fix-dictionary/4.4/msgType_N_78.html)

