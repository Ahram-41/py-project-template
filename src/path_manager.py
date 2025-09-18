import pathlib

_EXPECTED_REPO_ROOT_FILES = ["uv.lock", "pyproject.toml", "README.md"]


def get_repo_root() -> str:
    current_path = pathlib.Path(__file__).resolve().absolute()
    while current_path != current_path.parent:
        if all((current_path / file).exists() for file in _EXPECTED_REPO_ROOT_FILES):
            return str(current_path)
        current_path = current_path.parent
    raise FileNotFoundError("Repository root not found.")


REPO_ROOT = get_repo_root()
REPO_ROOT_PATH = pathlib.Path(REPO_ROOT)


if __name__ == "__main__":
    print("Testing path manager...")

    print(f"REPO_ROOT: type={type(REPO_ROOT)}, value={REPO_ROOT}")
    print(f"REPO_ROOT_PATH: type={type(REPO_ROOT_PATH)}, value={REPO_ROOT_PATH}")
