[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 550](https://www.onixs.biz/fix-dictionary/4.4/tagNum_550.html)

# FIX 4.4 : CrossPrioritization <550> field

**Type:** [int](https://www.onixs.biz/fix-dictionary/4.4/index.html#int)

## Description

Indicates if one side or the other of a cross order should be prioritized.

0 = None

1 = Buy side is prioritized

2 = Sell side is prioritized

The definition of prioritization is left to the market. In some markets prioritization means which side of the cross order is applied to the market first. In other markets - prioritization may mean that the prioritized side is fully executed (sometimes referred to as the side being protected).

## Used In

- [New Order Cross <s>](https://www.onixs.biz/fix-dictionary/4.4/msgType_s_115.html)
- [Cross Order Cancel/Replace Request <t>](https://www.onixs.biz/fix-dictionary/4.4/msgType_t_116.html)
- [Cross Order Cancel Request <u>](https://www.onixs.biz/fix-dictionary/4.4/msgType_u_117.html)

