[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 728](https://www.onixs.biz/fix-dictionary/4.4/tagNum_728.html)

# FIX 4.4 : PosReqResult <728> field

**Type:** [int](https://www.onixs.biz/fix-dictionary/4.4/index.html#int)

## Description

Result of [Request For Positions <AN>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AN_6578.html)

Valid values:

0 = Valid Request

1 = Invalid or unsupported Request

2 = No positions found that match criteria

3 = Not authorized to request positions

4 = Request for Position not supported

99 = Other (use [Text <58>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_58.html) in conjunction with this code for an explanation)

4000+ Reserved and available for bi-laterally agreed upon user-defined values

## Used In

- [Request for Positions Ack <AO>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AO_6579.html)
- [Position Report <AP>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AP_6580.html)

