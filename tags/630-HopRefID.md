[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 630](https://www.onixs.biz/fix-dictionary/4.4/tagNum_630.html)

# FIX 4.4 : HopRefID <630> field

**Type:** [SeqNum](https://www.onixs.biz/fix-dictionary/4.4/index.html#SeqNum)

## Description

Reference identifier assigned by [HopCompID <628>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_628.html) associated with the message sent. It is recommended that this value be the [MsgSeqNum <34>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_34.html) of the message sent by the third party.

Applicable when messages are communicated/re-distributed via third parties which function as service bureaus or "hubs". Only applicable if [OnBehalfOfCompID <115>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_115.html) is being used.

