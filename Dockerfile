FROM python:alpine AS base
WORKDIR /bot

RUN pip install -U discord.py
RUN pip install -U python-dotenv

CMD python3 bot.py