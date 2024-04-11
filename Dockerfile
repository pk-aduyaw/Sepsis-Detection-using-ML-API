# Define base of file
FROM python:3.10.9 

# Create working directory
WORKDIR /app    

# Copy requirements.txt into tmp folder
COPY requirements.txt /tmp/requirements.txt     

# Pip install packages in requirements.txt file
RUN python -m pip install -r /tmp/requirements.txt

# Copy everything into the app folder
COPY . /app

# Indicate port to expose
EXPOSE 6000

# Run app
CMD ["uvicorn","main:app","--host","0.0.0.0","--port", "6000"]