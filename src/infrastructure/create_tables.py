projects = """
    CREATE TABLE IF NOT EXISTS `projects` (
    `id` integer PRIMARY KEY,
    `name` varchar(255),
    `key` varchar(255) UNIQUE,
    FOREIGN KEY(`id`) REFERENCES todo_lists (`project_id`)
    )
"""

todo_list = """
    CREATE TABLE IF NOT EXISTS `todo_lists` (
    `id` integer PRIMARY KEY,
    `name` varchar(255),
    `project_id` integer,
    FOREIGN KEY(`id`) REFERENCES tasks (`todo_list_id`)
    )
"""

tasks = """
    CREATE TABLE IF NOT EXISTS `tasks` (
    `id` integer PRIMARY KEY,
    `title` varchar(255),
    `description` varchar(255),
    `completed` bool,
    `todo_list_id` integer
    );
"""





