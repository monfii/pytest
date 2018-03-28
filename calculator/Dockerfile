FROM alpine:3.1

# Update
RUN apk add --update python py-pip

# Install app dependencies
RUN pip install Flask

# Bundle app source
COPY calculator.py /src/main.py

EXPOSE  7000
CMD ["python", "/src/main.py", "-p 7000"]