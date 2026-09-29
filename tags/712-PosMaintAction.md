[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 712](https://www.onixs.biz/fix-dictionary/4.4/tagNum_712.html)

# FIX 4.4 : PosMaintAction <712> field

**Type:** [int](https://www.onixs.biz/fix-dictionary/4.4/index.html#int)

## Description

Maintenance Action to be performed.

Valid values:

1 = New: used to increment the overall transaction quantity

2 = Replace: used to override the overall transaction quantity or specific add messages based on the reference id

3 = Cancel: used to remove the overall transaction or specific add messages based on reference id

## Used In

- [Position Maintenance Request <AL>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AL_6576.html)
- [Position Maintenance Report <AM>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AM_6577.html)

