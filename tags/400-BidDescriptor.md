[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 400](https://www.onixs.biz/fix-dictionary/4.4/tagNum_400.html)

# FIX 4.4 : BidDescriptor <400> field

**Type:** [String](https://www.onixs.biz/fix-dictionary/4.4/index.html#String)

## Description

BidDescriptor value. Usage depends upon [BidDescriptorType <399>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_399.html).

If BidDescriptorType = 1

Industrials etc - Free text

If BidDescriptorType = 2

"FR" etc - ISO [Country <421>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_421.html) Codes

If BidDescriptorType = 3

FT100, FT250, STOX - Free text

## Used In

- [Bid Request <k>](https://www.onixs.biz/fix-dictionary/4.4/msgType_k_107.html)

