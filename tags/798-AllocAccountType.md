[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 798](https://www.onixs.biz/fix-dictionary/4.4/tagNum_798.html)

# FIX 4.4 : AllocAccountType <798> field

**Type:** [int](https://www.onixs.biz/fix-dictionary/4.4/index.html#int)

## Description

Type of account associated with a confirmation or other trade-level message

Valid values:

1 = Account is carried on customer Side of Books

2 = Account is carried on non-Customer Side of books

3 = House Trader

4 = Floor Trader

6 = Account is carried on non-customer side of books and is cross margined

7 = Account is house trader and is cross margined

8 = Joint Backoffice Account (JBO)

## Used In

- [Confirmation <AK>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AK_6575.html)
- [Confirmation Request <BH>](https://www.onixs.biz/fix-dictionary/4.4/msgType_BH_6672.html)

