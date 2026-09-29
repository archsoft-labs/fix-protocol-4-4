[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 549](https://www.onixs.biz/fix-dictionary/4.4/tagNum_549.html)

# FIX 4.4 : CrossType <549> field

**Type:** [int](https://www.onixs.biz/fix-dictionary/4.4/index.html#int)

## Description

Type of cross being submitted to a market

Valid values:

1 = Cross Trade which is executed completely or not. Both sides are treated in the same manner. This is equivalent to an All or None.

2 = Cross Trade which is executed partially and the rest is cancelled. One side is fully executed, the other side is partially executed with the remainder being cancelled. This is equivalent to an Immediate or Cancel on the other side. Note: The [CrossPrioritization <550>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_550.html) field may be used to indicate which side should fully execute in this scenario.

3 = Cross trade which is partially executed with the unfilled portions remaining active. One side of the cross is fully executed (as denoted with the [CrossPrioritization <550>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_550.html) field), but the unfilled portion remains active.

4 = Cross trade is executed with existing orders with the same price. In the case other orders exist with the same price, the quantity of the Cross is executed against the existing orders and quotes, the remainder of the cross is executed against the other side of the cross. The two sides potentially have different quantities.

## Used In

- [Execution Report <8>](https://www.onixs.biz/fix-dictionary/4.4/msgType_8_8.html)
- [New Order Cross <s>](https://www.onixs.biz/fix-dictionary/4.4/msgType_s_115.html)
- [Cross Order Cancel/Replace Request <t>](https://www.onixs.biz/fix-dictionary/4.4/msgType_t_116.html)
- [Cross Order Cancel Request <u>](https://www.onixs.biz/fix-dictionary/4.4/msgType_u_117.html)

