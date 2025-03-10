FROM windows
RUN apt-get update
RUN apt-get install -y curl
RUN curl
COPY package.json package.json
ENTRYPOINT [ "Python" ] 
