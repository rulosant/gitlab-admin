from proy import *

project = ""
projects = []


labels = [{'name': 'Back end', 'color': '#85B4FF'},
        {'name': 'Bases de datos', 'color': '#A899FF'},
        {'name': 'Front end', 'color': '#70F3FF'},
        {'name': 'Infraestructura', 'color': '#FFFFD6'},
        {'name': 'Obligatoria', 'color': '#330066'},
        {'name': 'Testing / QA', 'color': '#FFC885'},
        {'name': 'A verificar', 'color': '#36454f'},
        {'name': 'Bug / Error', 'color': '#FF8585'},
        {'name': 'Electiva', 'color': '#FFADFF'},
        {'name': 'En progreso', 'color': '#36454f'}]

milestones = [{'title': 'Sprint 1'},
              {'title': 'Sprint 2'},            
              {'title': 'Sprint 3'},
              {'title': 'Sprint 4'}]
 

while 1:

    if project:
        print("\n Current Project: "+ project.name)
    print("\nOptions:")
    print("""        
        P: Select Project (by id)
        L: List labels
        CL: Create Labels
        M: List Milestones
        CM: Create Milestones
        --
        AN: Create N projects with labels and milestones
        Q: Quit
    """)

    selected = input("Seleccione la opcion\n")

    if selected == "Q" or selected == "q":
        quit()  

    elif selected == "P" or selected == "p":
        project_id = input("project id: ")
        project = gl.projects.get(project_id)
        print(project.name)
    elif selected == "L" or selected == "l":
        list_labels(project)
    elif selected == "CL" or selected == "cl":
        create_labels(project, labels)
    elif selected == "M" or selected == "m":
        list_milestones(project)
    elif selected == "CM" or selected == "cm":
        create_milestones(project, milestones)
    elif selected == "AN" or selected == "an":
        group_id = input("group id: ")
        quantity = int(input("quantity: "))
        prefix = input("name prefix: ")
        projects = create_projects(group_id, quantity, prefix)    

        for project in projects:
            print("")
            print(str(project.id) + "  -  " + project.name)
            create_labels(project, labels)
            create_milestones(project, milestones)