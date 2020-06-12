FROM ubuntu:20.04
WORKDIR /bot

#update os
RUN apt update && \
	apt upgrade -y

# install python
RUN apt install -y python3 python3-pip

# install discord library build dependencies
RUN apt install -y gcc

#install python dependancies
RUN pip3 install -U discord.py
RUN pip3 install -U python-dotenv
RUN pip3 install -U requests

# copy the code into the image
COPY /bot /bot

# run the entrypoint file
CMD python3 bot.py