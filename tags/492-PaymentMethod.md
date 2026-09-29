[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 492](https://www.onixs.biz/fix-dictionary/4.4/tagNum_492.html)

# FIX 4.4 : PaymentMethod <492> field

**Type:** [int](https://www.onixs.biz/fix-dictionary/4.4/index.html#int)

## Description

A code identifying the Settlement payment method.

1 = CREST

2 = NSCC

3 = Euroclear

4 = Clearstream

5 = Cheque

6 = Telegraphic Transfer

7 = FedWire

8 = Debit Card

9 = Direct Debit (BECS)

10 = Direct Credit (BECS)

11 = Credit Card

12 = ACH Debit

13 = ACH Credit

14 = BPAY

15 = High Value Clearing System (HVACS)

16 through 998 are reserved for future use

Values above 1000 are available for use by private agreement among counterparties

## Used In

- [Settlement Instructions <T>](https://www.onixs.biz/fix-dictionary/4.4/msgType_T_84.html)

