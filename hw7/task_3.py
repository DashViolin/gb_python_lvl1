import shutil
import os
from contextlib import suppress

from task_1_2 import root_dir, structure


def collect_templates(project_folder, templates_folder_name='templates'):
    templates_folder = os.path.join(project_folder, templates_folder_name)
    with suppress(FileExistsError):
        os.mkdir(templates_folder)
        for root, dirs, files in os.walk(project_folder):
            if os.path.split(root)[-1] == templates_folder_name:
                content = os.listdir(root)
                for entry in content:
                    copy_from = os.path.join(root, entry)
                    copy_to = os.path.join(templates_folder, entry)
                    shutil.copytree(copy_from, copy_to)


if __name__ == '__main__':
    project_root = os.path.join(root_dir, list(structure.keys())[0])
    collect_templates(project_root)
