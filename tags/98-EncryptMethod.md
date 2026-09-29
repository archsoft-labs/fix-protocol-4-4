[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 98](https://www.onixs.biz/fix-dictionary/4.4/tagNum_98.html)

# FIX 4.4 : EncryptMethod <98> field

**Type:** [int](https://www.onixs.biz/fix-dictionary/4.4/index.html#int)

## Description

Method of encryption.

Valid values:

0 = None / other

1 = PKCS (proprietary)

2 = DES (ECB mode)

3 = PKCS/DES (proprietary)

4 = PGP/DES (defunct)

5 = PGP/DES-MD5 (see app note on FIX web site)

6 = PEM/DES-MD5 (see app note on FIX web site)

## Used In

- [Logon <A>](https://www.onixs.biz/fix-dictionary/4.4/msgType_A_65.html)

