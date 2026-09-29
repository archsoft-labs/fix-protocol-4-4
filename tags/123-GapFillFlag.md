[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 123](https://www.onixs.biz/fix-dictionary/4.4/tagNum_123.html)

# FIX 4.4 : GapFillFlag <123> field

**Type:** [Boolean](https://www.onixs.biz/fix-dictionary/4.4/index.html#Boolean)

## Description

Indicates that the [Sequence Reset <4>](https://www.onixs.biz/fix-dictionary/4.4/msgType_4_4.html) message is replacing administrative or application messages which will not be resent.

Valid values:

Y = [Gap Fill <4>](https://www.onixs.biz/fix-dictionary/4.4/msgType_4_4.html) message, [MsgSeqNum <34>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_34.html) field valid

N = [Sequence Reset <4>](https://www.onixs.biz/fix-dictionary/4.4/msgType_4_4.html), ignore [MsgSeqNum <34>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_34.html)

## Used In

- [Sequence Reset <4>](https://www.onixs.biz/fix-dictionary/4.4/msgType_4_4.html)

