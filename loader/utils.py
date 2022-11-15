def save_picture(picture) -> str:
    """
    Сохранение картинки (фото) по пути
    """
    filename = picture.filename
    path = f'./uploads/images/{filename}'
    picture.save(path)
    return path
