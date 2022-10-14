# Edit the enviroment var file and add the proper values
# sudo -H gedit /etc/environment

#  To list environment variables sorted alphabetically
#  env | sort 

#------------------------------------------------------------------------------
# GCP Cloud.  Prepare python Virtual Environmet
#------------------------------------------------------------------------------

sudo apt-get install python3-venv
#sudo apt-get install python3.10-venv

python3 -m venv env_01
source env_01/bin/activate

pip3 install --upgrade pip
python3 -m pip install --upgrade setuptools
pip3 install --no-cache-dir  --force-reinstall -Iv grpcio==1.35.0 

# get code from git
git clone git@github.com:canislatranscoxus/django_projects.git
cd ~/git/django_projects/firstProject/
git pull
git pull --ff-only


pip install -r requirements.txt

#update yaml file




#------------------------------------------------------------------------------
# Deploy to GCP App Engine
#------------------------------------------------------------------------------
# Update Environment variables in app.yaml

gcloud app deploy
gcloud app browse

# monitor and see logs
gcloud app logs tail -s default


#------------------------------------------------------------------------------
# how to renovate credentials
#------------------------------------------------------------------------------

# gcloud config set project  <PROJECT_ID>

gcloud config set project  oasisverde
gcloud auth login --no-launch-browser

#------------------------------------------------------------------------------

