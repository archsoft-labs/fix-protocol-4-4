[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 169](https://www.onixs.biz/fix-dictionary/4.4/tagNum_169.html)

# FIX 4.4 : StandInstDbType <169> field

**Type:** [int](https://www.onixs.biz/fix-dictionary/4.4/index.html#int)

## Description

Identifies the Standing Instruction database used

Valid values:

0 = Other

1 = DTC SID

2 = Thomson ALERT

3 = A Global Custodian ([StandInstDbName <170>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_170.html) must be provided)

4 = AccountNet

## Used In

- [<SettlInstructionsData>](https://www.onixs.biz/fix-dictionary/4.4/compBlock_SettlInstructionsData.html)
- [Settlement Instruction Request <AV>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AV_6586.html)

