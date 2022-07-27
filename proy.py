import gitlab
import requests
from credentials import *
#from pprint import pprint

# Create Milestones in project from a list of milestones
#
# milestones: [{'title': 'Sprint 1'}, {'title': 'Sprint 2'}]
def create_milestones(project, milestones):
    p_milestones = project.milestones.list()
    for m in p_milestones:
        print(m)
    
    print("Creating milestones...")
    for milestone in milestones:
        project.milestones.create(milestone)
    
    print("\nCurrent Milestones:")
    p_milestones = project.milestones.list()
    for m in p_milestones:
        print(m.title)

def list_milestones(project):
    print("Current Milestones:")
    p_milestones = project.milestones.list()
    for m in p_milestones:
        print(m.title)

# Create labels in project from a given list of labels
#
# labels: list of dictionaries: [{'name': 'Name1', 'color': '#85B4FF'}, {'name': 'Name2', 'color': '#FFFFF'}]

def create_labels(project, labels):
    current_labels = project.labels.list()
    #pprint(labels[0].attributes)

    print("Creating labels...")

    for label in current_labels:
        print(label.name + "	"+ label.color)

    for label in labels:
        project.labels.create(label)

    print("\nCurrent labels:")
    current_labels = project.labels.list()
    for label in current_labels:
        print(label.name + "	"+ label.color)

def list_labels(project):
    labels = project.labels.list()

    for label in labels:
        print(label.name + "	"+ label.color)
    

#groups
def create_subgroup(name, path, parent_id):
	subgroup = gl.groups.create({'name': name, 'path': path, 'parent_id': parent_id})
	#pprint(subgroup.attributes)


#Creates N projects named prefix+number
def create_projects(namespace_id, cant, prefix):
    projects=[]
    for i in range(1,cant+1): #Cantidad
        if i < 10:
            project_name = prefix + "-0"+str(i)
        else:
            project_name = prefix + "-"+str(i)

        project = gl.projects.create({'name': project_name, 'namespace_id': namespace_id})
        print(project_name + "	"+ str(project.id))
        projects.append(project)

    return projects

def commit_file(project):
    upload_file = open("README.md", "r")

    f = project.files.create({'file_path': 'README.md',
                          'branch': 'main',
                          'content': upload_file.read(),
                          'author_email': 'test@example.com',
                          'author_name': 'yourname',
                          'commit_message': 'Create initial file'})



def update_file(project):
    f = project.files.get(file_path='README.md', ref='main')

    upload_file = open("README.md", "r")
    f.content = upload_file.read()
    f.save(branch='main', commit_message='Update testfile')



#Creates N projects for a given group
def create_complete_projects(group_id, cant, labels):
    
    prefix = "team"
    projects = create_projects(group_id, cant, prefix)

    for project in projects:
        print("")
        print(str(project.id) + "  -  " + project.name)
        create_labels(project, labels)
        create_milestones(project, milestones)
#        update_file(project)
        #commit_file(project)


#create_complete_projects(822, 5, [{'name': 'name1'},{'name': 'name2'}])

#create_projects(620, 3, 'team')

