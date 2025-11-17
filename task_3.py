import sys
from pathlib import Path
from colorama import init, Fore

init(autoreset=True)

def visualize_directory(path_str):
    target_path = Path(path_str)

    if not target_path.exists():
        print(f"{Fore.RED}Помилка: Шлях '{path_str}' не знайдено.")
        return
    if not target_path.is_dir():
        print(f"{Fore.RED}Помилка: Шлях '{path_str}' не є директорією.")
        return

    print(f"{Fore.CYAN}📦 {target_path.name}")
    
    _walk_dir(target_path, prefix="", is_last=True)

def _walk_dir(path: Path, prefix: str, is_last: bool):
    connector = "┗ " if is_last else "┣ "
    color = Fore.BLUE if path.is_dir() else Fore.GREEN
    icon = "📂" if path.is_dir() else "📜"

    print(f"{color}{prefix}{connector}{icon}{path.name}")

    if path.is_dir():
        children = sorted(list(path.iterdir()), key=lambda p: (not p.is_dir(), p.name))
        new_prefix = prefix + ("    " if is_last else "┃   ")
        
        for i, child in enumerate(children):
            is_last_child = (i == len(children) - 1)
            _walk_dir(child, new_prefix, is_last_child)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"{Fore.YELLOW}Використання: python {Path(__file__).name} <шлях_до_директорії>")
    else:
        directory_path = sys.argv[1]
        visualize_directory(directory_path)
