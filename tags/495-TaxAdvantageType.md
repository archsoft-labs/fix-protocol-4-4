[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 495](https://www.onixs.biz/fix-dictionary/4.4/tagNum_495.html)

# FIX 4.4 : TaxAdvantageType <495> field

**Type:** [int](https://www.onixs.biz/fix-dictionary/4.4/index.html#int)

## Description

For CIV - a code identifying the type of tax exempt account in which purchased shares/units are to be held.

0 = None/Not Applicable (default)

1 = Maxi ISA (UK)

2 = TESSA (UK)

3 = Mini Cash ISA (UK)

4 = Mini Stocks and Shares ISA (UK)

5 = Mini Insurance ISA (UK)

6 = Current year payment (US)

7 = Prior year payment (US)

8 = Asset transfer (US)

9 = Employee - prior year (US)

10 = Employee - current year (US)

11 = Employer - prior year (US)

12 = Employer - current year (US)

13 = Non-fund prototype IRA (US)

14 = Non-fund qualified plan (US)

15 = Defined contribution plan (US)

16 = Individual Retirement Account (US)

17 = Individual Retirement Account - Rollover (US)

18 = KEOGH (US)

19 = Profit Sharing Plan (US)

20 = 401K (US)

21 = Self-Directed IRA (US)

22 = 403(b) (US)

23 = 457 (US)

24 = Roth IRA (fund prototype) (US)

25 = Roth IRA (non-prototype) (US)

26 = Roth Conversion IRA (fund prototype) (US)

27 = Roth Conversion IRA (non-prototype) (US)

28 = Education IRA (fund prototype) (US)

29 = Education IRA (non-prototype) (US)

30 - 998 are reserved for future use by recognized taxation authorities

999 = Other

values above 1000 are available for use by private agreement among counterparties

## Used In

- [Registration Instructions <o>](https://www.onixs.biz/fix-dictionary/4.4/msgType_o_111.html)

