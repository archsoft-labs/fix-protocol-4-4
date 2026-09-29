[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 16](https://www.onixs.biz/fix-dictionary/4.4/tagNum_16.html)

# FIX 4.4 : EndSeqNo <16> field

**Type:** [SeqNum](https://www.onixs.biz/fix-dictionary/4.4/index.html#SeqNum)

## Description

Message sequence number of last message in range to be resent.  If request is for a single message [BeginSeqNo <7>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_7.html) = [EndSeqNo <16>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_16.html).  If request is for all messages subsequent to a particular message, [EndSeqNo <16>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_16.html) = 0 (representing infinity).

## Used In

- [Resend Request <2>](https://www.onixs.biz/fix-dictionary/4.4/msgType_2_2.html)

