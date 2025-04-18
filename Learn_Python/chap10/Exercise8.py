# import prettytable as pt

# def show_ticket(row_num):
#     tb = pt.PrettyTable()
#     tb.field_names = ['行号', '座位1', '座位2', '座位3', '座位4', '座位5']
#     for i in range(1, row_num + 1):
#         lst = [f'第{i}行', '有票', '有票', '有票', '有票', '有票']
#         tb.add_row(lst)
#     print(tb)

# def order_ticket(row_num, row, column):
#     tb = pt.PrettyTable()
#     tb.field_names = ['行号', '座位1', '座位2', '座位3', '座位4', '座位5']
#     for i in range(1, row_num + 1):
#         if int(row) == i:
#             lst = [f'第{i}行', '有票', '有票', '有票', '有票', '有票']
#             lst[int(column)] = '已订'
#         else:
#             lst = [f'第{i}行', '有票', '有票', '有票', '有票', '有票']
#         tb.add_row(lst)
#     print(tb)


# if __name__ == '__main__':
#     row_num = 6
#     show_ticket(row_num)

#     choose_num = input('请输入你要订票的行号和座位号（行号,座位号）：')
#     row, column = choose_num.split(',')
#     order_ticket(row_num, row, column)


# import datetime

# def input_date():
#     inputdate = input('请输入开始日期：（20281001）后按回车：')
#     datestr = inputdate[0:4] + '-' + inputdate[4:6] + '-' + inputdate[6:8]
#     date = datetime.datetime.strptime(datestr, '%Y-%m-%d')
#     return date

# if __name__ == '__main__':
#     date = input_date()
#     in_num = eval(input('请输入间隔天数：'))
#     date = date + datetime.timedelta(days=in_num)
#     print('您推算的日期是：', date)

import jieba
from wordcloud import WordCloud

with open('华为笔记本.txt', 'r', encoding='utf-8') as file:
    s = file.read()

lst = jieba.lcut(s)

stopword = ['好久', '允许', '一族', '人来', '宣誓', '开课', '清廷', '到达', '明亮', '生计', '不错', '为什么', '国旗',
            '其中', '责任', '密集', '时考', '学说', '播种', '麻烦', '中断', '人群', '小孩', '大半部', '教育局', '公公',
            '另外', '报关行', '玩耍', '文学', '加入', '人当', '说话', '再后', '介绍', '九月', '太平洋战争', '人会', '账房',
            '负责', '人为', '二弟', '年春夏', '虽然', '亡灵', '转入', ' 中学', '还教', '清明', '亲自', '凶点', '实际', '忘记',
            '来说', '汽车', '多份', '一笔', '通知', '一点', '随着', '商船', '放学', '落脚', '私仇', '18', '犯下', '子孙', '烧纸', 
            '唐诗宋词', '贫苦', '胶州路', '早逝', '决定', '每个', '战士', '大人', '托人', '地不分', '先祖', '各家', '入学', '凌辱', 
            '停航', '做过', '每年', '到底', '国军', '英国人', '子女', '香火', '学校', '怎么', '要是', '第二年', '戚镇东', '才能', '以峰',
            '完会', '倭寇', '甲午海战', '常有', '不料', '还是', '孩提时代', '几年', '提供者', '成绩', '奴隶', '影响', '山顶', '这个', '十八年', 
            '罪行', '妹妹', '乡亲', '妇女', '蔬菜', '被迫', '对面', '一吐', '启蒙教育', '听说', '就常去', '米行', '一个劲地', '第一章', '几话', 
            '不论', '不但', '礼让', '我受', '惦记', '遭受', '担心', '能看懂', '国民党', '看不懂', '膝盖', '那次', '过门', '芜湖市', '好友', '管起', 
            '珍贵', '军队', '南北', '身上', '老大', '最有', '从商', '两个', '召集', '印象', '教起', '然后', '常到', '诗经', '贩卖', '1930', '金银珠宝', 
            '永远', '跪拜', '日伪', '读过', '事情', '按照', '不祥', '儿女', '不凶', '回家', '活动', '船上', '校工', '小名', '翻跟头', '极大', '学业', '多少', 
            '养病', '受到限制', '家人', '心海', '科举制度', '妻子', '游击队', '刘公岛', '17', '控诉', '缭绕', '一年级', '奖励', '进城', '宗谱', '慢慢', '没落', 
            '戚本玉', '就要', '人家', '传统美德', '三个', '否则', '思想', '路断', '奉养', '大名', '哀求', '赶下去', '当年', '告别', '晕车', '半路', '似懂非懂', 
            '准备', '稍大', '地下党', '书籍', '老人', '幼小', '一家', '过年', '通过', '说明', '人生', '事变', '藏书', '兴趣', '确实', '拿到', '嫡长子', '为报', 
            '直到', '只有', '1905', '摆在', '弃文', '震动', '打工', '年代', '军人', '1936', '现在', '找到', '爆发', '存在', '职业', '预感', '向着', '担负', '本字辈', 
            '1931', '自然科学', '观察', '因家道', '战死', '自觉', '年秋入', '海滩', '兄弟', '先是', '孩子', '谷源', '最大', '老姑', '经常', '职员', '塑像', '有些', '祸害',
            '传染', '解释', '表兄', '12', '不知疲倦', '宗族', '嫁给', '双方', '只要', '光线', '晚清', '思想家', '天下大事', '西城', '学前', '每到', '而是', '领着', '卢梭', 
            '再起', '三弟', '关心', '家法', '解放以后', '道路', '小楼', '学问', '1929', '操持家务', '整个', '温顺', '购进', '中央', '历史', '神像', '要学', '随时', '押运', 
            '坏人', '心灵', '全校', '却是', '汇来', '发现', '沿途', '图书馆', '真正', '预示', '来不及', '乘客', '从小', '观看', '高兴', '学名', '周易', '宣战', '讲得', 
            '撒酒', '就让', '1942', '继后', '海员', '还有', '任地', '呕吐', '地图', '只能', '呼唤', '名言', '三字经', '看书', '人不分' '为了', '以后', '重新', '车上', 
            '照顾', '姨父', '这条', '挣钱', '吃不起', '祭拜', '四十多年', '撞船', '对于', '诱惑力', '日本鬼子', '亲友', '丛秀梅', '不敢', '戚英科', '功成名就', '四书五经', 
            '几百年', '害怕', '处置', '成千', '讲故事', '老幼', '下车', '老百姓', '拼命', '大革命', '帮着', '汇款', '第一名', '识字', '岳飞', '故事', '不然', '团聚', '经书', 
            '可是', '秀才', '忘不了', '一大群', '出生', '颁发', '牢狱', '黄海', '背对', '东西', '不久', '造大孽', '回来', '丢脸', '知道', '喜欢', '边玩', '小时候', '人去', 
            '教书', '五年级', '进金', '经营', '联考', '年轻人', '小伙伴', '那些', '海疆', '有用', '赶紧', '爱国主义', '光宗耀祖', '一来', '少年', '抗击', '点香', '会议', 
            '乡下', '图书', '抓住', '教导', '它们', '养家糊口', '管事', '侵略', '逃离', '讲解', '独子', '那辈人', '听到', '生员', '功夫', '生硬', '附近', '大约', '钱后', '投降', '这样', '教育', '文化']
txt = ' '.join(lst)
wordcloud = WordCloud(background_color='white', font_path='msyh.ttc', stopwords=stopword,
                      width=800, height=600).generate(txt)
wordcloud.to_file('华为笔记本.png')