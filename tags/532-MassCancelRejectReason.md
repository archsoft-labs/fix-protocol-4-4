[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 532](https://www.onixs.biz/fix-dictionary/4.4/tagNum_532.html)

# FIX 4.4 : MassCancelRejectReason <532> field

**Type:** [char](https://www.onixs.biz/fix-dictionary/4.4/index.html#char)

## Description

Reason [Order Mass Cancel Request <q>](https://www.onixs.biz/fix-dictionary/4.4/msgType_q_113.html) was rejected

Valid values:

0 = Mass Cancel Not Supported

1 = Invalid or unknown Security

2 = Invalid or unknown Underlying security

3 = Invalid or unknown [Product <460>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_460.html)

4 = Invalid or unknown [CFICode <461>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_461.html)

5 = Invalid or unknown [SecurityType <167>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_167.html)

6 = Invalid or unknown trading session

99 = Other

## Used In

- [Order Mass Cancel Report <r>](https://www.onixs.biz/fix-dictionary/4.4/msgType_r_114.html)

