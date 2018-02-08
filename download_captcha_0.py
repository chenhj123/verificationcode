from urllib import request
host_url='http://kmustjwcxk3.kmust.edu.cn/jwweb/'
captcha_url=host_url+'sys/ValidateCode.aspx'
for k in range(10):
    request.urlretrieve(captcha_url,'captcha_example/%d.jpg'%k)
    # 观察结论: 字符为数字 + 大写英文字母.后面发现没有数字0, 1, 字母I, L, O.应该是考虑到人也不易区分这几个字符.字符有两种字体, 且都是斜体字.
    # 有五条随机的直线, 上方有噪点, 有一外框.干扰很小.
    # 一般字体的变形有两类: 线性的, 非线性的.线性的又可分为: 平移, 倾斜, 旋转, 伸缩.很少有对称的.这里只有垂直方向的平移, 较易处理.
    # 总之, 这是一个很弱的验证码.