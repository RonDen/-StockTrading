from random import randint, choice

from tradingSystem.models import UserTable
import os


class GenUser(object):
    city = [
        '山东', '江苏', '上海', '浙江', '安徽', '福建', '江西', '广东', '广西',
        '海南', '河南', '湖南', '湖北', '北京', '天津', '河北', '山西', '内蒙古', '宁夏',
        '青海', '陕西', '重庆', '吉林'
    ]

    def gen_code(self, l: int):
        code = ""
        for i in range(l):
            code += str(randint(0,9))
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


def main():
    genUser = GenUser()
    cnt = 0
    while cnt < 100:
        try:
            user = UserTable(
                user_id=genUser.gen_user_id(),
                id_no=genUser.gen_id_no(),
                user_name=genUser.gen_user_name(),
                password=genUser.gen_user_password(),
                user_sex=genUser.gen_sex(),
                phone_number=genUser.gen_phone(),
                user_email=genUser.gen_email(),
                photo_url=r'C:\Users\LuoD\Documents\codes\StockTrading\static\img\head.jpg',
                account_num=genUser.gen_account_number(),
                account_type=genUser.gen_account_type(),
                account_balance=genUser.gen_account_balance(),
            )
            user.save()
            cnt += 1
            print(cnt)

        except Exception:
            print(Exception)


def get_user_pic_path():
    pic1 = [img for img in os.listdir('static/img') if img.startswith('user') or img.startswith('ava')]
    return pic1


pics = get_user_pic_path()

for u in UserTable.objects.all():
    if not u.phone_number == '15601205711':
        u.photo_url = '../static/img/' + choice(pics)
        u.save()


if __name__ == '__main__':
    main()

