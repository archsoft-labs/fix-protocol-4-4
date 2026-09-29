[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 310](https://www.onixs.biz/fix-dictionary/4.4/tagNum_310.html)

# FIX 4.4 : UnderlyingSecurityType <310> field

**Type:** [String](https://www.onixs.biz/fix-dictionary/4.4/index.html#String)

## Description

Underlying security's SecurityType.

Valid values: see [SecurityType <167>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_167.html) field

The following applies when used in conjunction with [SecurityType <167>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_167.html)=REPO.

Represents the general or specific type of security that underlies a financing agreement.

Valid values for [SecurityType <167>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_167.html)=REPO:

TREASURY = Federal government or treasury

PROVINCE = State, province, region, etc.

AGENCY = Federal agency

MORTGAGE = Mortgage passthrough

CP = Commercial paper

CORP = Corporate

EQUITY = Equity

SUPRA = Supra-national agency

CASH

If bonds of a particular issuer or country are wanted in an Order or are in the basket of an Execution and the [SecurityType <167>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_167.html) is not granular enough, include the [UnderlyingIssuer <306>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_306.html), [UnderlyingCountryOfIssue <592>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_592.html), UnderlyingProgram, UnderlyingRegType and/or [<UnderlyingStipulations>](https://www.onixs.biz/fix-dictionary/4.4/compBlock_UnderlyingStipulations.html) block e.g.:

[SecurityType <167>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_167.html)=REPO

[UnderlyingSecurityType <310>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_310.html)=MORTGAGE

[UnderlyingIssuer <306>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_306.html)=GNMA

or

[SecurityType <167>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_167.html)=REPO

[UnderlyingSecurityType <310>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_310.html)=AGENCY

[UnderlyingIssuer <306>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_306.html)=CA Housing Trust

[UnderlyingCountryOfIssue <592>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_592.html)=CA

or

[SecurityType <167>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_167.html)=REPO

[UnderlyingSecurityType <310>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_310.html)=CORP

[UnderlyingNoStipulations <887>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_887.html)=1

[UnderlyingStipulationType <888>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_888.html)=RATING

[UnderlyingStipulationValue <889>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_889.html)=>bbb-

## Used In

- [<UnderlyingInstrument>](https://www.onixs.biz/fix-dictionary/4.4/compBlock_UnderlyingInstrument.html)

