"""局部字典和普通值块的完整解码读取。"""
def decode(block):
    if block['kind']=='plain':
        if any(v is not None and not isinstance(v,str) for v in block['values']):raise ValueError('列值类型非法')
        return list(block['values'])
    if block['kind']!='dict':raise ValueError('块类型不支持')
    dictionary=block['dictionary'];codes=block['codes'];valid=block['valid']
    if any(not isinstance(v,str) for v in dictionary):raise ValueError('字典值类型非法')
    if len(codes)!=len(valid) or any(type(v) is not bool for v in valid):raise ValueError('有效位图不符')
    values=[]
    for code,visible in zip(codes,valid):
        if not visible:values.append(None);continue
        if type(code) is not int or not 0<=code<len(dictionary):raise ValueError('有效码越界')
        values.append(dictionary[code])
    return values

def inspect(data,storage,root):
    return {'collation':data['collation'],'decoded':{b['id']:decode(b) for b in data['blocks']}}
