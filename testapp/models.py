from django.db import models

# Create your models here.
class TestApp(models.Model):
    name = models.CharField(max_length=64, null=True, verbose_name=u"名称")
    upfile = models.FileField(upload_to=u"upfiles", null=True, verbose_name=u"文件")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"上传文件"
        verbose_name_plural = verbose_name

class TestTable(models.Model):
    name = models.CharField(max_length=64, null=True, verbose_name=u"名称")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"测试表格"
        verbose_name_plural = verbose_name

class TestKey(models.Model):
    test = models.ForeignKey(TestTable, on_delete=models.CASCADE, null=True, verbose_name=u"关联表格")
    name = models.CharField(max_length=64, null=True, verbose_name=u"名称")
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"外键测试"
        verbose_name_plural = verbose_name
