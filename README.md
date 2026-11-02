# flask-demo

Flask + SQLite app deployed with Ansible.

## Run locally
    pip3 install -r requirements.txt
    python3 app.py
    # open http://localhost:5000

## Deploy with Ansible
1. Edit inventory.ini and set your server IP, user and SSH key.
2. Run:
       ansible-playbook -i inventory.ini deploy.yml
3. Open http://<your-server-ip>:5000
