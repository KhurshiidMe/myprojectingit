# from datetime import date
#
#
# def get_weekday():
#     return date.today().strftime('%A')
#
#
# def create_new_post(post, weekday=get_weekday()):
#     post_copy = post.copy()
#     post_copy['created_on_weekday'] = weekday
#     return post_copy
#
#
# initial_post = {
#     'id': 243,
#     'author': 'Khurshid',
# }
# post_with_weekday = create_new_post(initial_post, )
# print(post_with_weekday)
# print(initial_post)

# def print_number_info(num):
#     if (num % 2) == 0:
#         print("Entered number is even")
#     else:
#         print("Entered number is odd")
#
# def print_squear_num(num):
#     print("square of the num is", num * num)
# def process_number(num, callback_fn):
#     callback_fn(num)
#
#
# entered_num = int(input('Enter any number: '))
# process_number(entered_num, print_squear_num)
#
# def send_data(data):
#     pass
#
# def process_data(input_data, send_data_fn):
#     updated_data = input_data.copy()
#     send_data_fn(updated_data)
#
# process_data({'name': 'Khurshid'}, send_data)

# def greeting(greet):
#     return lambda name: f"{greet} {name}!"
#
# morning = greeting("Good Mording")
# print(morning('bogdan'))

# try:
#     print(10 / 2)
# except ZeroDivisionError:
#     print("xato bu xatooooo")
#
# print('Continue...')
# try:
#     print(10 / 5)
# except ZeroDivisionError as e:
#     print(e)
# except TypeError as e:
#     print(e)
# else:
#     print("There was no error")
# finally:
#     print('Continue...')
#
# def divide_nums(a, b):
#     if b == 0:
#         raise Error("Second argument can't be 0")
#     return a / b
#
# try:
#     divide_nums(10, 0)
# except ZeroDivisionError as e:
#     print(e)
# except TypeError as e:
#     print(e)
# user_profile = ['Khurshid', 23]
# def user_info(name, comments_qty = 0):
#     if not comments_qty:
#         return f"{name} has no comments"
#     return f"{name} has {comments_qty} comments"
# print(user_info(*user_profile),)
#
# my_phone = {
#     'brand': 200
# }
# if my_phone.get('brand'):
#     print("Phone's brand is", my_phone['brand'])
# else:
#     print("There is no phone brand")

# def route_info(dictme):
#     if  dictme.get('distance'):
#         return "Distance to your destination is <distance>"
#     if  dictme.get('speed' and 'time'):
#         return "Distance to your destination is <speed * time>"
#     return "No distance info is available"
#
#
# my_dict = {
#     'speed': '500km',
#     'time': 'mol',
# }
# print(route_info(my_dict))

# my_img = ('1920', '1080')
#
#
# print(f"{my_img[0]}x{my_img[1]}") if len(my_img) == 2 else print("Incorrect image")

