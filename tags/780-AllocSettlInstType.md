[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 780](https://www.onixs.biz/fix-dictionary/4.4/tagNum_780.html)

# FIX 4.4 : AllocSettlInstType <780> field

**Type:** [int](https://www.onixs.biz/fix-dictionary/4.4/index.html#int)

## Description

Used to indicate whether settlement instructions are provided on an [Allocation Instruction <J>](https://www.onixs.biz/fix-dictionary/4.4/msgType_J_74.html) message, and if not, how they are to be derived.

Valid values:

0 = use default instructions

1 = derive from parameters provided

2 = full details provided

3 = SSI db ids provided

4 = phone for instructions

## Used In

- [Allocation Report <AS>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AS_6583.html)
- [Allocation Instruction <J>](https://www.onixs.biz/fix-dictionary/4.4/msgType_J_74.html)

