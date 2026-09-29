[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 530](https://www.onixs.biz/fix-dictionary/4.4/tagNum_530.html)

# FIX 4.4 : MassCancelRequestType <530> field

**Type:** [char](https://www.onixs.biz/fix-dictionary/4.4/index.html#char)

## Description

Specifies scope of [Order Mass Cancel Request <q>](https://www.onixs.biz/fix-dictionary/4.4/msgType_q_113.html).

Valid values:

1 = Cancel orders for a security

2 = Cancel orders for an Underlying security

3 = Cancel orders for a [Product <460>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_460.html)

4 = Cancel orders for a [CFICode <461>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_461.html)

5 = Cancel orders for a [SecurityType <167>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_167.html)

6 = Cancel orders for a trading session

7 = Cancel all orders

## Used In

- [Order Mass Cancel Request <q>](https://www.onixs.biz/fix-dictionary/4.4/msgType_q_113.html)
- [Order Mass Cancel Report <r>](https://www.onixs.biz/fix-dictionary/4.4/msgType_r_114.html)

