# pdfplumber模块可用于从PDF文件中读取内容
# Numpy模块是Python数据分析方向和其他库的依赖库，用于处理数组、矩阵等数据
# Pandas模块是基于Numpy模块扩展的一个非常重要的数据分析模块，使用Pandas读取Excel数据更加方便
# Matplotlib模块是用于数据可视化的模块，使用Matplotlib.pyplot可以非常方便地绘制饼图、柱形图、折线图等。
# Seaborn模块是基于Matplotlib模块的一个数据可视化模块，使用Seaborn可以非常方便地绘制统计图表

import pdfplumber

with pdfplumber.open('paper.pdf') as pdf:
    for i in pdf.pages:                     # 遍历pdf文件中的每一页
        print(i.extract_text())             # extract_text()提取文本内容
        print(f'----------------------第{i.page_number}页结束----------------------')

