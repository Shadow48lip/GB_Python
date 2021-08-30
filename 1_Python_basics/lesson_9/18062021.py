# def print_human_name(human):
#     print(human['name'])
#
#
# h1 = {'name': 'ABC'}
# h2 = {'name': 'ASD'}
# h3 = {'full_name': 'ZXC'}
#
# print_human_name(h3)

# class Human:
#     def __init__(self, name):
#         self.name = name
#
#     def print_human_name(self):
#         print(self.name)
#
# h1 = Human('asd')
# h1.print_human_name()

class Phone:
    def __init__(self, phone_model):
        self.model = phone_model
        self._serial_number = 5654654
        self._loading()

    def call(self, number):
        self.last_call = number
        print(f'phone {self.model} is calling {number}')

    def _loading(self):
        print('loading')

    def get_serial_number(self):
        return self._serial_number


# phone1 = Phone('nokia1100')
# print(phone1.get_serial_number())
# phone1._Phone__loading()  # obj._ClassName__foo
# print(phone1.model)
# phone1.call(900)
# phone1.call(6541654)
# print(phone1.last_call)
# phone2 = Phone('nokia2110')
# print(phone2.model)
# phone2.call()


class SmartPhone(Phone):

    def sms(self):
        print('smsing')

    def email(self):
        print('emailing')


# smphone = SmartPhone('nokia6600')
# smphone.call(654654)
# smphone.sms()

class IPhone(SmartPhone):
    def __init__(self, phone_model):
        super().__init__(phone_model)
        print('show apple')

    def player(self):
        print('player')

    def browser(self):
        print('browser')

    def sms(self):
        print('Imessage sending')


iphone = IPhone('6')
# iphone.sms()

class NextGen(IPhone):
    pass


class Player:
    def method(self):
        print('player_method от Player')


class Navigator:
    def method(self):
        print('navigator_method от Navigator')


class MobilePhone(Player, Navigator):
    def mphone_method(self):
        print('mphone_method')


# mp = MobilePhone()
# mp.mphone_method()
# mp.method()


class Auto:
    def auto_start(self, x1, x2=None):
        if x2 is None:
            print(x1)
        else:
            print(x1 + x2)


# a = Auto()
# a.auto_start(10)
# a.auto_start(10, 20)