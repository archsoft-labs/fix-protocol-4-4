[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 321](https://www.onixs.biz/fix-dictionary/4.4/tagNum_321.html)

# FIX 4.4 : SecurityRequestType <321> field

**Type:** [int](https://www.onixs.biz/fix-dictionary/4.4/index.html#int)

## Description

Type of [Security Definition Request <c>](https://www.onixs.biz/fix-dictionary/4.4/msgType_c_99.html).

Valid values:

0 = Request Security identity and specifications

1 = Request Security identity for the specifications provided (Name of the security is not supplied)

2 = Request List Security Types

3 = Request List Securities (Can be qualified with [Symbol <55>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_55.html), [SecurityType <167>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_167.html), [TradingSessionID <336>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_336.html), [SecurityExchange <207>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_207.html). If provided then only list Securities for the specific type)

## Used In

- [Security Definition Request <c>](https://www.onixs.biz/fix-dictionary/4.4/msgType_c_99.html)

