import sys
from types import ModuleType
from importlib import import_module
from typing import Any


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
    print("LOADING STATUS: Loading programs...\n")
    all_ok = True
    print("Checking dependencies:")
    for module in modules.values():
        if module.obj is None:
            print(
                    f"[KO] {module.pkg_name} ({module.version}) "
                    f"- {module.use} not ready"
            )
            all_ok = False
        else:
            print(
                    f"[OK] {module.pkg_name} ({module.version}) "
                    f"- {module.use} ready"
            )
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


def show_pip_vs_poetry() -> None:
    print(
            "\nDependency management:\n"
            "pip    : requirements.txt, install what is listed\n"
            "Poetry : pyproject.toml + poetyr.lock. manages its own venv"
    )

def generate_matrix_data(low: int, high: int, size: int) -> Any:
    assert isinstance(np, ModuleType)
    return np.random.randint(low, high, size)


def generate_data_image(dataset: Any, filename: str) -> None:
    assert isinstance(pd, ModuleType) and isinstance(plt, ModuleType)
    print("\nAnalyzing Matrix data...")
    length = len(dataset)
    df = pd.DataFrame(dataset)
    print(f"Processing {length} data points...")
    fig, axs = plt.subplots(2, 1)
    axs[0].plot(df.index, df, label="graph")
    axs[0].set_xlabel("index")
    axs[0].set_ylabel("value")
    axs[0].legend(loc='upper center', bbox_to_anchor=(0.5, -0.25))
    axs[1].scatter(df.index, df, alpha=0.4, s=15, label="dispersion")
    axs[1].set_xlabel("Index")
    axs[1].set_ylabel("Value")
    axs[1].legend(loc='upper center', bbox_to_anchor=(0.5, -0.25))
    plt.tight_layout()
    print("Generating visualization...")
    plt.savefig(filename, bbox_inches="tight")
    print("\nAnalysis complete!")
    print(f"Results saved to: {filename}")


def main() -> None:
    global pd
    global np
    global plt
    import_all(DEPENDENCIES)
    show_import_status(DEPENDENCIES)
    show_pip_vs_poetry()
    pd = DEPENDENCIES["pandas"].obj
    np = DEPENDENCIES["numpy"].obj
    plt = DEPENDENCIES["matplotlib.pyplot"].obj
    dataset = generate_matrix_data(low=0, high=1000, size=100)
    generate_data_image(dataset, "matrix_analysis.png")


if __name__ == "__main__":
    main()
