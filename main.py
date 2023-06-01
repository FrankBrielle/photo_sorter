import os
# import datetime #TODO check попробовать прикрутить дату в название исходной папки

main_path = 'c:\\photo_sort' #путь в который сортируются файлы


#os.mkdir(main_path + '\\sorted_photo') # создание папки для сортировки

#словарь для сортировки файлов
extensions = {
    'photo': ['jpg', 'jpeg'], #можно указать допустимые расширения файлов
}

# создание папки для сортировки
def create_folder_from_list(folder_path, folder_names):
    for folder in folder_names:
        if not os.path.exists(f'{folder_path}\\{folder}'):
                    os.mkdir(f'{folder_path}\\{folder}')

#пути подпапок и файлов
def get_subfolder_paths(folder_path) -> list:
    subfolder_paths = [f.path for f in os.scandir(folder_path) if f.is_dir()]
    return subfolder_paths

#пути всех файлов к папке
def get_file_paths(folder_path) -> list:
    file_paths = [f.path for f in os.scandir(folder_path) if not f.is_dir()]
    return file_paths

#получение имен файлов
#def get_file_names(folder_path) -> list:
    file_paths = [f.path for f in os.scandir(folder_path) if not f.is_dir()]
    file_names = [f.split('\\')[-1] for f in file_paths]
    return file_names

#функция сортировки файлов
def sort_files(folder_path):
    file_paths = get_file_paths(folder_path)
    ext_list = list(extensions.items())

    for file_path in file_paths:
        extension = file_path.split('.')[-1]
        file_name = file_path.split('\\')[-1]

        for dict_key_int in range(len(ext_list)):
            if extension in ext_list[dict_key_int][1]:
                print(f'Moving {file_name} in {ext_list[dict_key_int][0]} folder\n')
                os.rename(file_path, f'{main_path}\\{ext_list[dict_key_int][0]}\\{file_name}')

#def get_subfolder_names(folder_path) -> list:
#    subfolder_paths = get_subfolder_paths(folder_path)
#    subfolder_names = [f.split('\\')[-1] for f in subfolder_paths]
#    return subfolder_names

#удаление пустых папок
def remove_empty_folders(folder_path):
    subfolder_paths = get_subfolder_paths(folder_path)
    for delpath in subfolder_paths:
        if not os.listdir(delpath):
            print('Удаляю пустую папку:', delpath.split('\\')[-1], '\n')
            os.rmdir(delpath)

if __name__ == '__main__':
    create_folder_from_list(main_path, extensions)
    sort_files(main_path)
    remove_empty_folders(main_path)



