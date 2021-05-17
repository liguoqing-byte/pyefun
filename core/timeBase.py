import time
import pendulum
import copy


pendulum.set_locale('zh')


# 文档
# https://pendulum.eustace.io/docs/#instantiation
class 日期时间:
    t = pendulum.DateTime

    def __init__(self, str="now"):
        pass

        if (type(str) == int):
            self.t = pendulum.from_timestamp(str, tz='Asia/Shanghai')
        elif (str != ""):
            self.t = pendulum.parse(str)

    def 到文本(self, format="YYYY-MM-DD HH:mm:ss"):
        return self.t.format(format)

    def 取时间戳(self):
        return self.t.int_timestamp

    def 取日期(self):
        return self.t.to_date_string()

    def 取年(self):
        return self.t.year

    def 取月(self):
        return self.t.month

    def 取日(self):
        return self.t.day

    def 取小时(self):
        return self.t.hour

    def 取分钟(self):
        return self.t.minute

    def 取秒(self):
        return self.t.second

    def 取微妙(self):
        return self.t.microsecond

    def 取每周的第几天(self):
        return self.t.day_of_week

    def 取每年的第几天(self):
        return self.t.day_of_year

    def 取每月的第几周(self):
        return self.t.week_of_month

    def 取每年的第几周(self):
        return self.t.week_of_year

    def 取月天数(self):
        return self.t.days_in_month

    def 设置年月日(self, year=None, month=None, day=None):
        self.t = self.t.on(year=int(year), month=int(month), day=int(day))
        return self

    def 设置时分秒(self, hour=0, minute=0, second=0):
        self.t = self.t.at(hour, minute, second)
        return self

    def 增减日期时间(self, years=0, months=0, weeks=0, days=0, hours=0, minutes=0, seconds=0):
        self.t = self.t.add(years=years,
                            months=months,
                            weeks=weeks,
                            days=days,
                            hours=hours,
                            minutes=minutes,
                            seconds=seconds,
                            )
        return self

    def 取时间间隔(self, datetime):

        d = self.t.diff(datetime, abs=False)
        return {
            "years": d.in_years(),
            "months": d.in_months(),
            "days": d.in_days(),
            "hours": d.in_hours(),
            "minutes": d.in_minutes(),
            "seconds": d.in_seconds(),
            "weeks": d.in_weeks(),
        }
    def 取友好时间(self):
        d = self.t.diff_for_humans()
        return d

    def datetime(self):
        return self.t
    def copy(self):
        return copy.deepcopy(self)
    def __str__(self):
        return self.到文本()


def 取现行时间戳():
    return round(time.time())


def 日期到时间戳(str="now"):
    return 日期时间(str).取时间戳()


def 取现行时间():
    t = 日期时间()
    return t

def 创建日期时间(str):
    t = 日期时间(str)
    return t

def 时间迭代(start,end):
    """
    为支持单位range()有：years，months，weeks， days，hours，minutes和seconds
    for i in list.range('months'):
        print(i.to_datetime_string())
    """
    return pendulum.period(pendulum.parse(start), pendulum.parse(end))