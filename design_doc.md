## 分页功能介绍

### 第一页 数据概览

> 本页对应基本实验要求第一条、所需任务第一条

导入数据集按钮

> 本功能对应所需任务第一条

各项指标的统计图显示，并支持保存（有一个导出按钮）

> 本功能对应基本实验要求第二条

其中指标与图表类型对应表如下

| 指标                                       | 图表类型 |
| ------------------------------------------ | -------- |
| 性别                                       | 饼状图   |
| 国籍                                       | 饼状图   |
| 出生地                                     | 饼状图   |
| 学校级别                                   | 条形图   |
| 年级                                       | 条形图   |
| 班级                                       | 条形图   |
| 学科科目                                   | 条形图   |
| 学期                                       | 条形图   |
| 关系                                       | 饼状图   |
| 举手次数                                   | 条形图   |
| 浏览在线课件次数                           | 条形图   |
| 浏览学校公告次数                           | 条形图   |
| 讨论次数                                   | 条形图   |
| 家长是否填写调查                           | 饼状图   |
| 家长是否满意                               | 饼状图   |
| 缺勤天数                                   | 饼状图   |
| 等级？（私以为这是输出，不应属于原始数据） |          |

> 表格类型对应所需任务第二条

### 第二页 班级与学年成绩展示

类似于第一页，不过用户可以通过下拉框选择年级、班级、学期和上表某个因素，来显示特定的一张表

> 本页对应所需任务第三条、可选任务第二条

### 第三页 训练过程（暂无）

> 本页对应基本实验要求第三条

一张折线图表位于中央，显示loss的变化。训练结束提示。

### 第四页 训练结果呈现

通过雷达图或条形图，显示各个因素对结果的影响程度

> 该功能对应基本实验要求第三条

对于影响最好的三个因素，运用条形图+折线图来表明在因素变化的情况下，三个等级的人数变化（因素的归纳来源于训练，不过呈现人数，按所有数据的真实等级来呈现）

> 该功能对应基本实验要求第三条、可选任务第三条

### 第五页 训练模型评估

> 该页对应可选任务第四条

（对于测试集数据）

可以列表（展示测试集每个人的真实值和预测值，以及预测正确性）、或者简单以文字的形式表明模型的准确率

（可以分析四个指标：准确率、错误率、精确率、召回率）

## 问题

可选任务第一条的分级，是原始真实数据的一个统计呈现？还是预测分类的展示？