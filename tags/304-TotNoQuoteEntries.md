[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 304](https://www.onixs.biz/fix-dictionary/4.4/tagNum_304.html)

# FIX 4.4 : TotNoQuoteEntries <304> field

**Type:** [int](https://www.onixs.biz/fix-dictionary/4.4/index.html#int)

## Description

Total number of quotes for the quote set across all messages. Should be the sum of all [NoQuoteEntries <295>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_295.html) in each message that has repeating quotes that are part of the same quote set.

(Prior to FIX 4.4 this field was named TotQuoteEntries)

## Used In

- [Mass Quote Acknowledgement <b>](https://www.onixs.biz/fix-dictionary/4.4/msgType_b_98.html)
- [Mass Quote <i>](https://www.onixs.biz/fix-dictionary/4.4/msgType_i_105.html)

