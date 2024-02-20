from django.db import models

# Create your models here.
"""
1. 模型类 需要继承自models.Model
2. 定义属性
    属性名 = models.类型（选项）
    id系统默认会生成
    2.1 属性名就是字段名
        不要使用python关键字或者mysql关键字
        不要使用连续的下划线
    2.2 类型  mysql的类型
    2.3 选项 是否有默认值，是否唯一，是否为null
        CharField必须设置max_length
        verbose_name 影响在admin站点中的显示
3. 改变表的名称
    默认名称是：子应用名_类名 都是小写
    修改表的名字
"""


class BookInfo(models.Model):
    name = models.CharField(max_length=10, unique=True, verbose_name='名字')
    pub_date = models.DateField(null=True)
    read_count = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'bookinfo'  # 修改表的名字
        verbose_name = '书籍管理'  # admin站点使用的


class PeopleInfo(models.Model):

    # 定义一个有序字典
    GENDER_CHOICES = (
        (1, 'male'),
        (2, 'female')
    )

    name = models.CharField(max_length=10, unique=True)
    gender = models.SmallIntegerField(choices=GENDER_CHOICES, default=1)
    description = models.CharField(max_length=100, null=True)
    is_delete = models.BooleanField(default=False)

    # 外键
    # 系统会自动为外键添加_id

    # 外键的级联操作
    # 主表和从表
    # 主表的一条数据删除了，从表关联的数据怎么办呢？

    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)

    class Meta:
        db_table = 'peopleinfo'
