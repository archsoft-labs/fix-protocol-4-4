[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 574](https://www.onixs.biz/fix-dictionary/4.4/tagNum_574.html)

# FIX 4.4 : MatchType <574> field

**Type:** [String](https://www.onixs.biz/fix-dictionary/4.4/index.html#String)

## Description

The point in the matching process at which this trade was matched.

Valid values:

**For NYSE and AMEX:**

A1 = Exact match on [Trade Date <75>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_75.html), Stock [Symbol <55>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_55.html), [Quantity <53>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_53.html), [Price <44>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_44.html), [Trade Type <418>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_418.html), and Special Trade Indicator plus four badges and execution time (within two-minute window)

A2 = Exact match on Trade Date, Stock Symbol, Quantity, Price, Trade Type, and Special Trade Indicator plus four badges

A3 = Exact match on Trade Date, Stock Symbol, Quantity, Price, Trade Type, and Special Trade Indicator plus two badges and execution time (within two-minute window)

A4 = Exact match on Trade Date, Stock Symbol, Quantity, Price, Trade Type, and Special Trade Indicator plus two badges

A5 = Exact match on Trade Date, Stock Symbol, Quantity, Price, Trade Type, and Special Trade Indicator plus execution time (within two-minute window)

AQ = Compared records resulting from stamped advisories or specialist accepts/pair-offs

S1 to S5 = Summarized Match using A1 to A5 exact match criteria except quantity is summarized

M1 = Exact Match on Trade Date, Stock Symbol, Quantity, Price, Trade Type, and Special Trade Indicator minus badges and times

M2 = Summarized Match minus badges and times

MT = OCS Locked In

**For NASDAQ:**

M1 = ACT M1 Match

M2 = ACT M2 Match

M3 = ACT Accepted Trade

M4 = ACT Default Trade

M5 = ACT Default After M2

M6 = ACT M6 Match

MT = Non-ACT

## Used In

- [Trade Capture Report <AE>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AE_6569.html)
- [Allocation Report <AS>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AS_6583.html)
- [Allocation Instruction <J>](https://www.onixs.biz/fix-dictionary/4.4/msgType_J_74.html)

