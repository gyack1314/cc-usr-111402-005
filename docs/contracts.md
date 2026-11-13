# 资料及接口契约

块为plain(values)或dict(dictionary,codes,valid)，valid=false时codes可为任意整数且不得解引用；有效码必须在字典范围。dictionary允许重复文本，空串是合法值；本期文本不做Unicode归一。collation=codepoint或casefold，casefold只用于等值、分组与连接的等价键，输出代表值取相等组中UTF8字节序最小原值。过滤eq/ne按该collation且null为UNKNOWN，group的null为单独组，join的null不匹配。dictionary.py提供块验证和完整解码慢路径，没有编码态算子。

所有记录为合成仓资料；data/source.json保存原始字段和身份。storage.py负责摘要读取，table.py保存独立关系版本，relations.py保留SQL三值和袋语义。inspect只调用现有基础接口，不提供新增查询或管理能力。
