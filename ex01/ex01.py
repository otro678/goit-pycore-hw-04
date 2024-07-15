from pathlib import Path

def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            salaries = []
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 2:
                    try:
                        salary = float(parts[1])
                        print(f"Parsed salary is {salary}")
                        salaries.append(salary)
                    except ValueError:
                        print(f"Wrong entry at {line}")
                        continue

            if not salaries:
                return 0, 0

            total = sum(salaries)
            average = total / len(salaries)
            return total, average

    except FileNotFoundError:
        print(f"File wasn't found at {path}")
        return 0, 0
    except Exception as e:
        print(f"Unhandled error while reading data from file: {e}")
        return 0, 0
    
script_dir = Path(__file__).parent.resolve()
path_to_file = script_dir / 'salaries.txt'
total, average = total_salary(path_to_file)
print(f"Total salary: {total}, Average salary: {average}")