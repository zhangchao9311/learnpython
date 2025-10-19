def make_album(singer_name, album_name, songs_number=None):
    """返回一个字典，其中包含一个音乐专辑的信息"""
    music_album={'singer': singer_name, 'album': album_name}
    return music_album

while True:
    print("\nPlease tell me your favorite album.")
    print("(enter 'q' at any time to quit)")

    a_name = input("Album name:")
    if a_name == 'q':
        break

    s_name = input("Singer name:")
    if s_name == 'q':
        break

    get_music_album = make_album(a_name, s_name)
    print(get_music_album)