[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 277](https://www.onixs.biz/fix-dictionary/4.4/tagNum_277.html)

# FIX 4.4 : TradeCondition <277> field

**Type:** [MultipleValueString](https://www.onixs.biz/fix-dictionary/4.4/index.html#MultipleValueString)

## Description

Space-delimited list of conditions describing a trade

Valid values:

A = Cash (only) Market

B = Average Price Trade

C = Cash Trade (same day clearing)

D = Next Day (only) Market

E = Opening / Reopening Trade Detail

F = Intraday Trade Detail

G = Rule 127 Trade (NYSE)

H = Rule 155 Trade (Amex)

I = Sold Last (late reporting)

J = Next Day Trade (next day clearing)

K = Opened (late report of opened trade)

L = Seller

M = Sold (out of sequence)

N = Stopped Stock (guarantee of price but does not execute the order)

P = Imbalance More Buyers (Cannot be used in combination with Q)

Q = Imbalance More Sellers (Cannot be used in combination with P)

R = Opening Price

## Used In

- [Market Data - Snapshot/Full Refresh <W>](https://www.onixs.biz/fix-dictionary/4.4/msgType_W_87.html)
- [Market Data - Incremental Refresh <X>](https://www.onixs.biz/fix-dictionary/4.4/msgType_X_88.html)

