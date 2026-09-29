[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 484](https://www.onixs.biz/fix-dictionary/4.4/tagNum_484.html)

# FIX 4.4 : ExecPriceType <484> field

**Type:** [char](https://www.onixs.biz/fix-dictionary/4.4/index.html#char)

## Description

For CIV - Identifies how the execution price [LastPx <31>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_31.html) was calculated from the fund unit/share price(s) calculated at the fund valuation point.

Valid values are:

B = Bid price

C = Creation price

D = Creation price plus adjustment %

E = Creation price plus adjustment amount

O = Offer price

P = Offer price minus adjustment %

Q = Offer price minus adjustment amount

S = Single price

## Used In

- [Execution Report <8>](https://www.onixs.biz/fix-dictionary/4.4/msgType_8_8.html)

