[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 433](https://www.onixs.biz/fix-dictionary/4.4/tagNum_433.html)

# FIX 4.4 : ListExecInstType <433> field

**Type:** [char](https://www.onixs.biz/fix-dictionary/4.4/index.html#char)

## Description

Identifies the type of [ListExecInst <69>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_69.html).

Valid values:

1 = Immediate

2 = Wait for Execute Instruction (e.g. a [List Execute <L>](https://www.onixs.biz/fix-dictionary/4.4/msgType_L_76.html) message or phone call before proceeding with execution of the list)

3 = Exchange/switch CIV order - Sell driven

4 = Exchange/switch CIV order - Buy driven, cash top-up (i.e. additional cash will be provided to fulfil the order)

5 = Exchange/switch CIV order - Buy driven, cash withdraw (i.e. additional cash will not be provided to fulfil the order)

## Used In

- [New Order List <E>](https://www.onixs.biz/fix-dictionary/4.4/msgType_E_69.html)

