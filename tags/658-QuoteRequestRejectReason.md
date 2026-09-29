[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 658](https://www.onixs.biz/fix-dictionary/4.4/tagNum_658.html)

# FIX 4.4 : QuoteRequestRejectReason <658> field

**Type:** [int](https://www.onixs.biz/fix-dictionary/4.4/index.html#int)

## Description

Reason [QuoteRequest <R>](https://www.onixs.biz/fix-dictionary/4.4/msgType_R_82.html) was rejected.

Valid values:

1 = Unknown symbol (Security)

2 = Exchange(Security) closed

3 = [Quote Request <R>](https://www.onixs.biz/fix-dictionary/4.4/msgType_R_82.html) exceeds limit

4 = Too late to enter

5 = Invalid price

6 = Not authorized to request quote

7 = No match for inquiry

8 = No market for instrument

9 = No inventory

10 = Pass

99 = Other

## Used In

- [Quote Request Reject <AG>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AG_6571.html)

