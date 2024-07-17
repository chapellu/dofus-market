![Release](https://img.shields.io/github/v/release/chapellu/dofus-market)
![Python](https://img.shields.io/badge/python-3.12-blue.svg?logo=python)
![Django](https://img.shields.io/badge/django-5-green.svg?logo=django)
![Vue.js](https://img.shields.io/badge/vue.js-3-brightgreen.svg?logo=vue.js)
![Vuetify](https://img.shields.io/badge/vuetify-3-blue.svg?logo=vuetify)
[![semantic-release: angular](https://img.shields.io/badge/semantic--release-angular-e10079?logo=semantic-release)](https://github.com/semantic-release/semantic-release)
![Docker](https://img.shields.io/badge/docker-grey?logo=docker)
![Kubernetes](https://img.shields.io/badge/kubernetes-grey?logo=kubernetes)
![Helm](https://img.shields.io/badge/helm-grey?logo=helm)
![Fluxcd](https://img.shields.io/badge/fluxcd-grey?logo=flux)
![Backend tests](https://github.com/chapellu/dofus-market/actions/workflows/test.yml/badge.svg)
# Dofus Market

Welcome to the Dofus Market project! This repository contains the code for both the backend and frontend components of the Dofus Market application.

## Documentation

For detailed documentation, please refer to the `docs` folder.

## Development Setup

### Environment Configuration

To switch between development and production environments, modify the commented code in `config.ts` and set up a `.env` file.

### Backend (Django REST API + Database)

See ![Backend README](backend/README.md)

### Frontend (Vue.js)

#### Setup and Installation

1. **Navigate to the frontend directory and install dependencies:**

    ```shell

    cd dofus_market/frontend

    npm install

    ```

2. **Run the development server:**

    ```shell

    npm run dev

    ```

3. **Build for production:**

    ```shell

    npm run build

    ```

#### Docker Commands

- **Build:**

    ```shell

    export version=1.0.0-alpha.1

    npm run build:docker

    ```


- **Run:**

    ```shell

    npm run serve:docker

    ```

- **Push to Docker Hub:**

    ```shell

    npm run push:docker

    ```

## Production

For production deployment details, refer to the `docs` folder.

## Contributing

Contributions are welcome! Please read our contributing guidelines in `CONTRIBUTING.md` to get started.

## License

This project is licensed under the Apache License 2.0 - see the `LICENSE` file for details.
