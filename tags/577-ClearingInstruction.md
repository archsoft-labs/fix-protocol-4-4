[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 577](https://www.onixs.biz/fix-dictionary/4.4/tagNum_577.html)

# FIX 4.4 : ClearingInstruction <577> field

**Type:** [int](https://www.onixs.biz/fix-dictionary/4.4/index.html#int)

## Description

Eligibility of this trade for clearing and central counterparty processing

Valid values:

0 = process normally

1 = exclude from all netting

2 = bilateral netting only

3 = ex clearing

4 = special trade

5 = multilateral netting

6 = clear against central counterparty

7 = exclude from central counterparty

8 = Manual mode (pre-posting and/or pre-giveup)

9 = Automatic posting mode (trade posting to the position account number specified)

10 = Automatic give-up mode (trade give-up to the give-up destination number specified)

11 = Qualified Service Representative (QSR)

12 = Customer Trade

13 = Self clearing

values above 4000 are reserved for agreement between parties

## Used In

- [Trade Capture Report <AE>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AE_6569.html)
- [Allocation Report <AS>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AS_6583.html)
- [Allocation Instruction <J>](https://www.onixs.biz/fix-dictionary/4.4/msgType_J_74.html)

