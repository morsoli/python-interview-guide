from urllib.parse import parse_qs
from random import randint
# 1.确认python版本
# 2.遵循PEP8风格
# 3.了解bytes、str与unicode的区别

# 接受bytes或str,总是返回str
def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value

# 接受bytes或str,总是返回bytes
def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value

# 4.用辅助函数取代复杂的表达式

my_values = parse_qs('red=5&blue=4&green=', keep_blank_values=True)
print(my_values)
# 待查询参数不存在或者查询参数的值为空白时返回0
def get_first_int(values, key, default=0):
    found = values.get(key, [''])
    if found[0]:
        found = int(found[0])
    else:
        found = default
    return found
print(get_first_int(my_values, 'blue', 0))

# 5.了解切割序列的方法(1.注意索引省略的情况；2.切片不考虑越界；3.利用切片操作对list赋值)
# 6.在单次切片操作内，不要同时指定start、end和stride(先做范围切割，再做步进切割，反过来也行，stride尽量为正)
# 7.用列表推导(list comprehension)来取代map和filter

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [x**2 for x in a if x % 2 == 0]
print(squares)

chile_ranks = {'ghost': 1, 'habanero': 2, 'cayene': 3}
rank_dict = {rank: name for name, rank in chile_ranks.items()}
chile_len_set = {len(name) for name in rank_dict.values()}
print(rank_dict)
print(chile_len_set)

# 8.不要使用含有两个以上表达式(两个条件，两个循环或者一个循环搭配一个条件)的列表推导
# 9.用生成器表达式(generator expression)来改写数据量较大(内存量激增，消耗大量内存)的列表推导

it = (x for x in a)
print(it)
print(next(it))
# 串在一起的生成器表达式执行速度很快
# 把某个声称其表达式所返回的迭代器，放在另一个生成器表达式的for子表达式中
roots = ((x, x**0.5) for x in it)
print(next(roots))  # 迭代器是有状态的
print(next(roots))

# 10.尽量用enumerate取代range(元素与下标相结合的序列遍历代码)

random_bits = 0
for i in range(8):
    if randint(0,1):
        random_bits |= 1 << i
print(random_bits)

flavor_list = ['vanilla', 'pecan', 'chocolate', 'strawbetery']
for i, flavor in enumerate(flavor_list,2):
    print('%d: %s'%(i, flavor))

# 11.用zip函数同时遍历两个迭代器(1.python3中的zip相当于生成器，会在遍历过程中逐次产生元组；2.如果提供的迭代器长度不等，zip会自动提前终止)

names = ['Cecilia', 'Lise', 'Marie']
letters = [len(n) for n in names]
longest_name = None
max_letters = 0
for name, count in zip(names, letters):
    if count > max_letters:
        longest_name = name
        max_letters = count
print(longest_name, max_letters)

# 12. 不要在for和while循环后面写else块
# 13. 合理利用try/except/else/finally结构中的每个代码块

def load_json_key(data, key):
    try:
        result_dict = json.loads(data)
    except ValueError as e:
        raise KeyError from e
    else:
        return result_dict[key]

UNDEFINED = object()
def divide_json(path):
    handle = open(path,'r+')
    try:
        data = handle.read()
        op = json.loads(data)
        value = (
            op['numerator'] /
            op['demominator']
        )
    except ZeroDivisionError as e:
        return UNDEFINED
    else:
        op['result'] = value
        result = json.dumps(op)
        handle.seek(0)
        handle.write(result)
        return value
    finally:
        handle.close()
from itertools import islice
from datetime import  datetime
import json
# 第一类对象（First-Class Object）
# 函数作为第一类对象（First-Class Object）,函数作为第一类对象，支持赋值给变量，作为参数传递给其它函数，作为其它函数的返回值，支持函数的嵌套，实现了__call__方法的类实例对象也可以当做函数被调用。是 Python 函数的一大特性。
# 函数身为一个对象，拥有对象模型的三个通用属性：id、类型、和值,
def foo(text):
     print(len(text))

foo("im ok")
print(id(foo))
print(type(foo))
print(foo)
'''
1746434188968
<class 'function'>
<function foo at 0x000001969F96E6A8>
'''
# 函数赋值给更多的变量，唯一变化的是该函数对象的引用计数不断地增加，本质上这些变量最终指向的都是同一个函数对象。
# 14.尽量用异常表示特殊情况，而不要返回None

def divide(a, b):
    try:
        return a/b
    except ZeroDivisionError as e:
        raise ValueError('invalid inputs') from e
divide(1, 1)

# 15.了解如何在闭包里使用外围作用域中的变量
 
def sort_priority(numbers, group):
    found = False
    def helper(x):
        #nonlocal found
        if x in group:
            found = True  #作用域bug(scoping bug),,python语言故意设计，防止函数的局部变量污染函数外面的模块
            return (0, x)
        return(1, x)
    numbers.sort(key=helper)
    return found
numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {2, 3, 5, 7}
print(sort_priority(numbers, group))
print(numbers)

# 16.考虑用生成器(generator)来改写直接返回列表的函数

def index_file(handle):
    offset = 0
    for line in handle:
        if line:
            yield offset
        for letter in line:
            offset += 1
            if letter == ' ':
                yield offset
with open(r'C:\Users\ASUS\Documents\我的坚果云\python学习笔记\Effective Python\address.txt', 'r') as f:
    it = index_file(f)
    results = islice(it, 0, 3)
    print(list(results))

# 17.在参数上面迭代时，要多加小心
# (Python的迭代器协议，描述了容器和迭代器应该如何与iter和next内置函数、for循环及相关表达式互相配合)
# (把__iter__方法实现为生成器，即可定义自己的容器类型)
class ReadVisits(object):
    def __init__(self, data_path):
        self.data_path = data_path
    def __iter__(self):
        with open(self.data_path) as f:
            for line in f:
                yield int(line)

def normalized(numbers):
    if iter(numbers) is iter(numbers):
        raise TypeError('必须提供容器类型')
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result
print(normalized([1,2,3]))

# 18.用数量可变的位置参数(*args,星号参数)
def log(message, *values):
    if not values:
        print(message)
    else:
        values_str = ','.join(str(x) for x in values)
        print('%s: %s'%(message, values_str))
log('my birth',9,12,98)
log('no values')

# 19.用关键字参数来表示可选的行为
# 20.用None和文档字符串来描述具有动态默认值的参数
#(例如打印日志消息时，要把相关事件的记录时间也标注在这条消息中)
def log(message, when = None):
    '''
    args:
    message: message to print
    when: datetime of when the message occurred>
         Default to the percent time.
    '''
    when = datetime.now() if when is None else when
    print('%s: %s'%(when, message))
log('hi there')

def decode(data, default=None):
    '''
    Load JSON data from a string.

    Args:
    data: JSON data to decode
    default: Value to return if decoding fails
           Default to an empty dictinary
    '''
    if default is None: # if 动态生成过程
        default = {}
    try:
        return json.loads(data)
    except ValueError:
        return default
         
# 21.用只能以关键字形式指定的参数来确保代码明晰
def safe_division(number, divisor, *, ignore_overflow = False, ignore_zero_division = False):
    print(ignore_overflow)
safe_division(1,2)
# 2.函数注释
def fun1(a:'spam',b:(1,2),c:float)->int:
    return a+b+c
print(fun1(1,2,3))
# 函数对象有一个名为 __annotations__ 的属性，它是一个映射（dict），
# 用于将每个参数名（key）映射到其相关的注释（value）。
print(fun1.__annotations__)
# 3.匿名函数:lambda是单一的表达式,
# 程序一次行使用，不需要定义函数名，节省内存中变量定义空间
L = [
    lambda x: x**2,
    lambda x: x**3,
    lambda x: x**4
]
for f in L:
    print(f(2))
# 4.函数式编程工具filter与reduce,map
from functools import reduce
print(reduce((lambda x,y:x+y),[1,2,3,4,5],5))

