## GitLab Admin

This project is used for automating the creation of gitlab projects with labels and milestones. 

It uses Python-GitLab Package and provides an easy way to create multiple copies of a project inside a subgroup. 

It is useful for educational purposes where it is necessary to replicate the same project for different computers.

## Usage

Get your GitLab Token and paste it in credentials.py

Run menu.py and you will see a list of basic actions:
 * Select Project (by id)
 * List labels
 * Create Labels
 * List Milestones
 * Create Milestones

There is an option with a sequence of steps:
  * Create N projects with labels and milestones: It will ask you for:
    * Number of projects
    * Subgroup id
    * Prefix for the projects names



## Links
 * Python-Gitlab Package: https://python-gitlab.readthedocs.io/
