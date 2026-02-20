# Libs
import os
import git
from git.exc import InvalidGitRepositoryError
from pathlib import Path

# Intern Libs

# Intern Variables
#REPO_PATH = r"C:/Users/haonovi/Desktop/mods_out"
ORIGIN_REPO = str(input("Repository Origin: "))
REPO_PATH = Path(input("Mods folder path: ").strip())

try:
	repo = git.Repo(REPO_PATH)
	print("Repositorio OK!")
except InvalidGitRepositoryError:
	print("Diretório de mods não está versionado!")
	print("Clonando da origem...")
	repo = git.Repo.clone_from(ORIGIN_REPO, REPO_PATH)
except Exception as e:
	print("Erro ao criar o repositorio") 	
	print(type(e).__name__)
	print(str(e))

origin = repo.remotes.origin

try:
	origin.pull()
	print("Mods sincronizados!")
except Exception as e:
	print("Falha ao atualizar os mods")
	print(str(e))

input("Press enter to exit.")
