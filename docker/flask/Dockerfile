# FROM python:3.8

# WORKDIR /home/myApp

# COPY . /home/myApp

# #RUN pip3 --no-cache-dir install -r requirements.txt
# RUN pip install -r requirements.txt

# EXPOSE 5000

# ENTRYPOINT ["python3"]

# CMD ["app.py"]

FROM python:alpine3.7

WORKDIR /home/myApp

COPY . /home/myApp

RUN apk update && apk upgrade

RUN apk add gcc

RUN apk add curl

# This following line is important
RUN apk add build-base 

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python3"]

CMD ["app.py"]