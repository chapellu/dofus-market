FROM nginx:stable-alpine

RUN apk update

# Bundle app source
COPY dist /usr/share/nginx/html

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]