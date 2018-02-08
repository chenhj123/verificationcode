from urllib import request
host_url = 'http://jwmis.hhtc.edu.cn/'
captcha_url = host_url+'sys/ValidateCode.aspx'
for k in range(300):
    request.urlretrieve(captcha_url,'captcha_example/%d.jpg'%k)