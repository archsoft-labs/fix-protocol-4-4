[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 814](https://www.onixs.biz/fix-dictionary/4.4/tagNum_814.html)

# FIX 4.4 : ApplQueueResolution <814> field

**Type:** [int](https://www.onixs.biz/fix-dictionary/4.4/index.html#int)

## Description

Resolution taken when [ApplQueueDepth <813>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_813.html) exceeds [ApplQueueMax <812>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_812.html) or system specified maximum queue size.

Valid values:

0 = No action taken

1 = Queue flushed

2 = Overlay last

3 = End session

## Used In

- [Market Data - Snapshot/Full Refresh <W>](https://www.onixs.biz/fix-dictionary/4.4/msgType_W_87.html)
- [Market Data - Incremental Refresh <X>](https://www.onixs.biz/fix-dictionary/4.4/msgType_X_88.html)

