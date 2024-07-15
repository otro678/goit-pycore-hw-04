from pathlib import Path

def get_cats_info(path):
    cats_info = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    cat_id, name, age = line.strip().split(',')
                    cat_dict = {"id": cat_id, "name": name, "age": age}
                    cats_info.append(cat_dict)
                except Exception as e:
                    print(f"Error while parsing line {line}")
    
    except FileNotFoundError:
        print(f"File was not found at {path}.")
    except Exception as e:
        print(f"An unknown error occurred: {e}")
    
    return cats_info

script_dir = Path(__file__).parent.resolve()
path_to_file = script_dir / 'cats.txt'

cats_info = get_cats_info(path_to_file)
print(cats_info)