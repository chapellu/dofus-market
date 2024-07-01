FROM node:22-alpine AS build

# Set the working directory inside the container
WORKDIR /app

# Bundle app source
COPY package.json ./
RUN npm install

COPY index.html .
COPY tsconfig.json .
COPY tsconfig.node.json .
COPY vite.config.ts .
COPY package.json .
COPY src/ /app/src/


RUN npm run build

FROM node:22-alpine

COPY package.json ./
RUN npm install

COPY vite.config.ts ./
COPY --from=build /app/dist .


EXPOSE 80
CMD ["npm", "run", "serve"]