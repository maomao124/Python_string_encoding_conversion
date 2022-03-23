"""
 * Project name(项目名称)：Python字符串编码转换
 * Package(包名): 
 * File(文件名): test2
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/23 
 * Time(创建时间)： 21:33
 * Version(版本): 1.0
 * Description(描述)： Python decode()方法
和 encode() 方法正好相反，decode() 方法用于将 bytes 类型的二进制数据转换为 str 类型，这个过程也称为“解码”。
参数	        含义
bytes	表示要进行转换的二进制数据。
encoding="utf-8"	指定解码时采用的字符编码，默认采用 utf-8 格式。当方法中只使用这一个参数时，可以省略“encoding=”，直接写编码方式即可。
注意，对 bytes 类型数据解码，要选择和当初编码时一样的格式。
errors = "strict"	指定错误处理方式，其可选择值可以是：
strict：遇到非法字符就抛出异常。
ignore：忽略非法字符。
replace：用“？”替换非法字符。
xmlcharrefreplace：使用 xml 的字符引用。
该参数的默认值为 strict。
 """

if __name__ == '__main__':
    str1 = "hello"
    b1 = str1.encode("utf-16le")
    print(b1)
    print(type(b1))
    str2 = b1.decode("utf-16le")
    print(str2)
    str2 = b1.decode("utf-16be")
    print(str2)
    str2 = b1.decode("gb2312")
    print(str2)
    str2 = b1.decode()
    print(str2)

    input()
