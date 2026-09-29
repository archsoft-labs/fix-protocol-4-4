[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 507](https://www.onixs.biz/fix-dictionary/4.4/tagNum_507.html)

# FIX 4.4 : RegistRejReasonCode <507> field

**Type:** [int](https://www.onixs.biz/fix-dictionary/4.4/index.html#int)

## Description

Reason(s) why [Registration Instructions <o>](https://www.onixs.biz/fix-dictionary/4.4/msgType_o_111.html) has been rejected.

Possible values of reason code include:

1 = Invalid/unacceptable Account Type

2 = Invalid/unacceptable Tax Exempt Type

3 = Invalid/unacceptable [OwnershipType <517>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_517.html)

4 = Invalid/unacceptable [NoRegistDtls <473>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_473.html)

5 = Invalid/unacceptable Reg Seq No

6 = Invalid/unacceptable [RegistDetls <509>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_509.html)

7 = Invalid/unacceptable [MailingDtls <474>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_474.html)

8 = Invalid/unacceptable [MailingInst <482>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_482.html)

9 = Invalid/unacceptable Investor ID

10 = Invalid/unacceptable Investor ID Source

11 = Invalid/unacceptable [DateOfBirth <486>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_486.html)

12 = Invalid/unacceptable [InvestorCountryOfResidence <475>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_475.html)

13 = Invalid/unacceptable [NoDistribInsts <510>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_510.html)

14 = Invalid/unacceptable [DistribPercentage <512>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_512.html)

15 = Invalid/unacceptable [DistribPaymentMethod <477>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_477.html)

16 = Invalid/unacceptable [CashDistribAgentAcctName <502>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_502.html)

17 = Invalid/unacceptable [CashDistribAgentCode <499>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_499.html)

18 = Invalid/unacceptable [CashDistribAgentAcctNum <500>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_500.html)

99 = Other

The reason may be further amplified in the [RegistRejReasonCode <507>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_507.html) field.

## Used In

- [Registration Instructions Response <p>](https://www.onixs.biz/fix-dictionary/4.4/msgType_p_112.html)

