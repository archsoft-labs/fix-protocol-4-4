[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 206](https://www.onixs.biz/fix-dictionary/4.4/tagNum_206.html)

# FIX 4.4 : OptAttribute <206> field

**Type:** [char](https://www.onixs.biz/fix-dictionary/4.4/index.html#char)

## Description

Can be used for [SecurityType <167>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_167.html)=OPT to identify a particular security.

Valid values vary by [SecurityExchange <207>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_207.html):

*** REPLACED values - See [Appendix 6-F: 7.Replaced values: OptAttribute(tag 206) with values in CFICode(tag 461) [Replaced in FIX 4.3]](https://www.onixs.biz/fix-dictionary/4.4/app_6_f.html#7) ***

~~For Exchange: MONEP (Paris)~~

~~L = Long (a.k.a. "American")~~

~~S = Short (a.k.a. "European")~~

For Exchanges: DTB (Frankfurt), HKSE (Hong Kong), and SOFFEX (Zurich)

0-9 = single digit "version" number assigned by exchange following capital adjustments (0=current, 1=prior, 2=prior to 1, etc).

## Used In

- [<Instrument>](https://www.onixs.biz/fix-dictionary/4.4/compBlock_Instrument.html)

