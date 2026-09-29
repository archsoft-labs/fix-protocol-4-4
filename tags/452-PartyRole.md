[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 452](https://www.onixs.biz/fix-dictionary/4.4/tagNum_452.html)

# FIX 4.4 : PartyRole <452> field

**Type:** [int](https://www.onixs.biz/fix-dictionary/4.4/index.html#int)

## Description

Identifies the type or role of the [PartyID <448>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_448.html) specified.

See "[Appendix 6-G – Use of <Parties> Component Block"](https://www.onixs.biz/fix-dictionary/4.4/app_6_g.html)

Valid values:

1 = [Executing Firm](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#ExecutingFirm) (formerly FIX 4.2 ExecBroker)

2 = [Broker of Credit](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#BrokerOfCredit) (formerly FIX 4.2 BrokerOfCredit)

3 = [Client ID](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#ClientID) (formerly FIX 4.2 ClientID)

4 = [Clearing Firm](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#ClearingFirm) (formerly FIX 4.2 ClearingFirm)

5 = [Investor ID](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#InvestorID)

6 = [Introducing Firm](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#IntroducingFirm)

7 = [Entering Firm](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#EnteringFirm)

8 = [Locate/Lending Firm](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#LocateLendingFirm) (for short-sales)

9 = [Fund manager Client ID (for CIV)](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#FundManagerClientID)

10 = [Settlement Location](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#SettlementLocation) (formerly FIX 4.2 SettlLocation)

11 = [Order Origination Trader](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#OrderOriginationTrader) (associated with Order Origination Firm - e.g. trader who initiates/submits the order)

12 = [Executing Trader](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#ExecutingTrader) (associated with Executing Firm - actually executes)

13 = [Order Origination Firm](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#OrderOriginationFirm) (e.g. buyside firm)

14 = [Giveup Clearing Firm](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#GiveupClearingFirm) (firm to which trade is given up)

15 = [Correspondant Clearing Firm](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#CorrespondentClearingFirm)

16 = [Executing System](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#ExecutingSystem)

17 = [Contra Firm](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#ContraFirm)

18 = [Contra Clearing Firm](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#ContraClearingFirm)

19 = [Sponsoring Firm](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#SponsoringFirm)

20 = [Underlying Contra Firm](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#UnderlyingContraFirm)

21 = [Clearing Organization](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#ClearingOrganization)

22 = [Exchange](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#Exchange)

24 = [Customer Account](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#CustomerAccount)

25 = [Correspondent Clearing Organization](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#CorrespondentClearingOrganization)

26 = [Correspondent Broker](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#CorrespondentBroker)

27 = Buyer/Seller (Receiver/Deliverer)

28 = Custodian

29 = Intermediary

30 = Agent

31 = Sub custodian

32 = Beneficiary

33 = Interested party

34 = Regulatory body

35 = [Liquidity provider](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#LiquidityProvider)

36 = [Entering Trader](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#EnteringTrader)

37 = [Contra Trader](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#ContraTrader)

38 = [Position Account](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#PositionAccount)

## Used In

- [<Parties>](https://www.onixs.biz/fix-dictionary/4.4/compBlock_Parties.html)

