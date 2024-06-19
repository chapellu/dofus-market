FROM node:22-alpine

# Set the working directory inside the container
WORKDIR /app

# Bundle app source
COPY package.json ./
RUN npm install

COPY vite.config.ts ./

COPY dist .


EXPOSE 80
CMD ["npm", "run", "serve"]