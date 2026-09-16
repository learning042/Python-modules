import sys
from types import ModuleType
from importlib import import_module


class Dependency:
    def __init__(self, pkg_name: str, use_case: str) -> None:
        self.pkg_name = pkg_name
        self.version = "N/A"
        self.obj: None | ModuleType = None
        self.use = use_case

        
DEPENDENCIES = {
    "pandas": Dependency("pandas", "Data manipulation"),
    "numpy": Dependency("numpy", "Numerical computation"),
    "matplotlib.pyplot": Dependency("matplotlib", "Visualization")
}

np: None | ModuleType = None
pd: None | ModuleType = None
plt: None | ModuleType = None


def import_all(modules: dict[str, Dependency]) -> None:
    for module in modules.keys():
        try:
            dependency = modules[module]
            dependency.obj = import_module(dependency.pkg_name)
            dependency.version = dependency.obj.__version__
            if module == "matplotlib.pyplot":
                dependency.obj = import_module(module)
        except ImportError:
            continue


def show_import_status(modules: dict[str, Dependency]) -> None:
    print("Loading status: Loading programs...\n")
    all_ok = True
    for module in modules.values():
        if module.obj is None:
            print(f"[KO] {module.pkg_name} ({module.version}) - {module.use} not ready")
            all_ok = False
        else:
            print(f"[OK] {module.pkg_name} ({module.version}) - {module.use} ready")
    if not all_ok:
        print(
            "\nThere are missing dependencies.\n"
            "Install with pip:\n"
            "	pip install -r requirements.txt\n"
            "		or\n"
            "	pip install <dependency_0> <dependency_1> ...\n\n"
            "Install with poetry:\n"
            "	poetry add <dependency_0> <dependency_1> ...\n"
            "	poetry install"
        )
        sys.exit(1)


def generate_matrix_data(low: float, high: float, size: tuple[int, int, ...]) -> np.ndarray: 
    return np.random.randint(low, high, size)


def generate_data_image(dataset: np.ndarray) -> None:
    print("Analyzing Matrix data...")
    length = len(dataset)
    df = pd.DataFrame(dataset)
    print(f"Processing {length} data points...")
    fig, axs = plt.subplots(2,1)
    axs[0].plot(df.index, df, label="graph")
    axs[0].set_xlabel("individual")
    axs[0].set_ylabel("power")
    axs[0].legend()
    axs[0].legend(loc='upper center', bbox_to_anchor=(0.5, -0.25))
    axs[1].scatter(df.index, df, alpha=0.4, s=15, label="dispersion")
    axs[1].set_xlabel("individual")
    axs[1].set_ylabel("power")
    axs[1].legend(loc='upper center', bbox_to_anchor=(0.5, -0.25))
    plt.tight_layout()
    plt.savefig("matrix_analysis.png", bbox_inches="tight")
            

def main() -> None:
    global pd
    global np
    global plt
    import_all(DEPENDENCIES)
    show_import_status(DEPENDENCIES)
    pd = DEPENDENCIES["pandas"].obj
    np = DEPENDENCIES["numpy"].obj
    plt = DEPENDENCIES["matplotlib.pyplot"].obj
    dataset = generate_matrix_data(low=0, high=100, size=1000)
    generate_data_image(dataset)
    

if __name__ == "__main__":
    main()
