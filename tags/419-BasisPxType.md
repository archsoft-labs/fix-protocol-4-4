[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 419](https://www.onixs.biz/fix-dictionary/4.4/tagNum_419.html)

# FIX 4.4 : BasisPxType <419> field

**Type:** [char](https://www.onixs.biz/fix-dictionary/4.4/index.html#char)

## Description

Code to represent the basis price type.

Valid values:

2 = Closing Price at morning session

3 = Closing Price

4 = Current price

5 = SQ

6 = VWAP through a day

7 = VWAP through a morning session

8 = VWAP through an afternoon session

9 = VWAP through a day except "YORI" (an opening auction)

A = VWAP through a morning session except "YORI" (an opening auction)

B = VWAP through an afternoon session except "YORI" (an opening auction)

C = Strike

D = Open

Z = Others

## Used In

- [Bid Request <k>](https://www.onixs.biz/fix-dictionary/4.4/msgType_k_107.html)

