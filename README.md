# Heyjobs Applications


### Dummy Heyjobs applications training and testing modules to predict number of application for given job using linear regression.

##### To run the app using docker and start celery periodic tasks
```docker
docker build -t job_app .
docker run -it --rm job_app
```


To train the model and save it, add the paths to the setting file and run 
```
python job_app/train.py
```

To test the model on new data, add the paths to the setting file and run 
```
python job_app/test.py
```

#### Todo list:
* TODO: Use multiple models, evaluate and select the best model
* TODO: Fine tune the selected model
* TODO: Add unit tests
* TODO: Add Doc strings
* TODO: Enhance the program reading from generic data sources and write into generic data sources

