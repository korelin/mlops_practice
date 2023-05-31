#!/bin/bash

script_dir=$1
data_dir=$2
dataset_name=$3

# Директории для данных
if  [ -z  "${data_dir}" ]
then
#   data_dir="$HOME/content$(date +%Y%m%d%H%M%S)"
#   data_dir="$(pwd)/content$(date +%Y%m%d%H%M%S)"
   data_dir="$(pwd)/content"
fi

if  [ -z  "${script_dir}" ]; then
  script_dir="$(pwd)"
fi
if [[ ! -d "$script_dir" && ! -L "$script_dir" ]] ; then
    echo "Указанного каталога для скриптов не существует."
    echo "Программа завершена."
    exit 3
fi
if [ !  -r "$script_dir" ] ; then
  echo "Невозможно получить доступ к каталогу со скриптами."
  echo "Программа завершена."
  exit 4
fi

if  [ -z  "${data_type}" ]
  dataset_name = 'moons'

mkdir -m ug+rw -p "$data_dir"
mkdir -m ug+rw -p "$data_dir/test"
mkdir -m ug+rw -p "$data_dir/train"

if [[  ! -r "$data_dir" || ! -w "$data_dir" ]] ; then
  echo "Невозможно получить доступ к каталогу данных."
  echo "Программа завершена."
  exit 2
fi

# Если venv не установлен:
#sudo apt-get install python3-venv

venv_dir="$script_dir/env"

if [[ ! -d "$venv_dir" && ! -L "$venv_dir" ]] ; then
  python3 -m venv "$venv_dir"
fi
source "$venv_dir/bin/activate"
pip install -r requirements.txt &> /dev/null

python_scripts=([0]='data_creation.py' [1]='data_preprocessing.py'  [2]='model_preparation.py'  [3]='model_testing.py')

for python_script in "${python_scripts[@]}"
do
  full_path=$script_dir/$python_script
  if [ -s "$full_path" ]; then
    echo "Executing $python_script"
    chmod ugo+x "$full_path"

    #result=python3 "$full_path" -d "$data_dir"
    if  python3 "$full_path" -d "$data_dir" -t "dataset_name"
    then
      echo   "$python_script is done"
    else
    #  echo $result
      echo    "$python_script is not done"
    fi
  else
    echo "$python_script not found"
  fi
done

deactivate
