```shell

$ docker-compose up --build
$ docker-compose exec dofus-market-back dofus_market/manage.py makemigrations
$ docker-compose exec dofus-market-back dofus_market/manage.py migrate
$ docker-compose exec dofus-market-grpc dofus_market/manage.py generateproto
```

I don't know why but the generateproto command does not create the python file
```
cd dofus_market/grpc_market/grpc
python -m grpc_tools.protoc -I./ --python_out=./ --grpc_python_out=./ grpc_market.proto
```