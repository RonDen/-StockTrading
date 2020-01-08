from random import randint, choice

from tradingSystem.models import UserTable
import os

banks = ['山东银行',
         '江苏银行',
         '上海银行',
         '浙江银行',
         '安徽银行',
         '福建银行',
         '江西银行',
         '广东银行',
         '广西银行',
         '海南银行',
         '河南银行',
         '湖南银行',
         '湖北银行',
         '北京银行',
         '天津银行',
         '河北银行',
         '山西银行',
         '内蒙古银行',
         '宁夏银行',
         '青海银行',
         '陕西银行',
         '重庆银行',
         '吉林银行']


class GenUser(object):
    city = [
        '山东', '江苏', '上海', '浙江', '安徽', '福建', '江西', '广东', '广西',
        '海南', '河南', '湖南', '湖北', '北京', '天津', '河北', '山西', '内蒙古', '宁夏',
        '青海', '陕西', '重庆', '吉林'
    ]

    def gen_code(self, l: int):
        code = ""
        for i in range(l):
            code += str(randint(0, 9))
        return code

    def gen_user_id(self):
        return self.gen_code(10)

    def gen_user_password(self):
        return self.gen_code(8)

    def gen_account_number(self):
        return self.gen_code(19)

    def gen_account_type(self):
        return choice(self.city) + '银行'

    def gen_id_no(self):
        return self.gen_code(18)

    def make_password(self):
        pass

    def gen_user_name(self):
        last_name = '赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜'
        first_name = '豫章故郡洪都新府星分翼轸地接衡庐襟三江而带五湖潦水尽而寒潭清落霞与孤鹜齐飞秋水共长天一色爽籁发而清风生纤歌凝而白云遏访风景于崇阿'
        return choice(last_name) + "".join(choice(first_name) for i in range(randint(1, 2)))

    def gen_email(self):
        mails = ['qq.com', '163.com', 'gmail.com', '126.com', 'mail.edu.cn']
        return self.gen_code(10) + '@' + choice(mails)

    def gen_sex(self):
        return choice(['男', '女'])

    def gen_phone(self):
        return '1' + self.gen_code(10)

    def gen_account_balance(self):
        return float(randint(10000, 500000))

def get_user_pic_path():
    pic1 = [img for img in os.listdir('static/img') if img.startswith('user') or img.startswith('ava')]
    return pic1

pics = get_user_pic_path()

def gen_photo_url():
    return '/static/img/' + choice(pics)


def main():
    genUser = GenUser()
    cnt = 0
    while cnt < 100:
        user = UserTable(
            user_id=genUser.gen_user_id(),
            id_no=genUser.gen_id_no(),
            user_name=genUser.gen_user_name(),
            password=genUser.gen_user_password(),
            user_sex=genUser.gen_sex(),
            phone_number=genUser.gen_phone(),
            user_email=genUser.gen_email(),
            photo_url=gen_photo_url(),
            account_num=genUser.gen_account_number(),
            account_type=genUser.gen_account_type(),
            account_balance=genUser.gen_account_balance(),
            freeze=False,
            account_opened=True
        )
        user.save()
        cnt += 1
        print(cnt)


if __name__ == '__main__':
    main()
