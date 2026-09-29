[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 563](https://www.onixs.biz/fix-dictionary/4.4/tagNum_563.html)

# FIX 4.4 : MultiLegRptTypeReq <563> field

**Type:** [int](https://www.onixs.biz/fix-dictionary/4.4/index.html#int)

## Description

Indicates the method of execution reporting requested by issuer of the order.

0 = Report by mulitleg security only (Do not report legs)

1 = Report by multileg security and by instrument legs belonging to the multileg security.

2 = Report by instrument legs belonging to the multileg security only (Do not report status of multileg security)

## Used In

- [New Order Multileg <AB>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AB_6566.html)
- [Multileg Order Cancel/Replace <AC>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AC_6567.html)

