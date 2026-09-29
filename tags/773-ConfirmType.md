[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 773](https://www.onixs.biz/fix-dictionary/4.4/tagNum_773.html)

# FIX 4.4 : ConfirmType <773> field

**Type:** [int](https://www.onixs.biz/fix-dictionary/4.4/index.html#int)

## Description

Identifies the type of [Confirmation <AK>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AK_6575.html) message being sent.

Valid values:

1 = Status

2 = Confirmation

3 = [Confirmation Request <BH>](https://www.onixs.biz/fix-dictionary/4.4/msgType_BH_6672.html) Rejected (reason can be stated in [Text <58>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_58.html) field)

## Used In

- [Confirmation <AK>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AK_6575.html)
- [Confirmation Request <BH>](https://www.onixs.biz/fix-dictionary/4.4/msgType_BH_6672.html)

