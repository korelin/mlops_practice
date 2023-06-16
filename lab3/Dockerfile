# syntax=docker/dockerfile:1
FROM python:3.10

# create working directory
WORKDIR /app

# install app dependencies
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# install app
COPY . .

# final configuration
EXPOSE 8501
CMD streamlit run app.py
