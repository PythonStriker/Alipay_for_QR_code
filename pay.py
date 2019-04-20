from self_Alipay import *
import qrcode,time

APPID = 2016092600601253
private_key = '''-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEA0ZmM9+lQRa0VkHsUTywF0msOVUrXIupBIp0f3T6TPT/tGrHfut3VtiO/c3Ota8YnaqxFfXui4rF5DtidOs32bJdvq4L0aOnOSeE9g/JDwG7X+GeQ3e0pzfNxLhEFlULt8ks+N4A+mVH+E1Fdy07FnyEF/JmuPjIq/2SfbgwghOgda5dP3rKE5VeOlgUL2pJWA2ZbzMZHQ+iAsQKfx2NzIRiygo89GFE8knOKweWqHYFMiZ2y2J9QYMyBJrBIGh+PRiswMfBS6xpfupAf2u+8BTGMxhj+I6zs5JBP1upngD0YhpPifU+SSK3SjKF19dJImJWqhaZD0vQdXzNJRkCMcQIDAQABAoIBAQC5+YrRNd2Z1Tf7GJounZsU1xTCrUMyobPlqJDrWGiAwkX5l7YyMj87+4AWSp+nrwyuY+jMrHUcu+f0OlNYKAPs2nmlLu76X+pAN3DDsKRZDIDo0cwCfjrHmKfl/gh8JgTHJegwisQAenX8YgfdKynCRiTvutSWLyFjtr6XgH8iLM8tYxkG8MYDuhpsPJ3ToZi17WZtGMduolOWMwBtYx3IfzukOTJnEsIMPLFl/zqw5/1700vm4MvMIalQ2eiU13WGfRywMyd/u4ISQJ6V4HNgbr7RRFBitt/bCMF+3rBd4mDSv9+iamzyYP0sjaSk3PZVxViIEHTfYJ8htVl8UShZAoGBAO1QH3tzq3KHOQ84i9FDSzyZG1tKcyvzAcb5bTXJTmHHsMW7zTtuWTe8Ki1eeoh9USHY+v5jFG+Kyt4ej2Yez9UT8wlYvHOspkKx1TZb/3cYQ8txQkQKgb00XwRVzyqEia3jkgGTY8AVPdw9UZTIJ37Sj45gq0Wk8lcrzFFU2ornAoGBAOIaxXOA2MoYdHVRPTTHVkJ5YkoG7/0S9eCok+EVsKTJnm0VInXi5Uk+/72T8qbr1gw54/DlBqdEGGrWUHCmz7ro2tVInpQ0lnY8muTjhSu2o0CNV9VfAMDcyUgE7mhPJkx1Kplh1WypBqQTKalTxG5rm87eAB85lCSqi/8PCFrnAoGBAMVXFXbxTybj770KhqozzYLMxwT5OiDX6ShvDjPl/Lou9n7XlujO8H36iRBFOpv5qdf9uWqFNd8ziVOAEjsXcDh+aGHjWoLOlUts2iJkCmIc2XN58WLnYc/WlxThzm5K3LqvPSD2UcLPZyuYChkxADbkHeCF3qcBbUyz7SnM6BcNAoGAHpkq4W+tZuQaVooQ82SKiuJsZ8I6lhAL0ERgBtTtm89hLjfu+u8iwl/RMjGkY+yEghEPhNkpplczyrmIF0ar1AqRGs4CD+Jx/jxDZfhYXEsSGrlGCq0Zp//5CVMJhHo5n503j5xKyrKxIGErgSvB6IONiVhHwfID11ZxLao2Ij8CgYBUp6BHP2pS5gS/B421dWjrddVGUDzd5hws4FU3QzQOi1Wp4W2yTX7dhPC6MvpG4TikWN58eO2Jw1lIAF10ZBXwp6r6C0XKEwdrT9+xYen2fQLB9tZef/5eEe3tvxASP5eDBSL6c5+nIK/X6F+6KDtSwQXl0pI4ZvYvBaJcvYYmcw==
-----END RSA PRIVATE KEY-----
'''
public_key = '''-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAuNcQoWf8TzYF1fhtmcTSytdRNhV8P+GkSUrn9aq7SKdW7MrI3i6qKXweNBtakgQlMBDcOjYU9qq4QpzouIO92IpNr51+S92pUuFlVA+Dmmp1Gw2hf6EQihYkIvS6sNJ6u/dJj0+GLr3/JKXgw0AanvxFMyaca5GxsAk41g+h3nYPKVWrXpisEKwvnSFQxZ8+BHJYu9BRC3XLO+y82HP9Ay10hsU3m7WrMfSoY5p1TuUDWFPax7oMfvLcZDewSiTorkKOJX7Xej0S5Jfy5uImY5wf3VePxNgP1V32+BpEsHRO8bZjuFtCpx/pR6HSXOBvAUIIRIqQ31SKfhO8Z5dufwIDAQAB
-----END PUBLIC KEY-----
'''

class pay:
    def __init__(self,out_trade_no,total_amount,subject,timeout_express):
        self.out_trade_no = out_trade_no
        self.total_amount = total_amount
        self.subject = subject
        self.timeout_express = timeout_express

    def get_qr_code(self,code_url):
        '''
        生成二维码
        :return None
        '''
        qr = qrcode.QRCode(
             version=1,
             error_correction=qrcode.constants.ERROR_CORRECT_H,
             box_size=10,
             border=1
        )
        qr.add_data(code_url)  # 二维码所含信息
        img = qr.make_image()  # 生成二维码图片
        img.save(r'A:\Study\Document\WorkSpace\Python\二维码\qrcode_image\qr_test_ali.png')
        print('二维码保存成功！')

    def query_order(self,out_trade_no: int):
        '''
        :param out_trade_no: 商户订单号
        :return: Nonem
        '''
        _time = 0
        for i in range(600):
            time.sleep(1)
            result = alipay.init_alipay_cfg().api_alipay_trade_query(out_trade_no=out_trade_no)
            if result.get("trade_status", "") == "TRADE_SUCCESS":
                print('订单已支付!')
                print('订单查询返回值：', result)
                return True
            _time += 2
        return False


if __name__ == '__main__':
    alipay = alipay(APPID, private_key, public_key)
    payer = pay(out_trade_no="555",total_amount= 6,subject = "relive",timeout_express='5m')
    dict = alipay.trade_pre_create(out_trade_no=payer.out_trade_no,total_amount=payer.total_amount,subject =payer.subject,timeout_express=payer.timeout_express )

    payer.get_qr_code(dict['qr_code'])
    payer.query_order(payer.out_trade_no)