FROM node:16-buster

# set working directory
WORKDIR /app

# add `/app/node_modules/.bin` to $PATH
ENV PATH /app/node_modules/.bin:$PATH

# install app dependencies
COPY ./package.json ./package-lock.json ./
RUN npm install

# add app
COPY . .

EXPOSE 3000

# start app
CMD ["npm", "start"]
