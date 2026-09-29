[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 808](https://www.onixs.biz/fix-dictionary/4.4/tagNum_808.html)

# FIX 4.4 : AllocIntermedReqType <808> field

**Type:** [int](https://www.onixs.biz/fix-dictionary/4.4/index.html#int)

## Description

Response to allocation to be communicated to a counterparty through an intermediary, i.e. clearing house. Used in conjunction  with [AllocType <626>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_626.html) = "Request to Intermediary" and [AllocReportType <794>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_794.html) = "Request to Intermediary"

Valid values:

1 = Pending Accept

2 = Pending Release

3 = Pending Reversal

4 = Accept

5 = Block Level Reject

6 = Account Level Reject

## Used In

- [Allocation Report <AS>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AS_6583.html)
- [Allocation Report Ack <AT>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AT_6584.html)
- [Allocation Instruction <J>](https://www.onixs.biz/fix-dictionary/4.4/msgType_J_74.html)
- [Allocation Instruction Ack <P>](https://www.onixs.biz/fix-dictionary/4.4/msgType_P_80.html)

