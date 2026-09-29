[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 370](https://www.onixs.biz/fix-dictionary/4.4/tagNum_370.html)

# FIX 4.4 : OnBehalfOfSendingTime <370> field

**Type:** [UTCTimestamp](https://www.onixs.biz/fix-dictionary/4.4/index.html#UTCTimestamp)

## Description

No longer used as of FIX.4.4. Included here for reference to prior versions.

See [Appendix 6-F: 13.Removed Deprecated Field: OnBehalfOfSendingTime (tag 370) [Deprecated and Replaced in FIX 4.3, Removed in FIX 4.4]](https://www.onixs.biz/fix-dictionary/4.4/app_6_f.html#13)

Used when a message is sent via a "hub" or "service bureau". If A sends to Q (the hub) who then sends to B via a separate FIX session, then when Q sends to B the value of this field should represent the [SendingTime <52>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_52.html) on the message A sent to Q. (always expressed in UTC (Universal Time Coordinated, also known as "GMT")

