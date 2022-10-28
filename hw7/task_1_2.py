import os
import yaml
from contextlib import suppress

config_file = r'config.yaml'
root_dir = os.path.abspath(os.getcwd())
with open(config_file) as file:
    structure = yaml.safe_load(file)


def create_tree(tree_item, root=root_dir):
    with suppress(FileExistsError):
        if isinstance(tree_item, list):
            for path in tree_item:
                create_tree(path, root)
        if isinstance(tree_item, dict):
            for folder, children in tree_item.items():
                current_root = os.path.join(root, folder)
                os.mkdir(current_root)
                create_tree(children, current_root)
        if isinstance(tree_item, str):
            open(os.path.join(root, tree_item), mode='a').close()


if __name__ == '__main__':
    create_tree(structure, root_dir)
