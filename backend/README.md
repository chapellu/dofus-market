# Dofus-market backend

## Dev

First and foremost create a virtualenv

``` shell
python3 -m venv .venv  # Creates a virtual environment named ".venv"
```


Then activate it

<details>
    <summary>Activates the virtual environment on Linux/macOS</summary>
  
``` shell
source .venv/bin/activate  # Activates the virtual environment on Linux/macOS
```

</details>

<details>
    <summary>Activates the virtual environment on Windows</summary>

``` shell
.venv\Scripts\activate  # Activates the virtual environment on Windows
```

</details>


Once that's done you can install the requirements

```shell
poetry install
```

And finally, run the projet

```shell
docker-compose up --build
```

This is going to launch several dockers defined in the docker-compose file. The local directory is mounted inside those dockers so your modification will be taken into account live.

Further commands

```shell
docker-compose exec dofus-market-back dofus_market/manage.py makemigrations
docker-compose exec dofus-market-back dofus_market/manage.py migrate
```

If you make changes to the protofile do not forget to recreate them

```shell
cd grpc_market/grpc
python -m grpc_tools.protoc -I./ --python_out=./ --grpc_python_out=./ --protobuf-to-pydantic_out=./ grpc_market.proto
```

You will also need to sanitize the generated file
<details>
    <summary>On mac</summary>

```shell
sed -i '' 's/_partial_update_fields/partial_update_fields/' grpc_market_p2p.py
sed -i '' 's/import grpc_market_pb2 as grpc__market__pb2/from grpc_market.grpc import grpc_market_pb2 as grpc__market__pb2/g' grpc_market_pb2_grpc.py
```

</details>

<details>
    <summary>On linux</summary>

```shell
sed -i 's/_partial_update_fields/partial_update_fields/g' grpc_market_p2p.py
sed -i 's/import grpc_market_pb2 as grpc__market__pb2/from grpc_market.grpc import grpc_market_pb2 as grpc__market__pb2/g' grpc_market_pb2_grpc.py
```

</details>
