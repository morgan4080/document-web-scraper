from convert import convert_folder_to_html
directories = [
    'STU',
    'Capella University',
    'GCU',
    'ARTICLES',
]
if __name__ == '__main__':
    for directory in directories:
        added, found = convert_folder_to_html(directory)
        print(f"{directory} COMPLETE::::::")
        print(f"Total files added: {added}")
        print(f"Total files found: {found}")
