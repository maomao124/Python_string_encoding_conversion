"""
 * Project name(项目名称)：Python字符串编码转换
 * Package(包名): 
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/23 
 * Time(创建时间)： 21:22
 * Version(版本): 1.0
 * Description(描述)： Python encode()方法
encode() 方法为字符串类型（str）提供的方法，用于将 str 类型转换成 bytes 类型，这个过程也称为“编码”。
encode() 方法的语法格式如下：
str.encode([encoding="utf-8"][,errors="strict"])
注意，格式中用 [] 括起来的参数为可选参数，也就是说，在使用此方法时，可以使用 [] 中的参数，也可以不使用。
参数	含义
str	表示要进行转换的字符串。
encoding = "utf-8"	指定进行编码时采用的字符编码，该选项默认采用 utf-8 编码。例如，如果想使用简体中文，可以设置 gb2312。
当方法中只使用这一个参数时，可以省略前边的“encoding=”，直接写编码格式，例如 str.encode("UTF-8")。
errors = "strict"	指定错误处理方式，其可选择值可以是：
strict：遇到非法字符就抛出异常。
ignore：忽略非法字符。
replace：用“？”替换非法字符。
xmlcharrefreplace：使用 xml 的字符引用。
该参数的默认值为 strict。
 """

if __name__ == '__main__':
    str1 = "hello"
    b1 = str1.encode()
    print(b1)
    print(type(b1))
    b1 = str1.encode("utf-8")
    print(b1)
    print(type(b1))
    b1 = str1.encode("utf-16le")
    print(b1)
    print(type(b1))

    input()
