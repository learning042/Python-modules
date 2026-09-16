import importlib.util
import importlib
import importlib.metadata


class Dependency:
    def __init__(self, alias: str, use_case: str) -> None:
        self.module = None
        self.version = None
        self.alias = alias
        self.use_case = use_case

DEPENDENCIES = {
    "pandas": Dependency("pd", "Data manipulation"),
    "numpy": Dependency("np", "Numerical computation"),
    "matplotlib.pyplot": Dependency("plt", "Visualization")
}

imports = {
    "pandas": [None, "Data manipulation"],
    "numpy": [None, "Numerical computation"],
    "matplotlib.pyplot": [None, "Visualization"]
}

ALIASES = {
    "pandas": "pd",
    "numpy": "np",
    "matplotlib.pyplot": "plt"
}

def has_pkg(pkg_name: str) -> bool: 
    return importlib.util.find_spec(pkg_name) is not None


def update_imports_status() -> None:
    for module in imports.keys():
        pkg_name = module.split(".")[0]
        if not has_pkg(pkg_name):
            continue
        imports[module][0] = importlib.metadata.version(pkg_name)


def safe_import(module_name: str) -> None:
    mod = importlib.import_module(module_name)
    globals()[ALIASES[module_name]] = mod 


def import_modules(modules: dict[str, list[str | None, str]]) -> None:
    for module_name in modules.keys():
        safe_import(module_name)
    

def show_import_status() -> None:
    print("LOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")
    for module in imports:
        version = imports[module][0]
        use_case = imports[module][1]
        if version is not None:
            print(f"[OK] {module} ({version}) - {use_case} ready")
        else:
            print(
                f"[KO] {module} not installed.\n\n"
                "Install using pip:\n"
                f"pip install {module}\nor\n"
                f"pip install -r requirements.txt\n\n"
                "Install using Poetry:\n"
                f"poetry add {module}\nor\n"
                "poetry install"
            )


def main() -> None:
    update_imports_status()
    show_import_status()
    if any(None in status for status in imports.values()):
    	return
    import_modules(imports)
    fig, axs = plt.subplots(2,2)
    

    

if __name__ == "__main__":
    main()

    
