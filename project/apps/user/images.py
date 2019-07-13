def user_profile_image_path(instance, filename):
    return '{id}/{file}'.format(
        id=instance.id,
        file=filename
    )