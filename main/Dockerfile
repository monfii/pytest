FROM alpine:3.1

# Update
RUN apk add --update python py-pip

# Install app dependencies
RUN pip install Flask
RUN pip install requests

# Bundle app source
COPY main.py /src/main.py

EXPOSE  8000
CMD ["python", "/src/main.py", "-p 8000"]