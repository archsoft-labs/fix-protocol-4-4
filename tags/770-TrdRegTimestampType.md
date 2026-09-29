[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 770](https://www.onixs.biz/fix-dictionary/4.4/tagNum_770.html)

# FIX 4.4 : TrdRegTimestampType <770> field

**Type:** [int](https://www.onixs.biz/fix-dictionary/4.4/index.html#int)

## Description

Traded / Regulatory timestamp type.

Valid values:

1 = [Execution Time](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#ExecutionTime)

2 = [Time In](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#TimeIn)

3 = [Time Out](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#TimeOut)

4 = [Broker Receipt](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#BrokerReceipt)

5 = [Broker Execution](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#BrokerExecution)

Note of Applicability: values are required in US futures markets by the CFTC to support computerized trade reconstruction.

## Used In

- [<TrdRegTimestamps>](https://www.onixs.biz/fix-dictionary/4.4/compBlock_TrdRegTimestamps.html)

