

w1: 規劃 project structure by DMLM
w2: 分段寫CODE
w3: tox, pytest
w4: pydantic, lint 
w5: fast api
w6: heroku
w7: CI
w8: CD


process data:
    rename
    column name lower
    recode 類別型 e.g. pay_0

freature engineering:
	# 數值型
	limit_bal
	age
	bill_amt_1
	pay_amt_1

	# 類別型
	sex
	education
	mariage
	pay_0


	# 次數類
    fullpay_l6m, l3m
    revolve_l6m, l3m
    nobill_l6m, l3m
    default_l6m, l3m
    wstpay_l6m, l3m

    # unpaid amt 類
    unpaid_amt_l6m, l3m, l1m

    # bill amt 類
    sum_bill_amt_l6m, l3m
    avg_bill_amt_l6m, l3m
    std_bill_amt_l6m
    max_bill_amt_l6m, l3m
    min_bill_amt_l6m, l3m
    range_bill_amt_l6m, l3m
    min_bill_amt_f3m
    growingrt_bill_amt

    # pay amt 類
	sum_pay_amt_l6m, l3m
	avg_pay_amt_l6m, l3m
	std_pay_amt_l6m
	max_pay_amt_l6m, l3m
	min_pay_amt_l6m, l3m
	range_pay_amt_l6m, l3m

	# 相除類
	avg_ultrt_l6m, l3m, l1m
	avg_revolve_l6m, l3m, l1m

training:
    data split
    model building
    model training with cv
    save model

predict:
   load model
   feature engineering





