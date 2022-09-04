# Invoice Django Project

`environment` Python Project Full Setup

```base
git clone https://github.com/mohammadanarul/invoice-django.git
cd invoice-django
pip install virtualenv
virtualenv venv
```

`windows` virtualenv activate
```base
.\venv\Scripts\activate
```

`linux & mac` virtualenv activate
```base
source venv/bin/activate
```

install all package `requirements.txt` and project `run`
```base
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

windows, linux and mac virtualenv environment `deactive`
```base
deactivate
```