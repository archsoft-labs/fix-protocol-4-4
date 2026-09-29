[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 871](https://www.onixs.biz/fix-dictionary/4.4/tagNum_871.html)

# FIX 4.4 : InstrAttribType <871> field

**Type:** [int](https://www.onixs.biz/fix-dictionary/4.4/index.html#int)

## Description

Code to represent the type of instrument attribute

Valid values:

1 = Flat (securities pay interest on a current basis but are traded without interest)

2 = Zero coupon

3 = Interest bearing (for Euro commercial paper when not issued at discount)

4 = No periodic payments

5 = Variable rate

6 = Less fee for put

7 = Stepped coupon

8 = Coupon period (if not semi-annual). Supply redemption date in the [InstrAttribValue <872>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_872.html) field

9 = When [and if] issued

10 = Original issue discount

11 = Callable, puttable

12 = Escrowed to Maturity

13 = Escrowed to redemption date - callable. Supply redemption date in the [InstrAttribValue <872>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_872.html) field

14 = Prerefunded

15 = In default

16 = Unrated

17 = Taxable

18 = Indexed

19 = Subject to Alternative Minimum Tax

20 = Original issue discount price. Supply price in the [InstrAttribValue <872>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_872.html) field

21 = Callable below maturity value

22 = Callable without notice by mail to holder unless registered

99 = Text. Supply the text of the attribute or disclaimer in the [InstrAttribValue <872>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_872.html) field

## Used In

- [<InstrumentExtension>](https://www.onixs.biz/fix-dictionary/4.4/compBlock_InstrumentExtension.html)

