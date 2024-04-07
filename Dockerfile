FROM python:3.6

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN apt update

# Set GDAL library path
ENV GDAL_LIBRARY_PATH=/usr/lib/libgdal.so

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["sh", "-c", "python manage.py makemigrations Core && python manage.py migrate Core "]
