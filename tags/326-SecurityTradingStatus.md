[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 326](https://www.onixs.biz/fix-dictionary/4.4/tagNum_326.html)

# FIX 4.4 : SecurityTradingStatus <326> field

**Type:** [int](https://www.onixs.biz/fix-dictionary/4.4/index.html#int)

## Description

Identifies the trading status applicable to the transaction.

Valid values:

1 = Opening Delay

2 = Trading Halt

3 = Resume

4 = No Open/No Resume

5 = Price Indication

6 = Trading Range Indication

7 = Market Imbalance Buy

8 = Market Imbalance Sell

9 = Market On Close Imbalance Buy

10 = Market On Close Imbalance Sell

11 = (not assigned)

12 = No Market Imbalance

13 = No Market On Close Imbalance

14 = ITS Pre-Opening

15 = New Price Indication

16 = Trade Dissemination Time

17 = Ready to trade (start of session)

18 = Not Available for trading (end of session)

19 = Not Traded on this Market

20 = Unknown or Invalid

21 = Pre-Open

22 = Opening Rotation

23 = Fast Market

## Used In

- [Security Status <f>](https://www.onixs.biz/fix-dictionary/4.4/msgType_f_102.html)

