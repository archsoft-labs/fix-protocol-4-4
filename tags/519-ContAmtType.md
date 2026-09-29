[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 519](https://www.onixs.biz/fix-dictionary/4.4/tagNum_519.html)

# FIX 4.4 : ContAmtType <519> field

**Type:** [int](https://www.onixs.biz/fix-dictionary/4.4/index.html#int)

## Description

Type of [ContAmtValue <520>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_520.html).

For UK valid values include:

1 = Commission Amount (actual)

2 = Commission % (actual)

3 = Initial Charge Amount

4 = Initial Charge %

5 = Discount Amount

6 = Discount %

7 = Dilution Levy Amount

8 = Dilution Levy %

9 = Exit Charge Amount

10 = Exit Charge %

11 = Fund-based Renewal Commission % (a.k.a. Trail commission)

12 = Projected Fund Value (i.e. for investments intended to realise or exceed a specific future value)

13 = Fund-based Renewal Commission Amount (based on Order value)

14 = Fund-based Renewal Commission Amount (based on Projected Fund value)

15 = Net Settlement Amount

NOTE That Commission Amount / % in Contract Amounts is the commission actually charged, rather than the commission instructions given in Fields [Commission <12>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_12.html) and [CommType <13>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_13.html).

## Used In

- [Execution Report <8>](https://www.onixs.biz/fix-dictionary/4.4/msgType_8_8.html)
- [Trade Capture Report <AE>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AE_6569.html)

