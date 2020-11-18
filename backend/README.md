## 시작하기

``` bash
// s03p31a207/backend 디렉토리
py manage.py runserver

aws 에선 
python3 manage.py runserver
```


# models.py 를 이용해 mysqlworkbench 에 table 생성하는법 

출처: https://django-document-korean.readthedocs.io/ko/master/intro/tutorial02.html 

## models.py에 DB 테이블로 넣을 class를 생성한다. 
ex) class User(models.Model):
    uid = models.UUIDField(db_column='UID', primary_key=True, default=uuid.uuid4, editable=False)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=45, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=45, blank=True, null=True)  # Field name made lowercase.
    img = models.CharField(db_column='IMG', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
    #   managed =false -> 이 줄을 지워줘야 django 가 생성할 수 있다.
        db_table = 'USER'

## INSTALLED_APPS 에 user.apps.UserConfig 를 등록한다. 
-> 이제 django 는 user app 이 포함된 것을 알게되었다.
ex)   INSTALLED_APPS = [
    ...,
 'user.apps.UserConfig',
]

## migrations 를 만든다. (변경사항을 migration 으로 저장시키고 싶다고 django 에게 알림)
python manage.py makemigrations user

-> (성공시 0001로 숫자가 뜰것이다. 다음단계에서 사용한다. )

## sqlmigrate 를 이용해 migration 내용을 sql 로 변환한다. 
python manage.py sqlmigrate user 0001

## migrations 에 따라 필요한 데이터베이스 테이블을 생성한다. 
python manage.py migrate 

