# xpath解析
# （1）本地文件        etree.parse
# （2）服务器响应的数据  etree.HTML()

# xpath解析本地文件
from lxml import etree
tree = etree.parse('015_供xpath学习用.html')

#tree.xpath('xpath路径')

# 查找ul下面的li
# li_list = tree.xpath("//ul/li")

# 查找所有有id的属性的li标签
# text()获取标签中的内容
# li_list = tree.xpath("//li[@id]/text()")
# print(len(li_list))

# 找到id为g1的li标签  注意引号的问题
# li_list = tree.xpath("//li[@id='g1']")
# print(len(li_list))

# 查找到id为g1的li标签的class的属性值
# li_list = tree.xpath("//li[@id='g1']/@class")
# print(li_list)
