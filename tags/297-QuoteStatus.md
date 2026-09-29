[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 297](https://www.onixs.biz/fix-dictionary/4.4/tagNum_297.html)

# FIX 4.4 : QuoteStatus <297> field

**Type:** [int](https://www.onixs.biz/fix-dictionary/4.4/index.html#int)

## Description

Identifies the status of the quote acknowledgement.

Valid values:

0 = Accepted

1 = Canceled for [Symbol <55>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_55.html)(s)

2 = Canceled for [SecurityType <167>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_167.html)(s)

3 = Canceled for [UnderlyingSymbol <311>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_311.html)

4 = Canceled All

5 = Rejected

6 = Removed from Market

7 = Expired

8 = Query

9 = Quote Not Found

10 = Pending

11 = Pass

12 = Locked Market Warning

13 = Cross Market Warning

14 = Canceled due to lock market

15 = Canceled due to cross market

## Used In

- [Quote Status Report <AI>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AI_6573.html)
- [Mass Quote Acknowledgement <b>](https://www.onixs.biz/fix-dictionary/4.4/msgType_b_98.html)

