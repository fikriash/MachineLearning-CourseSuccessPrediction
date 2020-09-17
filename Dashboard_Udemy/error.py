# level_enc = '1'
# if level_enc == "0":
#     level_enc = 0
# elif level_enc == "1":
#     level_enc = 1
# elif level_enc == "2":
#     level_enc = 2
# else:
#     level_enc = 3
# price=5
# is_paid_False = 'no'
# if price == 0:
#     if is_paid_False == 'no':
#         is_paid_False = 1
#     elif is_paid_False == 'yes':
#         is_paid_False = 0
# else:
#     is_paid_False = 1
    
# is_paid_True = 'yes'
# if price != 0:
#     if is_paid_True == 'no':
#         is_paid_True = 0
#     elif is_paid_True == 'yes':
#         is_paid_True = 1
# else:
#     is_paid_True == 0

business_subject = 'business'
if business_subject == 'business':
    business_subject = 1
else:
    business_subject = 0

# graphic_subject = 'business'
# if graphic_subject == 'graphic':
#     graphic_subject == 1
# else:
#     graphic_subject == 0

# music_subject = 'business'
# if music_subject == 'music':
#     music_subject == 1
# else:
#     music_subject == 0

# webdev_subject = 'business'
# if webdev_subject == 'web':
#     webdev_subject == 1
# else:
#     webdev_subject == 0

# sample = pd.DataFrame(
#     columns=[course_id],
#     index=[
#         'price', 'num_lectures', 'content_duration', 'year_p', 'month_p',
#         'date_p', 'level_enc', 'is_paid_False', 'is_paid_True',
#         'business_subject', 'graphic_subject', 'music_subject',
#         'webdev_subject'
#     ],
#     data = [price,num_lectures,content_duration,year_p,month_p,date_p,level_enc,is_paid_False,is_paid_True,business_subject,graphic_subject,music_subject,webdev_subject]
# ).T

print(business_subject)
print(type(business_subject))