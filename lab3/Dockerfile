

# install app dependencies
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# install app
COPY . .

# final configuration
EXPOSE 8501
CMD streamlit run app.py
