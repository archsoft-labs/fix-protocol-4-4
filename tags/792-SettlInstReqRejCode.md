[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 792](https://www.onixs.biz/fix-dictionary/4.4/tagNum_792.html)

# FIX 4.4 : SettlInstReqRejCode <792> field

**Type:** [int](https://www.onixs.biz/fix-dictionary/4.4/index.html#int)

## Description

Identifies reason for rejection (of a [Settlement Instruction Request <AV>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AV_6586.html) message).

Valid values:

0 = unable to process request (e.g. database unavailable)

1 = unknown account

2 = no matching settlement instructions found

99 = other

## Used In

- [Settlement Instructions <T>](https://www.onixs.biz/fix-dictionary/4.4/msgType_T_84.html)

