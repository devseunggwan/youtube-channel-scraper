sudo apt-get update
sudo apt-get install build-essential libbz2-dev openssl
curl https://pyenv.run | bash

echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc

# Restart your shell for the changes to take effect.
# Load pyenv-virtualenv automatically by adding
# the following to ~/.bashrc:

echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc

# activate bash
source ~/.bashrc

pyenv install 3.11.4
pyenv virtualenv 3.11.4 .venv
pyenv activate .venv

pip install poetry
poetry install
pre-commit install
