[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 461](https://www.onixs.biz/fix-dictionary/4.4/tagNum_461.html)

# FIX 4.4 : CFICode <461> field

**Type:** [String](https://www.onixs.biz/fix-dictionary/4.4/index.html#String)

## Description

Indicates the type of security using ISO 10962 standard, Classification of Financial Instruments (CFI code) values. ISO 10962 is maintained by ANNA (Association of National Numbering Agencies) acting as Registration Authority. See [Appendix 6-B: FIX Fields Based Upon Other Standards](https://www.onixs.biz/fix-dictionary/4.4/app_6_b.html). See also the [Product <460>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_460.html) and [SecurityType <167>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_167.html) fields. It is recommended that [CFICode <461>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_461.html) be used instead of [SecurityType <167>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_167.html) for non-Fixed Income instruments.

A subset of possible values applicable to FIX usage are identified in [Appendix 6-D: CFICode Usage - ISO 10962 Classification of Financial Instruments (CFI code)](https://www.onixs.biz/fix-dictionary/4.4/app_6_d.html)

## Used In

- [<Instrument>](https://www.onixs.biz/fix-dictionary/4.4/compBlock_Instrument.html)
- [Settlement Instruction Request <AV>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AV_6586.html)
- [Settlement Instructions <T>](https://www.onixs.biz/fix-dictionary/4.4/msgType_T_84.html)
- [Security Types <w>](https://www.onixs.biz/fix-dictionary/4.4/msgType_w_119.html)

