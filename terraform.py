import subprocess

def terraform_run(command):
    process = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE)
    
directory = "<directory path of terraform files>"
command = f"terraform -chdir={directory} init"     #command to init terraform configurations
command = f"terraform -chdir={directory} plan"      #command to view plan of terraform configurations

terraform_run(command)

