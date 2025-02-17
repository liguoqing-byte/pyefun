"""

.. Hint::
    算数运算

.. literalinclude:: ../../../pyefun/arithmeticOperationBase_test.py
    :language: python
    :caption: 代码示例
    :linenos:
    :lines: 1-100

"""

import math
import random


def 四舍五入(欲被四舍五入的数值: float, 被舍入的位置: int):
    """
    调用格式： 〈双精度小数型〉 四舍五入 （双精度小数型 欲被四舍五入的数值，［整数型 被舍入的位置］） - 系统核心支持库->算术运算

    英文名称：round

    返回按照指定的方式进行四舍五入运算的结果数值。本命令为初级命令。

    参数<1>的名称为“欲被四舍五入的数值”，类型为“双精度小数型（double）”。

    参数<2>的名称为“被舍入的位置”，类型为“整数型（int）”，可以被省略。如果大于0，表示小数点右边应保留的位数；如果等于0，表示舍入到整数；如果小于0，表示小数点左边舍入到的位置。例如：四舍五入 (1056.65, 1) 返回 1056.7； 四舍五入 (1056.65, 0) 返回 1057； 四舍五入 (1056.65, -1) 返回 1060。如果省略本参数，则默认为0。

    操作系统需求： Windows、Linux

    """
    return round(欲被四舍五入的数值, 被舍入的位置)


def 取绝对值(双精度小数型: float):
    """
     调用格式： 〈双精度小数型〉 取绝对值 （双精度小数型 欲取其绝对值的数值） - 系统核心支持库->算术运算

     英文名称：abs

     如果所提供数值为字节型，则将直接返回该数值。本命令为初级命令。

     参数<1>的名称为“欲取其绝对值的数值”，类型为“双精度小数型（double）”。

     操作系统需求： Windows、Linux
    """
    return abs(双精度小数型)


def 取整(value):
    """
    调用格式： 〈整数型〉 取整 （双精度小数型 欲取整的小数） - 系统核心支持库->算术运算

    英文名称：int

    返回一个小数的整数部分。本命令与“绝对取整”命令不相同之处为：

    如果给定小数为负数，则本命令返回小于或等于该小数的第一个负整数，而“绝对取整”命令则会返回大于或等于该小数的第一个负整数。例如，本命令将 -7.8 转换成 -8，而“绝对取整”命令将 -7.8 转换成 -7。本命令为初级命令。

    参数<1>的名称为“欲取整的小数”，类型为“双精度小数型（double）”。

    操作系统需求： Windows、Linux
    """
    return int(value)


def 求次方(欲求次方数值: float, 次方数: float):
    """
     调用格式： 〈双精度小数型〉 求次方 （双精度小数型 欲求次方数值，双精度小数型 次方数） - 系统核心支持库->算术运算

     英文名称：pow

     返回指定数值的指定次方。本命令为初级命令。

     参数<1>的名称为“欲求次方数值”，类型为“双精度小数型（double）”。参数值指定欲求其某次方的数值。

     参数<2>的名称为“次方数”，类型为“双精度小数型（double）”。参数值指定对欲求次方数值的运算指数。

     操作系统需求： Windows、Linux
    """
    return pow(欲求次方数值, 次方数)


def 求平方根(欲求次方数值: float):
    """
     调用格式： 〈双精度小数型〉 求平方根 （双精度小数型 欲求其平方根的数值） - 系统核心支持库->算术运算

     英文名称：sqr

     返回指定参数的平方根。本命令为初级命令。

     参数<1>的名称为“欲求其平方根的数值”，类型为“双精度小数型（double）”。参数值如果小于零将导致计算错误。

     操作系统需求： Windows、Linux
    """
    return math.sqrt(欲求次方数值)


def 求正弦(欲进行计算的角: float):
    """
     调用格式： 〈双精度小数型〉 求正弦 （双精度小数型 欲进行计算的角） - 系统核心支持库->算术运算

     英文名称：sin

     返回指定角的正弦值。本命令为初级命令。

     参数<1>的名称为“欲进行计算的角”，类型为“双精度小数型（double）”。所使用单位为弧度。为了将角度转换成弧度，请将角度乘以 pi / 180。为了将弧度转换成角度，请将弧度乘以 180 / pi。如果参数值大于等于 2 的 63 次方，或者小于等于 -2 的 63 次方，将导致计算溢出。

     操作系统需求： Windows、Linux
    """
    return math.sin(欲进行计算的角)


def 求余弦(欲进行计算的角: float):
    """
     调用格式： 〈双精度小数型〉 求余弦 （双精度小数型 欲进行计算的角） - 系统核心支持库->算术运算

     英文名称：cos

     返回指定角的余弦值。本命令为初级命令。

     参数<1>的名称为“欲进行计算的角”，类型为“双精度小数型（double）”。所使用单位为弧度。为了将角度转换成弧度，请将角度乘以 pi / 180。为了将弧度转换成角度，请将弧度乘以 180 / pi。如果参数值大于等于 2 的 63 次方，或者小于等于 -2 的 63 次方，将导致计算溢出。

     操作系统需求： Windows、Linux
    """
    return math.cos(欲进行计算的角)


def 求正切(欲进行计算的角: float):
    """
     调用格式： 〈双精度小数型〉 求正切 （双精度小数型 欲进行计算的角） - 系统核心支持库->算术运算

     英文名称：tan

     返回指定角的正切值。本命令为初级命令。

     参数<1>的名称为“欲进行计算的角”，类型为“双精度小数型（double）”。所使用单位为弧度。为了将角度转换成弧度，请将角度乘以 pi / 180。为了将弧度转换成角度，请将弧度乘以 180 / pi。如果参数值大于等于 2 的 63 次方，或者小于等于 -2 的 63 次方，将导致计算溢出。

     操作系统需求： Windows、Linux
    """
    return math.tan(欲进行计算的角)


def 求反正切(欲求其反正切值的数值: float):
    """
     调用格式： 〈双精度小数型〉 求反正切 （双精度小数型 欲求其反正切值的数值） - 系统核心支持库->算术运算

     英文名称：atn

     返回指定数的反正切值。本命令为初级命令。

     参数<1>的名称为“欲求其反正切值的数值”，类型为“双精度小数型（double）”。

     操作系统需求： Windows、Linux
    """
    return math.atan(欲求其反正切值的数值)


def 置随机数种子(欲置入的种子数值):
    """
     调用格式： 〈无返回值〉 置随机数种子 （［整数型 欲置入的种子数值］） - 系统核心支持库->算术运算

     英文名称：randomize

     为随机数生成器初始化一个种子值，不同的种子值将导致“取随机数”命令返回不同的随机数系列。本命令为初级命令。

     参数<1>的名称为“欲置入的种子数值”，类型为“整数型（int）”，可以被省略。如果省略本参数，将默认使用当前计算机系统的时钟值。

     操作系统需求： Windows、Linux
    """
    random.seed()


def 取随机数(欲取随机数的最小值: int, 欲取随机数的最大值: int):
    """
     调用格式： 〈整数型〉 取随机数 （［整数型 欲取随机数的最小值］，［整数型 欲取随机数的最大值］） - 系统核心支持库->算术运算

     英文名称：rnd

     返回一个指定范围内的随机数值。在使用本命令取一系列的随机数之前，应该先使用“置随机数种子”命令为随机数生成器初始化一个种子值。本命令为初级命令。

     参数<1>的名称为“欲取随机数的最小值”，类型为“整数型（int）”，可以被省略。参数必须大于或等于零。本参数如果被省略，默认为 0 。

     参数<2>的名称为“欲取随机数的最大值”，类型为“整数型（int）”，可以被省略。参数必须大于或等于零。本参数如果被省略，默认为无限。

     操作系统需求： Windows、Linux
    """
    return random.randint(欲取随机数的最小值, 欲取随机数的最大值)


def 保留位数(数值, 位数=2):
    """
    保留小数点后指定位数

    :param 数值: 1.12345
    :param 位数: 2
    :return: 1.12
    """
    return format(数值, '.{}f'.format(位数))


def 取最小数(数值列表):
    """
    传入要对比的列表,如(1,2,3),返回里面最小的数字

    :param 数值列表: (1,2,3)
    :return: 1
    """
    return min(数值列表)


def 取最大数(数值列表):
    """
    传入要对比的列表,如(1,2,3),返回里面最大的数字

    :param 数值列表: (1,2,3)
    :return: 3
    """

    return max(数值列表)


def 向下取整(数值):
    """
    示例:1.9返回1

    :param 数值: 1.9
    :return: 1
    """
    return math.floor(数值)


def 向上取整(数值):
    """
    示例:1.1返回2

    :param 数值:  1.1
    :return: 2
    """
    return math.ceil(数值)


def 取整数(val):
    """
    示例:'8852791.5'返回8852791

    :param 字符串:  8852791.5
    :return: 8852791
    """
    return int(float(val))