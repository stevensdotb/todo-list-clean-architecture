projects = """
    CREATE TABLE IF NOT EXISTS `projects` (
    `id` integer PRIMARY KEY,
    `name` varchar(255),
    `key` varchar(255) UNIQUE,
    FOREIGN KEY(`id`) REFERENCES tasks (`project_id`) ON DELETE CASCADE
    )
"""

tasks = """
    CREATE TABLE IF NOT EXISTS `tasks` (
    `id` integer PRIMARY KEY,
    `key` varchar(255) UNIQUE,
    `title` varchar(255),
    `description` varchar(255),
    `completed` bool,
    `project_id` integer
    );
"""





