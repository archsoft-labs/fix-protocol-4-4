[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 935](https://www.onixs.biz/fix-dictionary/4.4/tagNum_935.html)

# FIX 4.4 : NetworkRequestType <935> field

**Type:** [int](https://www.onixs.biz/fix-dictionary/4.4/index.html#int)

## Description

Indicates the type and level of details required for a Network Status Request Message

Boolean logic applies EG If you want to subscribe for changes to certain id's then [UserRequestType <924>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_924.html) = 10 (8+2), Snapshot for certain ID's = 9 (8+1)

Valid values:

1 = Snapshot

2 = Subscribe

4 = Stop subscribing

8 = Level of detail, then [NoCompIDs <936>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_936.html) becomes required

## Used In

- [Network Counterparty System Status Request <BC>](https://www.onixs.biz/fix-dictionary/4.4/msgType_BC_6667.html)

