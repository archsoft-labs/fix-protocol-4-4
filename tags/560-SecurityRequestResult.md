[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 560](https://www.onixs.biz/fix-dictionary/4.4/tagNum_560.html)

# FIX 4.4 : SecurityRequestResult <560> field

**Type:** [int](https://www.onixs.biz/fix-dictionary/4.4/index.html#int)

## Description

The results returned to a Security Request message

Valid values:

0 = Valid request

1 = Invalid or unsupported request

2 = No instruments found that match selection criteria

3 = Not authorized to retrieve instrument data

4 = [<Instrument>](https://www.onixs.biz/fix-dictionary/4.4/compBlock_Instrument.html) data temporarily unavailable

5 = Request for instrument data not supported

## Used In

- [Derivative Security List <AA>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AA_6565.html)
- [Security List <y>](https://www.onixs.biz/fix-dictionary/4.4/msgType_y_121.html)

