[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 669](https://www.onixs.biz/fix-dictionary/4.4/tagNum_669.html)

# FIX 4.4 : LastParPx <669> field

**Type:** [Price](https://www.onixs.biz/fix-dictionary/4.4/index.html#Price)

## Description

Last price expressed in [percent-of-par](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#PercentOfPar). Conditionally required for Fixed Income trades when [LastPx <31>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_31.html) is expressed in Yield, Spread, Discount or any other type (see [PriceType <423>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_423.html)).

Usage: [Execution Report <8>](https://www.onixs.biz/fix-dictionary/4.4/msgType_8_8.html) and [Allocation Report <AS>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AS_6583.html) repeating executions block (from sellside).

## Used In

- [Execution Report <8>](https://www.onixs.biz/fix-dictionary/4.4/msgType_8_8.html)
- [Trade Capture Report <AE>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AE_6569.html)
- [Allocation Report <AS>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AS_6583.html)
- [Allocation Instruction <J>](https://www.onixs.biz/fix-dictionary/4.4/msgType_J_74.html)

