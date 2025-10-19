def make_album(singer_name, album_name, songs_number=None):
    """返回一个字典，其中包含一个音乐专辑的信息"""
    music_album={'singer': singer_name, 'album': album_name}
    if songs_number:
        music_album['songs_number'] = songs_number
    return music_album

album_1 = make_album('Thriller', 'Michael Jackson', songs_number=9)
print(album_1)

album_2 = make_album('1989', 'Taylor Swift')
print(album_2)

album_3 = make_album('good kid', 'Kendrick Lamar')
print(album_3)