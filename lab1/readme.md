# clear installation into VBox Ubuntu 22.04 and run lab1
```
sudo apt install python3.10-venv git curl
mkdir projects
cd projects
git clone https://github.com/ViktorRtm/mlops_practice.git
cd ~
mkdir python_venv
python3 -m venv python_venv/lab1
source ~/python_venv/lab1/bin/activate
cd ./projects/mlops_practice/lab1
bash ./pipeline.sh
```
