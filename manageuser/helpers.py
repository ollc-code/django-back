from django.contrib.auth import get_user_model


def change_password(username, current_password, new_password):
    try:
        user = get_user_model().objects.get(username=username)
    except:
        return "User could not be found"
    print(user.check_password(current_password))
    if user.check_password(current_password):
        user.set_password(new_password)
        user.save()
        return True
    else:
        print("not")
        return False