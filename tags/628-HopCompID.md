[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 628](https://www.onixs.biz/fix-dictionary/4.4/tagNum_628.html)

# FIX 4.4 : HopCompID <628> field

**Type:** [String](https://www.onixs.biz/fix-dictionary/4.4/index.html#String)

## Description

Assigned value used to identify the third party firm which delivered a specific message either from the firm which originated the message or from another third party (if multiple "hops" are performed). It is recommended that this value be the [SenderCompID <49>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_49.html) of the third party.

Applicable when messages are communicated/re-distributed via third parties which function as service bureaus or "hubs". Only applicable if [OnBehalfOfCompID <115>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_115.html) is being used.

