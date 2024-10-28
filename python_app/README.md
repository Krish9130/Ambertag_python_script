
nohup python app.py >> /opt/flask/app.out 2>&1 &


nohup python log_monitor.py >> "/opt/flask/monitor.out" 2>&1 &
