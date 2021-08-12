FROM node:14

# Create app directory
WORKDIR /app

# Install app dependencies
COPY package*.json ./
COPY * ./

RUN npm install
RUN apt-get update
# Copying rest of the application to app directory
COPY . /app

# Expose the port and start the application
Expose 3000

CMD ["npm","i"]

CMD ["npm","run","start"]
