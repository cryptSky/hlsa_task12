### Setup

1. Install docker
2. Install siege

## Steps to run

1. `docker-compose up --build` 
   

### Results


`siege -c100 -t240S --content-type "application/json" 'http://localhost:8000/users POST {"type": "redis"}'`
```console
Transactions:                 128833 hits
Availability:                 100.00 %
Elapsed time:                 239.25 secs
Data transferred:               6.00 MB
Response time:                  0.19 secs
Transaction rate:             538.49 trans/sec
Throughput:                     0.03 MB/sec
Concurrency:                   99.94
Successful transactions:      128833
Failed transactions:               0
Longest transaction:            0.29
Shortest transaction:           0.02
```

`siege -c100 -t240S --content-type "application/json" 'http://localhost:8000/users POST {"type": "redis-aof"}'`

```console
Transactions:                 127944 hits
Availability:                 100.00 %
Elapsed time:                 239.69 secs
Data transferred:               5.96 MB
Response time:                  0.19 secs
Transaction rate:             533.79 trans/sec
Throughput:                     0.02 MB/sec
Concurrency:                   99.94
Successful transactions:      127944
Failed transactions:               0
Longest transaction:            0.48
Shortest transaction:           0.02
```


`siege -c100 -t240S --content-type "application/json" 'http://localhost:8000/users POST {"type": "beanstalkd"}'`

```console
Transactions:                 120220 hits
Availability:                 100.00 %
Elapsed time:                 239.25 secs
Data transferred:               5.60 MB
Response time:                  0.20 secs
Transaction rate:             502.49 trans/sec
Throughput:                     0.02 MB/sec
Concurrency:                   99.94
Successful transactions:      120220
Failed transactions:               0
Longest transaction:            0.57
Shortest transaction:           0.00
```
