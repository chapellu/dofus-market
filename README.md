# dofus-market

For more documentation see the docs folder

## Dev

For now, you have to switch commented code in settings.py and config.ts to switch between dev and prod mode

### Backend REST API + Database (Django)

Install dependencies

```shell
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Migrate database and run dev server

```shell
cd dofus_market
python manage.py makemigrations market
python manage.py migrate
python manage.py runserver
```

Docker build

```shell
export version=1.0.0-alpha.1
docker build -t chapellu/dofus-market-backend:${version} -f deploy/Dockerfile .
```

Docker run

```shell
docker run -p 8000:8000 --name dofus-market-backend chapellu/dofus-market-backend:${version}
```

Docker push to dockerhub

```shell
docker push chapellu/dofus-market-backend:${version}
```

### Frontend (vuejs)

Install dependencies

```shell
cd dofus_market/frondend
npm install
```

Run dev server

```shell
npm run dev
```

Compiles and minifies for production

```shell
npm run build
```

#### Docker

Docker build

```shell
export version=1.0.0-alpha.1
npm run build:docker
```

Docker run

```shell
npm run serve:docker
```

Docker push to dockerhub

```shell
npm run push:docker
```

## Production

