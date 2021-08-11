# airflow tutorial

```bash
git clone https://github.com/J-TKim/airflow_tutorial
cd airflow

pip install -r requirements.txt

airflow initdb

airflow webserver -p 8080

# open another terminal
airflow scheduler
```

더 많은 설명은 [여기](https://j-tkim.github.io/mlops/2021/08/11/airflow1/)에서 볼 수 있습니다.