[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 422](https://www.onixs.biz/fix-dictionary/4.4/tagNum_422.html)

# FIX 4.4 : TotNoStrikes <422> field

**Type:** [int](https://www.onixs.biz/fix-dictionary/4.4/index.html#int)

## Description

Total number of strike price entries across all messages. Should be the sum of all [NoStrikes <428>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_428.html) in each message that has repeating strike price entries related to the same [ListID <66>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_66.html). Used to support fragmentation.

## Used In

- [List Strike Price <m>](https://www.onixs.biz/fix-dictionary/4.4/msgType_m_109.html)

