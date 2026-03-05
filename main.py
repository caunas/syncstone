# Libs
import os
import git
from git.exc import InvalidGitRepositoryError, GitCommandError
from pathlib import Path

# Intern Libs

# Intern Variables
ORIGIN_REPO = str(input("Repository Origin: "))
REPO_PATH = Path(input("Mods folder path: ").strip())

try:
	repo = git.Repo(REPO_PATH)
except InvalidGitRepositoryError:
	try:
		print("Diretório de mods não está versionado!")
		print("Ajustando...")
		repo = git.Repo.clone_from(ORIGIN_REPO, REPO_PATH)
	except GitCommandError:
		# Corrige bug de arquivos existentes
		repo = git.Repo.init(REPO_PATH)
		if "origin" not in [r.name for r in repo.remotes]:
			repo.create_remote("origin", ORIGIN_REPO)
except Exception as e:
	print("Erro ao criar o repositorio.") 	
	print(type(e).__name__)
	print(str(e))

origin = repo.remotes.origin
origin.fetch()
print("Syncstone OK!")


try:
	print("Sincronizando mods...")
	origin.pull()
	print("Mods sincronizados!")
except GitCommandError:
	# Corrige bug de arquivos existentes
	if os.path.exists(os.path.join(REPO_PATH, "info.txt")):
		print("Atualizando arquivo info...")
	else:
		print("Atualizando arquivos...")
	repo.git.reset("--hard", "origin/main")
	origin.pull(
		"main",	
		allow_unrelated_histories = True
	)
	print("Mods sincronizados!")
except Exception as e:
	print("Falha ao atualizar os mods")
	print(type(e).__name__)
	print(str(e))

input("Press enter to exit.")
