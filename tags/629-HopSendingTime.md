[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 629](https://www.onixs.biz/fix-dictionary/4.4/tagNum_629.html)

# FIX 4.4 : HopSendingTime <629> field

**Type:** [UTCTimestamp](https://www.onixs.biz/fix-dictionary/4.4/index.html#UTCTimestamp)

## Description

Time that [HopCompID <628>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_628.html) sent the message. It is recommended that this value be the [SendingTime <52>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_52.html) of the message sent by the third party.

Applicable when messages are communicated/re-distributed via third parties which function as service bureaus or "hubs". Only applicable if [OnBehalfOfCompID <115>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_115.html) is being used.

