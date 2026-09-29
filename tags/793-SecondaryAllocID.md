[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 793](https://www.onixs.biz/fix-dictionary/4.4/tagNum_793.html)

# FIX 4.4 : SecondaryAllocID <793> field

**Type:** [String](https://www.onixs.biz/fix-dictionary/4.4/index.html#String)

## Description

Secondary allocation identifier. Unlike the [AllocID <70>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_70.html), this can be shared across a number of allocation instruction or allocation report messages, thereby making it possible to pass an identifier for an original allocation message on multiple messages (e.g. from one party to a second to a third, across cancel and replace messages etc.).

## Used In

- [Confirmation <AK>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AK_6575.html)
- [Allocation Report <AS>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AS_6583.html)
- [Allocation Report Ack <AT>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AT_6584.html)
- [Confirmation Request <BH>](https://www.onixs.biz/fix-dictionary/4.4/msgType_BH_6672.html)
- [Allocation Instruction <J>](https://www.onixs.biz/fix-dictionary/4.4/msgType_J_74.html)
- [Allocation Instruction Ack <P>](https://www.onixs.biz/fix-dictionary/4.4/msgType_P_80.html)

